# Generated by Django 4.1.2 on 2022-10-20 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_project_options_project_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='Dirección Web'),
        ),
    ]
