# Generated by Django 3.2.3 on 2021-06-30 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cta', '0009_map'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]