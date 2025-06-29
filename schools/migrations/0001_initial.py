# Generated by Django 5.2.3 on 2025-06-24 14:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_phone', models.CharField(max_length=20)),
                ('school_type', models.CharField(max_length=50)),
                ('academic_programs', models.TextField()),
                ('admission_requirements', models.TextField()),
                ('fee_structure', models.TextField()),
                ('website', models.URLField(blank=True, null=True)),
                ('social_media', models.CharField(blank=True, max_length=255, null=True)),
                ('highlights', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='school_profile', to='accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='school_images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='school_videos/')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to='schools.schoolprofile')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='schools.schoolprofile')),
            ],
        ),
    ]
