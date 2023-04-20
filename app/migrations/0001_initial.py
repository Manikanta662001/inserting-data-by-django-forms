# Generated by Django 4.1.7 on 2023-04-20 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=20)),
                ('course', models.CharField(max_length=100)),
            ],
        ),
    ]
