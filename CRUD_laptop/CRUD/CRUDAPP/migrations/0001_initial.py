# Generated by Django 4.0.3 on 2022-03-22 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lid', models.IntegerField()),
                ('brand_name', models.CharField(max_length=40)),
                ('model_name', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
                ('rom', models.CharField(max_length=40)),
                ('ram', models.CharField(max_length=40)),
                ('SSD', models.CharField(max_length=40)),
                ('HDD', models.CharField(max_length=40)),
                ('Weight', models.FloatField()),
                ('year', models.IntegerField()),
            ],
        ),
    ]