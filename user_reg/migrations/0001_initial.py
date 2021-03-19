# Generated by Django 3.1.6 on 2021-02-21 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('Username', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=2, null=True)),
                ('gender', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]