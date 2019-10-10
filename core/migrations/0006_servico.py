# Generated by Django 2.2.5 on 2019-10-04 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_produto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('status', models.BooleanField()),
                ('valor_venda', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
