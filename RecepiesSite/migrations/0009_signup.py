# Generated by Django 3.1.3 on 2020-11-15 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecepiesSite', '0008_auto_20201111_2356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]