# Generated by Django 4.2.1 on 2023-06-07 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopets', '0002_tutor_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='estado',
            field=models.CharField(default='MS', max_length=2),
        ),
    ]
