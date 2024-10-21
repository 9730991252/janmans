# Generated by Django 5.1.2 on 2024-10-20 12:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0004_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post_views',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=None)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='owner.post')),
            ],
        ),
    ]
