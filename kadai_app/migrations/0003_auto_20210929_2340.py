# Generated by Django 2.2.2 on 2021-09-29 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadai_app', '0002_auto_20210928_0959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='play',
            name='attach2',
        ),
        migrations.RemoveField(
            model_name='play',
            name='attach3',
        ),
    ]
