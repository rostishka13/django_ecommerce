# Generated by Django 3.1.4 on 2020-12-12 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
