# Generated by Django 4.2.3 on 2023-07-30 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
    ]
