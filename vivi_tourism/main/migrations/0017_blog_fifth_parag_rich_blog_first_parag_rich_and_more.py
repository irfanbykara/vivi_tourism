# Generated by Django 4.0 on 2024-02-19 19:00

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_remove_villa_multiple_image_delete_multipleimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='fifth_parag_rich',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='first_parag_rich',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='forth_parag_rich',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='second_parag_rich',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='third_parag_rich',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]