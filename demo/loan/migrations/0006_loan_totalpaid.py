# Generated by Django 4.1.7 on 2023-05-03 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0005_remove_loan_guaranter_id_loan_guaranter_card_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='TotalPaid',
            field=models.FloatField(default=0.08333333333333333),
            preserve_default=False,
        ),
    ]
