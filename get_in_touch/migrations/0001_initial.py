# Generated by Django 2.2.2 on 2022-08-23 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('surname', models.CharField(default='Some String', max_length=255)),
                ('phone', models.CharField(default='', max_length=15)),
                ('mobile', models.CharField(default='', max_length=15)),
                ('email', models.EmailField(default='', max_length=254)),
                ('subject', models.TextField(max_length=150)),
                ('massage', models.TextField(max_length=150)),
                ('company', models.CharField(default='Some String', max_length=255)),
                ('role', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
