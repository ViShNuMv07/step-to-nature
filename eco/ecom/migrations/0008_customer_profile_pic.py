# Generated by Django 4.2.2 on 2023-07-13 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0007_remove_customer_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/CustomerProfilePic/'),
        ),
    ]
