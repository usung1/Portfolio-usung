# Generated by Django 4.2.5 on 2024-01-31 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_post_content_alter_postimage_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='내용'),
        ),
    ]
