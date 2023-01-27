# Generated by Django 4.1.5 on 2023-01-27 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=220)),
                ('cpf', models.IntegerField()),
                ('fone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('data_nascimento', models.DateField()),
                ('endereço', models.TextField()),
                ('data_cadastro', models.DateTimeField()),
                ('description', models.TextField()),
            ],
        ),
    ]
