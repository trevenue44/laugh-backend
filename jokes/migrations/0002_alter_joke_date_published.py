# Generated by Django 4.2 on 2023-04-26 22:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("jokes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="joke",
            name="date_published",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
