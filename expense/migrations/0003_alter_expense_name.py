# Generated by Django 4.2.7 on 2023-11-08 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0002_alter_expensetransaction_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Expense Name'),
        ),
    ]
