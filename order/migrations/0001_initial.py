# Generated by Django 3.0.4 on 2020-04-04 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servis_name', models.CharField(blank=True, db_index=True, max_length=70, verbose_name='Магазин')),
            ],
            options={
                'verbose_name': 'Магазин',
                'verbose_name_plural': 'Магазины',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(blank=True, db_index=True, max_length=70, verbose_name='Статус готовности')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_Type', models.CharField(blank=True, max_length=100, verbose_name='Тип модели')),
                ('firma', models.CharField(blank=True, max_length=50, verbose_name='Фирма')),
                ('model_devie', models.CharField(blank=True, db_index=True, max_length=50, verbose_name='Модель устройства')),
                ('Error_type', models.TextField(blank=True, verbose_name='Тип поломки')),
                ('Cost', models.CharField(max_length=7, verbose_name='Стоимость')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('komplekt', models.CharField(blank=True, max_length=200, verbose_name='Комплектация')),
                ('zametki_priemshika', models.CharField(blank=True, max_length=200, verbose_name='Заметки приёмщика')),
                ('predoplata', models.CharField(blank=True, max_length=13, verbose_name='Предопата')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Приёмщик')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.Customer', verbose_name='Клиент')),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shop', to='order.Shop', verbose_name='Магазин')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status', to='order.Status', verbose_name='Статус')),
            ],
        ),
    ]
