# Generated by Django 4.1.2 on 2022-10-11 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('first_name', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('middle_name', models.CharField(blank=True, max_length=26)),
                ('date_of_graduation', models.DateField(null=True)),
                ('date_of_employment', models.DateField(null=True)),
                ('position', models.CharField(blank=True, max_length=20)),
                ('salary', models.IntegerField(default=True)),
                ('supervisors', models.CharField(blank=True, max_length=26)),
            ],
        ),
    ]
