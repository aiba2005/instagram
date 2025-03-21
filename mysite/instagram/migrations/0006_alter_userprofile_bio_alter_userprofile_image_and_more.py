# Generated by Django 5.1.7 on 2025-03-15 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0005_alter_follow_follower_alter_follow_following'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user_images/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
