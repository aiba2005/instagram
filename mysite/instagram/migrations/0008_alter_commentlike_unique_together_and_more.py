# Generated by Django 5.1.7 on 2025-03-16 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0007_comment_text_en_comment_text_ru_post_description_en_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='commentlike',
            unique_together={('user', 'comment')},
        ),
        migrations.AlterUniqueTogether(
            name='postlike',
            unique_together={('user', 'post')},
        ),
    ]
