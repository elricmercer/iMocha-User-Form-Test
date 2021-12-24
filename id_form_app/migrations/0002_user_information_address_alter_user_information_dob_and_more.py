# Generated by Django 4.0 on 2021-12-24 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('id_form_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_information',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_information',
            name='dob',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user_information',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user_information',
            name='postcode',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user_information',
            name='state',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
