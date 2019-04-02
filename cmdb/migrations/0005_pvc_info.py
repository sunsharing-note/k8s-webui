# Generated by Django 2.1.7 on 2019-03-19 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0004_namespace_info_pvs_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='pvc_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('namespace', models.CharField(max_length=64)),
                ('access_mode', models.CharField(max_length=64)),
                ('capacity', models.CharField(max_length=64)),
                ('phase', models.CharField(max_length=64)),
                ('storage_class_name', models.CharField(max_length=64)),
            ],
        ),
    ]