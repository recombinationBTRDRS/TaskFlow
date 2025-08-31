from sqlalchemy import (
    Column, Integer, String, Text, DateTime, ForeignKey, 
    Table, CheckConstraint, Index
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timedelta
from .base import Base, TimestampMixin

# Association table for many-to-many Task-Tag relationship
task_tags = Table(
    'task_tags',
    Base.metadata,
    Column('task_id', Integer, ForeignKey('tasks.id', ondelete='CASCADE'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id', ondelete='CASCADE'), primary_key=True),
    Index('ix_task_tags_task_id', 'task_id'),
    Index('ix_task_tags_tag_id', 'tag_id')
)

class Task(Base, TimestampMixin):
    __tablename__ = "tasks"
    
    # Basic fields
    title = Column(String(200), nullable=False, index=True)
    description = Column(Text, nullable=True)
    
    # Foreign keys
    category_id = Column(
        Integer,
        ForeignKey("categories.id", ondelete="RESTRICT"),
        nullable=False,
        index=True
    )
    subcategory_id = Column(
        Integer,
        ForeignKey("subcategories.id", ondelete="SET NULL"),
        nullable=True,
        index=True
    )
    
    # Time tracking
    start_time = Column(DateTime(timezone=True), nullable=True, index=True)
    end_time = Column(DateTime(timezone=True), nullable=True, index=True)
    duration = Column(Integer, nullable=True)  # Duration in seconds
    
    # Relationships
    category = relationship("Category", back_populates="tasks")
    subcategory = relationship("Subcategory", back_populates="tasks")
    tags = relationship(
        "Tag",
        secondary=task_tags,
        back_populates="tasks"
    )
    
    # Constraints
    __table_args__ = (
        CheckConstraint(
            'start_time IS NOT NULL OR duration IS NOT NULL',
            name='check_time_or_duration'
        ),
        CheckConstraint(
            'end_time IS NULL OR start_time IS NOT NULL',
            name='check_end_requires_start'
        ),
        CheckConstraint(
            'duration IS NULL OR duration > 0',
            name='check_positive_duration'
        ),
        Index('ix_tasks_start_time_desc', 'start_time', postgresql_using='btree'),
        Index('ix_tasks_category_start_time', 'category_id', 'start_time'),
    )
    
    @hybrid_property
    def calculated_duration(self) -> int | None:
        """Calculate duration from start_time and end_time if not set explicitly"""
        if self.duration is not None:
            return self.duration
        
        if self.start_time and self.end_time:
            delta = self.end_time - self.start_time
            return int(delta.total_seconds())
        
        return None
    
    @hybrid_property
    def calculated_end_time(self) -> datetime | None:
        """Calculate end_time from start_time and duration if not set explicitly"""
        if self.end_time is not None:
            return self.end_time
            
        if self.start_time and self.duration:
            return self.start_time + timedelta(seconds=self.duration)
            
        return None
    
    @hybrid_property
    def is_active(self) -> bool:
        """Check if task is currently active (started but not finished)"""
        return self.start_time is not None and self.end_time is None and self.duration is None
    
    @hybrid_property
    def is_completed(self) -> bool:
        """Check if task is completed"""
        return (self.end_time is not None) or (self.start_time is not None and self.duration is not None)
    
    def __repr__(self):
        return f"<Task(id={self.id}, title='{self.title[:30]}...', category_id={self.category_id})>"