# Generated by Django 3.1.1 on 2020-09-12 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200912_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='total_comments',
            field=models.IntegerField(default=0),
        ),
    ]
