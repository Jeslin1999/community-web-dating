# Generated by Django 5.0.6 on 2024-07-03 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_remove_user_dob_remove_user_address_remove_user_bio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True),
        ),
    ]