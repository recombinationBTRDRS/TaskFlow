from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship
from .base import Base, TimestampMixin

class Tag(Base, TimestampMixin):
    __tablename__ = "tags"
    
    name = Column(String(50), nullable=False, unique=True, index=True)
    color = Column(String(7), nullable=False, default="#10B981")  # Hex color
    description = Column(Text, nullable=True)
    
    # Many-to-many relationship with tasks
    tasks = relationship(
        "Task",
        secondary="task_tags",
        back_populates="tags"
    )
    
    def __repr__(self):
        return f"<Tag(id={self.id}, name='{self.name}')>"