# Generated by Django 5.1.1 on 2024-10-03 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_gymsync', '0004_rotina_rotinadia'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditarTreino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True)),
                ('exercicios', models.TextField()),
            ],
        ),
    ]
