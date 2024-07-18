# Generated by Django 5.0.6 on 2024-07-16 18:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contents", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="document",
            field=models.FileField(blank=True, null=True, upload_to="documents/"),
        ),
        migrations.AddField(
            model_name="article",
            name="link",
            field=models.URLField(blank=True),
        ),
    ]