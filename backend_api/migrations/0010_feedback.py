# Generated by Django 3.2.19 on 2023-06-14 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0009_alter_judgement_i_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('f_id', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=255)),
            ],
        ),
    ]
