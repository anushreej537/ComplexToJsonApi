# Generated by Django 5.1 on 2024-08-30 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=300)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
