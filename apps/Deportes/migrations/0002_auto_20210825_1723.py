# Generated by Django 2.0.6 on 2021-08-25 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Deportes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='garment',
            fields=[
                ('pk_id_garment', models.AutoField(primary_key=True, serialize=False)),
                ('mark', models.CharField(max_length=50)),
                ('size', models.DateField(auto_now_add=True)),
                ('shop', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=3)),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='mark',
            fields=[
                ('pk_id_mark', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='fk_product',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='fk_product',
        ),
        migrations.DeleteModel(
            name='invoice',
        ),
        migrations.DeleteModel(
            name='product',
        ),
        migrations.DeleteModel(
            name='stock',
        ),
    ]
