# Generated by Django 4.2.1 on 2023-06-05 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('idade', models.CharField(max_length=10)),
                ('porte', models.CharField(choices=[('P', 'Porte pequeno'), ('P/M', 'Porte pequeno/médio'), ('M', 'Porte médio'), ('M/G', 'Porte médio/grande'), ('G', 'Porte grande')], max_length=20)),
                ('caracteristicas', models.CharField(max_length=30)),
                ('cidade', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=11)),
                ('cidade', models.CharField(max_length=20)),
                ('sobre', models.TextField()),
            ],
        ),
    ]
