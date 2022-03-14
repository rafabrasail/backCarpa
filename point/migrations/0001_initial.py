# Generated by Django 4.0.3 on 2022-03-14 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0003_usercustom_remove_jointdenavit_robot_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PointDefault',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position_x', models.FloatField(default=0.0)),
                ('position_y', models.FloatField(default=0.0)),
                ('position_z', models.FloatField(default=0.0)),
                ('orientation_x', models.FloatField(default=0.0)),
                ('orientation_y', models.FloatField(default=0.0)),
                ('orientation_z', models.FloatField(default=0.0)),
                ('robot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.robotdefault')),
            ],
        ),
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
                ('robot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.robot')),
            ],
        ),
    ]
