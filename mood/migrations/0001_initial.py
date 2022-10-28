# Generated by Django 4.0.5 on 2022-10-28 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MoodFactors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factor', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SleepTimeField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('hour', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='FactorDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('factor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mood.moodfactors')),
            ],
        ),
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('mood', models.CharField(max_length=255)),
                ('place', models.CharField(max_length=255)),
                ('weather', models.CharField(max_length=255)),
                ('text', models.TextField(blank=True, null=True)),
                ('people', models.ManyToManyField(to='mood.factordetail')),
            ],
        ),
    ]
