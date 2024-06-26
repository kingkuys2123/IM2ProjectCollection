# Generated by Django 5.0.2 on 2024-05-16 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WarehouseItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('Quantity', models.IntegerField()),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
