# Generated by Django 4.1.4 on 2022-12-10 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=250, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
