# Generated by Django 4.2.7 on 2023-11-16 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locais', '0004_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(to='locais.category'),
        ),
    ]
