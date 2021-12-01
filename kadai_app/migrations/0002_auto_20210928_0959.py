# Generated by Django 2.2.2 on 2021-09-28 09:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kadai_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='play',
            name='attach1',
            field=models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(['mp3'])], verbose_name='添付ファイル'),
        ),
        migrations.AlterField(
            model_name='play',
            name='attach2',
            field=models.FileField(default='ww', upload_to='', validators=[django.core.validators.FileExtensionValidator(['mp3'])], verbose_name='添付ファイル'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='play',
            name='attach3',
            field=models.FileField(default='ww', upload_to='', validators=[django.core.validators.FileExtensionValidator(['mp3'])], verbose_name='添付ファイル'),
            preserve_default=False,
        ),
    ]
