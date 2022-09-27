# Generated by Django 4.1.1 on 2022-09-27 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("searches", "0003_remove_profile_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="starrted",
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("comment", models.CharField(max_length=300)),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="searches.profile",
                    ),
                ),
            ],
        ),
    ]