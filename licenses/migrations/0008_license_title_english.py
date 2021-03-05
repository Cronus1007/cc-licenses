# Generated by Django 2.2.13 on 2020-10-14 16:37

# Third-party
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("licenses", "0007_auto_20201005_1411"),
    ]

    operations = [
        migrations.AddField(
            model_name="license",
            name="title_english",
            field=models.TextField(
                blank=True,
                default="",
                help_text="License title in English, e.g."
                " 'Attribution-NonCommercial-NoDerivs 3.0 Unported'",
            ),
        ),
    ]
