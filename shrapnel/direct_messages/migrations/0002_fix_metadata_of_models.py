# Generated by Django 2.2.8 on 2019-12-22 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('direct_messages', '0001_create_direct_message_model'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='directmessage',
            options={'verbose_name': 'DirectMessage', 'verbose_name_plural': 'DirectMessages'},
        ),
    ]