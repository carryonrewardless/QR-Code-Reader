# Generated by Django 2.1.5 on 2019-01-22 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('postal_code', models.CharField(max_length=20)),
                ('membership_num', models.CharField(max_length=20)),
                ('end_date', models.DateTimeField(verbose_name='membership end')),
                ('status_id', models.IntegerField()),
            ],
        ),
    ]
