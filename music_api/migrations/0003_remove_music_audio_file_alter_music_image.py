# Generated by Django 4.0.5 on 2022-06-01 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_api', '0002_alter_music_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='audio_file',
        ),
        migrations.AlterField(
            model_name='music',
            name='image',
            field=models.CharField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIS9NmMDZNSiXrq6Q1C62ihL3MuLsXLfUw2w&usqp=CAU', max_length=600),
        ),
    ]
