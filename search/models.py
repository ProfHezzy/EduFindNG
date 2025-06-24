from django.db import models
from accounts.models import User
from schools.models import SchoolProfile

class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='search_histories')
    query = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class SchoolComparison(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comparisons')
    schools = models.ManyToManyField(SchoolProfile)
    created_at = models.DateTimeField(auto_now_add=True)
