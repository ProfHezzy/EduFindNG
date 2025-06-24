from django.db import models
from accounts.models import User

class SchoolProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='school_profile')
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    school_type = models.CharField(max_length=50)
    academic_programs = models.TextField()
    admission_requirements = models.TextField()
    fee_structure = models.TextField()
    website = models.URLField(blank=True, null=True)
    social_media = models.CharField(max_length=255, blank=True, null=True)
    highlights = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class SchoolMedia(models.Model):
    school = models.ForeignKey(SchoolProfile, on_delete=models.CASCADE, related_name='media')
    image = models.ImageField(upload_to='school_images/', blank=True, null=True)
    video = models.FileField(upload_to='school_videos/', blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

class SchoolEvent(models.Model):
    school = models.ForeignKey(SchoolProfile, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.school.name}"
