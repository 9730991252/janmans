# Generated by Django 5.1.2 on 2024-10-20 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
