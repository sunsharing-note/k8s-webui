# Generated by Django 2.1.7 on 2019-03-15 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0002_pods_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pods_info',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]