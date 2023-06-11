# Generated by Django 4.2.1 on 2023-06-11 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adopets', '0003_tutor_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abrigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('cidade', models.CharField(max_length=20)),
                ('estado', models.CharField(default='MS', max_length=2)),
            ],
        ),
        migrations.AlterField(
            model_name='tutor',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='telefone',
            field=models.CharField(max_length=14),
        ),
        migrations.AddField(
            model_name='pet',
            name='abrigo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adopets.abrigo'),
        ),
    ]
