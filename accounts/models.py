# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('parent', 'Parent/Individual'),
        ('school', 'School'),
        ('admin', 'Admin'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='parent')
    # Additional fields can be added here

    # Add these lines to resolve the SystemCheckError
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='accounts_user_set', # IMPORTANT: Unique related_name
        related_query_name='accounts_user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='accounts_user_permissions_set', # IMPORTANT: Unique related_name
        related_query_name='accounts_user_permission',
    )

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"