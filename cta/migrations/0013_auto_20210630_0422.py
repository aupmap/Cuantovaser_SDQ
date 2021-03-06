# Generated by Django 3.2.3 on 2021-06-30 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cta', '0012_alter_form_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuantovaser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('edad', models.CharField(max_length=30)),
                ('interpretacion', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('urgente', models.CharField(choices=[('yes', 'Sí'), ('no', 'No')], max_length=3)),
                ('nombre_2', models.CharField(max_length=30)),
                ('apellido_2', models.CharField(max_length=30)),
                ('celular', models.CharField(max_length=11)),
            ],
        ),
        migrations.DeleteModel(
            name='Map',
        ),
    ]
