# Generated by Django 3.0.6 on 2020-05-27 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_note_access'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='access',
        ),
        migrations.AddField(
            model_name='note',
            name='access',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]
