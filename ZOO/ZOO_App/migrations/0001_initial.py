# Generated by Django 4.1.7 on 2023-05-08 16:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bilhete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intervalo_idade', models.CharField(choices=[('B', 'Bebé'), ('C', 'Criança'), ('A', 'Adulto'), ('S', 'Sénior')], max_length=1)),
                ('preco', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_especie', models.CharField(max_length=50)),
                ('classe', models.CharField(choices=[('MAM', 'Mamífero'), ('REP', 'Réptil'), ('INS', 'Inseto'), ('ANF', 'Anfíbio'), ('ARA', 'Aracnídeo')], max_length=3)),
                ('alimentacao', models.CharField(choices=[('C', 'Carnívoro'), ('O', 'Omnívoro'), ('H', 'Herbívoro')], max_length=1)),
                ('regiao', models.CharField(choices=[('1', 'Europa'), ('2', 'América do Norte'), ('3', 'América do Sul'), ('4', 'África'), ('5', 'Ártico'), ('6', 'Antártida'), ('7', 'Austrália'), ('8', 'Ásia'), ('9', 'Oceano Pacífico'), ('10', 'Oceano Atlântico'), ('11', 'Oceano Ártico'), ('12', 'Oceano Antártico'), ('13', 'Oceano Índico')], max_length=2)),
                ('quantidade', models.IntegerField()),
                ('peso', models.CharField(max_length=30)),
                ('comprimento', models.CharField(max_length=30)),
                ('altura', models.CharField(max_length=30)),
                ('atividade', models.CharField(choices=[('N', 'Noturno'), ('D', 'Diurno'), ('C', 'Crepuscular')], max_length=1)),
                ('vida_social', models.CharField(choices=[('C', 'Casal'), ('S', 'Solitário'), ('B', 'Bando')], max_length=1)),
                ('reproducao', models.CharField(choices=[('O', 'Ovípara'), ('V', 'Vívipara')], max_length=1)),
                ('ameacada', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Fatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('preco_total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.FileField(null=True, upload_to='noticias')),
                ('descricao', models.CharField(max_length=200)),
                ('titulo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designacao', models.CharField(max_length=50)),
                ('preco', models.IntegerField()),
                ('categoria', models.CharField(choices=[('R', 'Roupa'), ('U', 'Utensílios'), ('P', 'Peluches')], max_length=1)),
                ('imagem', models.FileField(null=True, upload_to='produtos')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Utilizador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_nascimento', models.DateField()),
                ('morada', models.CharField(max_length=100)),
                ('numero_contribuinte', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UtilizadorNoticia_pk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noticia', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ZOO_App.noticia')),
                ('utilizador', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ZOO_App.utilizador')),
            ],
            options={
                'unique_together': {('utilizador', 'noticia')},
            },
        ),
        migrations.CreateModel(
            name='utilizadorNoticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('utilizadornoticia_pk', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='ZOO_App.utilizadornoticia_pk')),
            ],
        ),
        migrations.CreateModel(
            name='ProdutoCarinhoCompras_pk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ZOO_App.produto')),
                ('utilizador', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ZOO_App.utilizador')),
            ],
            options={
                'unique_together': {('produto', 'utilizador')},
            },
        ),
        migrations.CreateModel(
            name='ProdutoCarinhoCompras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('produtocarinhocompras_pk', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='ZOO_App.produtocarinhocompras_pk')),
            ],
        ),
        migrations.CreateModel(
            name='FaturaProduto_pk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fatura', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ZOO_App.fatura')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ZOO_App.produto')),
            ],
            options={
                'unique_together': {('fatura', 'produto')},
            },
        ),
        migrations.CreateModel(
            name='FaturaProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('faturaproduto_pk', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='ZOO_App.faturaproduto_pk')),
            ],
        ),
        migrations.AddField(
            model_name='fatura',
            name='utilizador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ZOO_App.utilizador'),
        ),
        migrations.CreateModel(
            name='Donativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('data', models.DateField()),
                ('utilizador', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ZOO_App.utilizador')),
            ],
        ),
        migrations.CreateModel(
            name='BilheteUtilizador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_compra', models.DateTimeField(default=datetime.datetime.now)),
                ('data_bilhete', models.DateField()),
                ('quantidade', models.IntegerField()),
                ('bilhete', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ZOO_App.bilhete')),
                ('utilizador', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NoticiaTag_pk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noticia', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ZOO_App.noticia')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ZOO_App.tag')),
            ],
            options={
                'unique_together': {('noticia', 'tag')},
            },
        ),
    ]