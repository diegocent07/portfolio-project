# Generated by Django 2.1.5 on 2020-02-19 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pubdate',
            field=models.DateTimeField(),
        ),
    ]