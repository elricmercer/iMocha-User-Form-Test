# Generated by Django 4.0 on 2021-12-24 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_Information',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('dob', models.CharField(max_length=200)),
                ('postcode', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
            ],
        ),
    ]
