# Generated by Django 5.0.6 on 2024-06-23 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_user_height_user_rel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='community',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='drinking',
            field=models.CharField(choices=[('R', 'Regular'), ('S', 'Socialy'), ('O', 'Occasionally'), ('T', 'Teetotaler'), ('P', 'Plan to Quit')], default='T', max_length=1),
        ),
        migrations.AddField(
            model_name='user',
            name='fath',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='images',
            field=models.FileField(blank=True, null=True, upload_to='upload/'),
        ),
        migrations.AddField(
            model_name='user',
            name='mother_tonge',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='smoke',
            field=models.CharField(choices=[('N', 'No'), ('Y', 'Yes'), ('P', 'Plan to Quit')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='user',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='upload/'),
        ),
    ]