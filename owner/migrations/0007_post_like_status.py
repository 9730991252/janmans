# Generated by Django 5.1.2 on 2024-10-20 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0006_post_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_like',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]
