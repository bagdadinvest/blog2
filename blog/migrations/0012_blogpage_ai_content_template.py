# Generated by Django 3.2.25 on 2024-09-22 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_aicontenttemplate'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='ai_content_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='blog.aicontenttemplate'),
        ),
    ]