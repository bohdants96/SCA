# Generated by Django 5.1.3 on 2024-11-15 19:03

import SpyCat.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpyCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Years_of_Experience', models.IntegerField(validators=[SpyCat.validators.validate_int])),
                ('Breed', models.CharField(max_length=50, validators=[SpyCat.validators.validate_breed])),
                ('Salary', models.IntegerField(validators=[SpyCat.validators.validate_int])),
            ],
            options={
                'verbose_name': 'SpyCat',
                'verbose_name_plural': 'SpyCats',
                'ordering': ['Salary'],
            },
        ),
    ]
