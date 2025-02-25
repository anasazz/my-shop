# Generated by Django 4.2.7 on 2023-11-08 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_alter_sale_client_alter_sale_date_alter_sale_notes_and_more'),
        ('purchase', '0002_productinoutdbview'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchase',
            options={'verbose_name': 'Purchase', 'verbose_name_plural': 'Purchases'},
        ),
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.DateTimeField(verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.product', verbose_name='Product'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='quantity',
            field=models.IntegerField(verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='value',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=9, verbose_name='Value'),
        ),
    ]
