# Generated by Django 3.2.25 on 2024-09-21 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_auto_20180619_1705'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={},
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='body',
            new_name='main_description',
        ),
        migrations.AddField(
            model_name='homepage',
            name='background_video',
            field=models.URLField(blank=True, null=True),
        ),
    ]