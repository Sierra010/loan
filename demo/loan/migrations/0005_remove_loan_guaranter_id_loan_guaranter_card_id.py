# Generated by Django 4.1.7 on 2023-05-03 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0004_alter_customer_card_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='Guaranter_id',
        ),
        migrations.AddField(
            model_name='loan',
            name='Guaranter_card_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
