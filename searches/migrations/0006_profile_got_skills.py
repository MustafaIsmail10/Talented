# Generated by Django 4.1.1 on 2022-09-27 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("searches", "0005_rename_article_comment_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="got_skills",
            field=models.BooleanField(default=False),
        ),
    ]
