# Generated by Django 4.2.1 on 2023-06-27 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
