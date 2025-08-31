from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base, TimestampMixin

class Category(Base, TimestampMixin):
    __tablename__ = "categories"
    
    name = Column(String(100), nullable=False, unique=True, index=True)
    color = Column(String(7), nullable=False, default="#3B82F6")  # Hex color
    description = Column(Text, nullable=True)
    
    # Relationships
    subcategories = relationship(
        "Subcategory", 
        back_populates="category",
        cascade="all, delete-orphan"
    )
    tasks = relationship(
        "Task", 
        back_populates="category",
        cascade="all, delete-orphan"
    )
    
    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"

class Subcategory(Base, TimestampMixin):
    __tablename__ = "subcategories"
    
    name = Column(String(100), nullable=False, index=True)
    category_id = Column(
        Integer, 
        ForeignKey("categories.id", ondelete="CASCADE"), 
        nullable=False,
        index=True
    )
    description = Column(Text, nullable=True)
    
    # Relationships
    category = relationship("Category", back_populates="subcategories")
    tasks = relationship(
        "Task", 
        back_populates="subcategory",
        cascade="all, delete-orphan"
    )
    
    def __repr__(self):
        return f"<Subcategory(id={self.id}, name='{self.name}', category_id={self.category_id})>"