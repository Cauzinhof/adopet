# Generated by Django 4.2.1 on 2023-06-28 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopets', '0002_alter_baseuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='foto',
            field=models.ImageField(blank=True, default='', upload_to='fotos/pets/'),
        ),
    ]