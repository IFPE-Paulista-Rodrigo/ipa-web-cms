# Generated by Django 4.1.6 on 2023-02-28 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_blogpage_last_modified"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blogpage",
            name="last_modified",
        ),
    ]