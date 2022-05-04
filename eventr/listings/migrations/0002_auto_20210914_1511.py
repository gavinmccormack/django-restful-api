# Generated by Django 3.2.5 on 2021-09-14 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="foreign_id",
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name="eventinstance",
            name="event",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="eventinstances",
                to="listings.event",
            ),
        ),
    ]
