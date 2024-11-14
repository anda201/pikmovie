# Generated by Django 4.2.16 on 2024-11-14 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=100)),
                ('pubDate', models.DateField()),
                ('author', models.TextField(max_length=100)),
                ('bestDuration', models.TextField(max_length=50)),
            ],
        ),
    ]
