# Generated by Django 4.1.6 on 2023-03-23 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("breads", "0013_alter_country_countries"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="country",
            options={"verbose_name_plural": "Locais de Origem"},
        ),
        migrations.AddField(
            model_name="country",
            name="title",
            field=models.CharField(max_length=100, null=True),
        ),
    ]