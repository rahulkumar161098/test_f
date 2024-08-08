# Generated by Django 3.1 on 2022-05-02 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('discount', models.FloatField()),
                ('duration', models.FloatField()),
                ('authodName', models.CharField(max_length=30)),
            ],
        ),
    ]
