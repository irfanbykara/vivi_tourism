# Generated by Django 4.0 on 2024-02-15 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_villa_explanation_rich'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='')),
                ('associated_villa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='multiple_images', to='main.villa')),
            ],
        ),
        migrations.AddField(
            model_name='villa',
            name='multiple_image',
            field=models.ManyToManyField(related_name='villas', to='main.MultipleImages'),
        ),
    ]