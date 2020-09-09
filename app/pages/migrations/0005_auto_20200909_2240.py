# Generated by Django 3.1.1 on 2020-09-09 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20200908_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dessert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Назва страви')),
                ('price', models.IntegerField(verbose_name='Ціна страви')),
                ('description', models.TextField(max_length=250, verbose_name='Опис страви')),
                ('image', models.ImageField(upload_to='Dessert/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Назва страви')),
                ('price', models.IntegerField(verbose_name='Ціна страви')),
                ('description', models.TextField(max_length=250, verbose_name='Опис страви')),
                ('image', models.ImageField(upload_to='Pizza/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Sushi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Назва страви')),
                ('price', models.IntegerField(verbose_name='Ціна страви')),
                ('description', models.TextField(max_length=250, verbose_name='Опис страви')),
                ('image', models.ImageField(upload_to='Sushi/%Y/%m/%d/')),
            ],
        ),
        migrations.DeleteModel(
            name='Food',
        ),
    ]
