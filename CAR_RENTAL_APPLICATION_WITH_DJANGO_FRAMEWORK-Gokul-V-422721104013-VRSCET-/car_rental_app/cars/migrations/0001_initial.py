# Generated by Django 3.0.7 on 2024-04-11 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('model', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('availability', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='car_images/')),
                ('car_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]