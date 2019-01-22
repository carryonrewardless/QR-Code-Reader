# Generated by Django 2.1.5 on 2019-01-22 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('key', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scanner.Venue'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scanner.Event'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scanner.Member'),
        ),
    ]
