# Generated by Django 4.0 on 2022-03-05 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ufeed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
    ]
