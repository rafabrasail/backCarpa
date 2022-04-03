# Generated by Django 4.0.3 on 2022-03-25 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Joint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('T', 'translation'), ('R', 'rotation')], default='R', max_length=1)),
                ('screw_s_x', models.FloatField(default=0.0)),
                ('screw_s_y', models.FloatField(default=0.0)),
                ('screw_s_z', models.FloatField(default=0.0)),
                ('screw_s0_x', models.FloatField(default=0.0)),
                ('screw_s0_y', models.FloatField(default=0.0)),
                ('screw_s0_z', models.FloatField(default=0.0)),
                ('screw_t', models.FloatField(default=0.0)),
                ('screw_theta', models.FloatField(default=0.0)),
                ('denavit_alpha', models.FloatField(default=0.0)),
                ('denavit_a', models.FloatField(default=0.0)),
                ('denavit_d', models.FloatField(default=0.0)),
                ('denavit_theta', models.FloatField(default=0.0)),
                ('file', models.FileField(blank=True, null=True, upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Joint_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('T', 'translation'), ('R', 'rotation')], default='R', max_length=1)),
                ('screw_s_x', models.FloatField(default=0.0)),
                ('screw_s_y', models.FloatField(default=0.0)),
                ('screw_s_z', models.FloatField(default=0.0)),
                ('screw_s0_x', models.FloatField(default=0.0)),
                ('screw_s0_y', models.FloatField(default=0.0)),
                ('screw_s0_z', models.FloatField(default=0.0)),
                ('screw_t', models.FloatField(default=0.0)),
                ('screw_theta', models.FloatField(default=0.0)),
                ('denavit_alpha', models.FloatField(default=0.0)),
                ('denavit_a', models.FloatField(default=0.0)),
                ('denavit_d', models.FloatField(default=0.0)),
                ('denavit_theta', models.FloatField(default=0.0)),
                ('file', models.FileField(blank=True, null=True, upload_to='media')),
            ],
        ),
    ]
