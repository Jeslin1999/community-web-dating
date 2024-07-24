# Generated by Django 5.0.6 on 2024-07-01 08:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_employmentinfo_relationship_goal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='images',
        ),
        migrations.RemoveField(
            model_name='user',
            name='video',
        ),
        migrations.CreateModel(
            name='ProfileImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='upload/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]