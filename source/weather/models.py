from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
import uuid
# Create your models here.
class SearchHistory(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    user = models.ForeignKey(User, related_name="search_history",
                             on_delete=models.CASCADE)
    keyword = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)