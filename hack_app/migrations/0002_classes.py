# Generated by Django 5.1.2 on 2024-10-25 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hack_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.TextField()),
            ],
        ),
    ]