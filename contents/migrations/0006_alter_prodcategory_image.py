# Generated by Django 4.1 on 2023-06-16 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0005_alter_prodcategory_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prodcategory',
            name='image',
            field=models.ImageField(null=True, upload_to='static/images/'),
        ),
    ]
