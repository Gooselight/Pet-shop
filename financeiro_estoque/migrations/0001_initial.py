# Generated by Django 2.2.5 on 2019-11-06 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimentacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_final', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('movimentacao_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='financeiro_estoque.Movimentacao')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Fornecedor')),
            ],
            bases=('financeiro_estoque.movimentacao',),
        ),
        migrations.CreateModel(
            name='FluxoDeCaixa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora_abertura', models.DateTimeField()),
                ('data_hora_fechamento', models.DateTimeField(null=True)),
                ('valor_abertura', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('valor_fechamento', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('valor_final', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('movimentacoes', models.ManyToManyField(to='financeiro_estoque.Movimentacao')),
            ],
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('data_entrada', models.DateField()),
                ('data_saida', models.DateField(blank=True, null=True)),
                ('data_validade', models.DateField()),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Produto')),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('movimentacao_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='financeiro_estoque.Movimentacao')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cliente')),
            ],
            bases=('financeiro_estoque.movimentacao',),
        ),
        migrations.CreateModel(
            name='ItemDeVenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=5)),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('produto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Produto')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro_estoque.Venda')),
            ],
        ),
        migrations.CreateModel(
            name='ItemDeCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('produto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Produto')),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro_estoque.Compra')),
            ],
        ),
    ]
