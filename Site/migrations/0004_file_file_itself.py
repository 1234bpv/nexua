# Generated by Django 2.0.3 on 2018-04-01 13:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0003_auto_20180330_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file_itself',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]