# Generated by Django 2.0.6 on 2018-06-13 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_usermessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermessage',
            name='id',
        ),
        migrations.AddField(
            model_name='usermessage',
            name='object_id',
            field=models.CharField(default='', max_length=50, primary_key=True, serialize=False),
        ),
    ]
