from sqlalchemy import Column, Integer, DateTime, func
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime

class Base(DeclarativeBase):
    """Base model with common fields"""
    pass

class TimestampMixin:
    """Mixin for created_at and updated_at timestamps"""
    
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(
        DateTime(timezone=True), 
        server_default=func.now(),
        nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id})>"