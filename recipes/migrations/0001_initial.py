# Generated by Django 4.2.9 on 2024-01-24 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('cooking_time', models.IntegerField(default=0, help_text='in minutes')),
                ('ingredients', models.CharField(max_length=500)),
                ('difficulty', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
    ]
