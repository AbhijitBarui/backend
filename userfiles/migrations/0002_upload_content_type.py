# Generated by Django 4.0.5 on 2022-06-14 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userfiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='content_type',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
