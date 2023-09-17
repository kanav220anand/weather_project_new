import uuid

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class SearchHistory(models.Model):
    """Stores data about searches made by user"""
    id           = models.UUIDField(primary_key=True, 
                                    editable=False, unique=True, 
                                    default=uuid.uuid4)
    user         = models.ForeignKey(User, related_name="search_history",
                             on_delete=models.CASCADE)
    keyword      = models.CharField(max_length=256)
    created_at   = models.DateTimeField(auto_now_add=True)
    found_result = models.BooleanField(default=True)
