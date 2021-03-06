# Generated by Django 2.1.7 on 2020-02-08 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0016_auto_20200127_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remote_key', models.CharField(max_length=20, unique=True)),
                ('street_address', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LocBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remote_key', models.CharField(max_length=20, unique=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scanner.Address')),
            ],
        ),
    ]
