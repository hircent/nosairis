# Generated by Django 4.1.1 on 2022-09-11 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Terminals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('switch', models.CharField(max_length=20)),
                ('t1', models.IntegerField()),
                ('t2', models.IntegerField()),
                ('t3', models.IntegerField()),
                ('t4', models.IntegerField()),
                ('t5', models.IntegerField()),
                ('ts', models.IntegerField()),
            ],
        ),
    ]
