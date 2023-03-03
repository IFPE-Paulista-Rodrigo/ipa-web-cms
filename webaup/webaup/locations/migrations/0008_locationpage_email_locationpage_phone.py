# Generated by Django 4.1.6 on 2023-03-03 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("locations", "0007_alter_locationoperatinghours_day"),
    ]

    operations = [
        migrations.AddField(
            model_name="locationpage",
            name="email",
            field=models.TextField(blank=True, help_text="E-mail para contato"),
        ),
        migrations.AddField(
            model_name="locationpage",
            name="phone",
            field=models.TextField(
                blank=True,
                help_text="Número de telefone para contato, formato (xx)xxxxx-xxxx",
            ),
        ),
    ]
