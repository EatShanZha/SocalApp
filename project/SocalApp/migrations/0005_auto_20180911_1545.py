# Generated by Django 2.1 on 2018-09-11 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocalApp', '0004_auto_20180908_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='head_img',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
