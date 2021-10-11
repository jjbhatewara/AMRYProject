# Generated by Django 3.2.8 on 2021-10-11 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SatImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('Sat_Main_Img', models.ImageField(upload_to='images/')),
                ('action', models.CharField(choices=[('0', 'Roads'), ('1', 'Planes')], default=0, max_length=11)),
            ],
        ),
    ]
