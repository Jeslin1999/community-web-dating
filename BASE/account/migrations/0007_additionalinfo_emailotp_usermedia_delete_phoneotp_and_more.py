# Generated by Django 5.0.6 on 2024-07-03 12:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_phoneotp_remove_user_is_verified_remove_user_otp_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobbies', models.CharField(help_text='Enter up to 5 hobbies separated by commas', max_length=255)),
                ('intrested_in', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('both', 'Both')], max_length=50)),
                ('drinking_habits', models.CharField(choices=[('non_drinker', 'Non-Drinker'), ('social_drinker', 'Social Drinker'), ('regular_drinker', 'Regular Drinker')], default='non_drinker', max_length=20)),
                ('smoking_habits', models.CharField(choices=[('non_smoker', 'Non-Smoker'), ('occasional_smoker', 'Occasional Smoker'), ('regular_smoker', 'Regular Smoker')], default='non_smoker', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='EmailOTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('otp', models.CharField(blank=True, max_length=6, null=True)),
                ('is_verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('additional_image1', models.ImageField(blank=True, null=True, upload_to='additional_images/')),
                ('additional_image2', models.ImageField(blank=True, null=True, upload_to='additional_images/')),
                ('additional_image3', models.ImageField(blank=True, null=True, upload_to='additional_images/')),
                ('additional_image4', models.ImageField(blank=True, null=True, upload_to='additional_images/')),
                ('additional_image5', models.ImageField(blank=True, null=True, upload_to='additional_images/')),
                ('short_reel', models.FileField(blank=True, null=True, upload_to='short_reels/')),
            ],
        ),
        migrations.DeleteModel(
            name='PhoneOTP',
        ),
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.RemoveField(
            model_name='user',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='user',
            name='drinking',
        ),
        migrations.RemoveField(
            model_name='user',
            name='images',
        ),
        migrations.RemoveField(
            model_name='user',
            name='smoke',
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='designation',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='district',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='fullname',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='pincode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='qualification',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('single', 'single'), ('in relationship', 'in relationship'), ('married', 'married')], default='S', max_length=15),
        ),
        migrations.AddField(
            model_name='user',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='height',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='additionalinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usermedia',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='DOB',
            field=models.DateField(blank=True, default='1980-01-01', null=True),
        ),
    ]
