# Generated by Django 4.0 on 2024-02-06 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20230129_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='villa',
            name='is_popular',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='villa',
            name='extra',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.province')),
            ],
        ),
        migrations.AddField(
            model_name='villa',
            name='province',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.province'),
        ),
        migrations.AddField(
            model_name='villa',
            name='zone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.zone'),
        ),
    ]
