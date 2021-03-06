# Generated by Django 4.0.3 on 2022-03-25 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position_x', models.FloatField(default=0.0)),
                ('position_y', models.FloatField(default=0.0)),
                ('position_z', models.FloatField(default=0.0)),
                ('orientation_x', models.FloatField(default=0.0)),
                ('orientation_y', models.FloatField(default=0.0)),
                ('orientation_z', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='PointUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position_x', models.FloatField(default=0.0)),
                ('position_y', models.FloatField(default=0.0)),
                ('position_z', models.FloatField(default=0.0)),
                ('orientation_x', models.FloatField(default=0.0)),
                ('orientation_y', models.FloatField(default=0.0)),
                ('orientation_z', models.FloatField(default=0.0)),
            ],
        ),
    ]
