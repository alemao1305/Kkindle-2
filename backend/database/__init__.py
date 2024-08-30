# backend/database/__init__.py

from .models import BookModel
from .mongodb_config import db

__all__ = ['BookModel', 'db']
