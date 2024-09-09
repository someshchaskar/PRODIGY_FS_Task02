# Generated by Django 5.1.1 on 2024-09-08 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Empid', models.IntegerField()),
                ('Name', models.CharField(max_length=60)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('Email', models.CharField(max_length=75)),
                ('Address', models.CharField(max_length=150)),
                ('Contact', models.IntegerField()),
                ('Department', models.CharField(max_length=80)),
                ('Salary', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
