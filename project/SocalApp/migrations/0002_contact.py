# Generated by Django 2.1 on 2018-09-02 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocalApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userAccount', models.CharField(max_length=20)),
                ('userContact', models.CharField(max_length=20)),
                ('latestTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
