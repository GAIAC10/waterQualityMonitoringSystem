# Generated by Django 4.1 on 2023-02-21 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('TDS', models.CharField(default=None, max_length=50, null=True, verbose_name='固体溶解度')),
                ('PH', models.CharField(default=None, max_length=50, null=True, verbose_name='酸碱度')),
                ('TU', models.CharField(default=None, max_length=50, null=True, verbose_name='浊度')),
                ('TEM', models.CharField(default=None, max_length=50, null=True, verbose_name='温度')),
                ('LON', models.CharField(default=None, max_length=50, null=True, verbose_name='经度')),
                ('LAT', models.CharField(default=None, max_length=50, null=True, verbose_name='纬度')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'db_table': 'data_info',
            },
        ),
    ]