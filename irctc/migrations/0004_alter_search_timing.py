# Generated by Django 3.2.5 on 2021-12-02 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irctc', '0003_search'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='timing',
            field=models.CharField(max_length=20),
        ),
    ]
