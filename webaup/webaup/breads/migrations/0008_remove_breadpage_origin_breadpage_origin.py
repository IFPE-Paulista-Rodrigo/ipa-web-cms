# Generated by Django 4.1.6 on 2023-03-21 22:54

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ("breads", "0007_alter_country_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="breadpage",
            name="origin",
        ),
        migrations.AddField(
            model_name="breadpage",
            name="origin",
            field=modelcluster.fields.ParentalManyToManyField(
                blank=True, to="breads.country"
            ),
        ),
    ]