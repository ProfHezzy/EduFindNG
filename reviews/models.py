from django.db import models
from schools.models import SchoolProfile
from accounts.models import User

class Review(models.Model):
    school = models.ForeignKey(SchoolProfile, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    academics = models.PositiveSmallIntegerField(default=0)
    facilities = models.PositiveSmallIntegerField(default=0)
    faculty = models.PositiveSmallIntegerField(default=0)
    safety = models.PositiveSmallIntegerField(default=0)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.school.name} - {self.user.username} ({self.rating})"

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

class Like(models.Model):
    school = models.ForeignKey(SchoolProfile, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('school', 'user')
