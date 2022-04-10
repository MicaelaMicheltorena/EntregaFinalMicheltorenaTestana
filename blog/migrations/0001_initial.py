# Generated by Django 4.0.3 on 2022-04-10 13:55

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('subtitulo', models.CharField(max_length=50)),
                ('cuerpo', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('autor', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
            ],
        ),
    ]