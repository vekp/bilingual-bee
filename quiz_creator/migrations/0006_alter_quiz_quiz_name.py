# Generated by Django 5.0.6 on 2024-06-14 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_creator', '0005_quiz_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='quiz_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
