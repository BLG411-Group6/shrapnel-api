# Generated by Django 2.2.8 on 2019-12-22 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_create_user_model'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]
