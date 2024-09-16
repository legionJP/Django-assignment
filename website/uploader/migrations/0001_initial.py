# Generated by Django 5.1.1 on 2024-09-15 22:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('v_file', models.FileField(upload_to='videos/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('processed_status', models.BooleanField(default=False)),
                ('subtitles', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subtitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=10)),
                ('file', models.FileField(default='subtitles/placeholder.srt', upload_to='subtitles/')),
                ('content', models.TextField()),
                ('start_time', models.FloatField(default=0.0)),
                ('end_time', models.FloatField(default=0.0)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_subtitles', to='uploader.videos')),
            ],
        ),
    ]
