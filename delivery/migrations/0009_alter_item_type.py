# Generated by Django 5.0.1 on 2024-02-16 07:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("delivery", "0008_alter_item_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="type",
            field=models.CharField(
                choices=[
                    ("perishable", "Perishable"),
                    ("non-perishable", "Non-Perishable"),
                ],
                max_length=20,
            ),
        ),
    ]
