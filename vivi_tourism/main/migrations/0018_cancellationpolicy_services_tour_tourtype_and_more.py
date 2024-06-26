# Generated by Django 4.0 on 2024-04-23 17:03

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_blog_fifth_parag_rich_blog_first_parag_rich_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CancellationPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('explanation', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('explanation', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('explanation', ckeditor.fields.RichTextField(null=True)),
                ('default_price', models.IntegerField(default=1000, null=True)),
                ('avatar', models.ImageField(upload_to='')),
                ('address', models.CharField(max_length=300, null=True)),
                ('tour_duration', models.CharField(max_length=20, null=True)),
                ('has_guide', models.BooleanField(default=False, null=True)),
                ('has_wifi', models.BooleanField(default=False, null=True)),
                ('has_lunch', models.BooleanField(default=False, null=True)),
                ('has_shuttle', models.BooleanField(default=False, null=True)),
                ('currency', models.CharField(blank=True, default='try', max_length=3, null=True)),
                ('province', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.province')),
            ],
        ),
        migrations.CreateModel(
            name='TourType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VillaFeatureCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Yatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('explanation', ckeditor.fields.RichTextField(null=True)),
                ('default_price', models.IntegerField(default=1000, null=True)),
                ('avatar', models.ImageField(upload_to='')),
                ('num_bathroom', models.IntegerField()),
                ('brand', models.CharField(blank=True, max_length=30, null=True)),
                ('model', models.CharField(blank=True, max_length=30, null=True)),
                ('made_year', models.CharField(blank=True, max_length=4, null=True)),
                ('renovation_year', models.CharField(blank=True, max_length=4, null=True)),
                ('cruising_capacity', models.IntegerField(blank=True, null=True)),
                ('capacity', models.IntegerField(blank=True, null=True)),
                ('num_rooms', models.IntegerField(blank=True, null=True)),
                ('boarding_passanger_capacity', models.IntegerField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('cenova', models.CharField(blank=True, max_length=30, null=True)),
                ('main_sail', models.CharField(blank=True, max_length=30, null=True)),
                ('num_engine', models.IntegerField(blank=True, null=True)),
                ('engine_type', models.CharField(blank=True, max_length=30, null=True)),
                ('fuel_cost', models.CharField(blank=True, max_length=30, null=True)),
                ('fuel_type', models.CharField(blank=True, max_length=30, null=True)),
                ('yatch_material', models.CharField(blank=True, max_length=30, null=True)),
                ('num_rudder', models.IntegerField(blank=True, null=True)),
                ('daily_cruise_duration', models.CharField(blank=True, max_length=30, null=True)),
                ('daily_ac_duration', models.CharField(blank=True, max_length=30, null=True)),
                ('engine_horse_power', models.CharField(blank=True, max_length=30, null=True)),
                ('fuel_capacity', models.CharField(blank=True, max_length=30, null=True)),
                ('waste_tank_capacity', models.CharField(blank=True, max_length=30, null=True)),
                ('water_tank_capacity', models.CharField(blank=True, max_length=30, null=True)),
                ('hall_height', models.CharField(blank=True, max_length=30, null=True)),
                ('width', models.CharField(blank=True, max_length=30, null=True)),
                ('water_draft', models.CharField(blank=True, max_length=30, null=True)),
                ('currency', models.CharField(blank=True, default='try', max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='YatchFeatureCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='YatchPort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='YatchType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='priceinterval',
            name='min_nights',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='villa',
            name='currency',
            field=models.CharField(blank=True, default='try', max_length=3, null=True),
        ),
        migrations.CreateModel(
            name='YatchReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('total_price', models.IntegerField()),
                ('name', models.CharField(default='', max_length=70)),
                ('last_name', models.CharField(default='', max_length=70)),
                ('address', models.CharField(default='', max_length=150)),
                ('email', models.EmailField(default='', max_length=254)),
                ('phone', models.CharField(default='', max_length=20)),
                ('country', models.CharField(default='', max_length=20)),
                ('city', models.CharField(default='', max_length=20)),
                ('zip_code', models.CharField(default='', max_length=6)),
                ('completed', models.BooleanField(default=False)),
                ('yatch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.yatch')),
            ],
        ),
        migrations.CreateModel(
            name='YatchPriceInterval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('price', models.IntegerField()),
                ('min_nights', models.IntegerField(null=True)),
                ('yatch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.yatch')),
            ],
        ),
        migrations.CreateModel(
            name='YatchImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='')),
                ('yatch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.yatch')),
            ],
        ),
        migrations.CreateModel(
            name='YatchFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('yatch_feature_categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.yatchfeaturecategories')),
            ],
        ),
        migrations.AddField(
            model_name='yatch',
            name='features',
            field=models.ManyToManyField(blank=True, to='main.YatchFeature'),
        ),
        migrations.AddField(
            model_name='yatch',
            name='province',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.province'),
        ),
        migrations.AddField(
            model_name='yatch',
            name='services',
            field=models.ManyToManyField(blank=True, to='main.Services'),
        ),
        migrations.AddField(
            model_name='yatch',
            name='type',
            field=models.ManyToManyField(blank=True, to='main.YatchType'),
        ),
        migrations.AddField(
            model_name='yatch',
            name='yatch_port',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.yatchport'),
        ),
        migrations.AddField(
            model_name='yatch',
            name='zone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.zone'),
        ),
        migrations.CreateModel(
            name='VillaFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('is_internal', models.BooleanField(default=False, null=True)),
                ('villa_feature_categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.villafeaturecategories')),
            ],
        ),
        migrations.CreateModel(
            name='TourPriceInterval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('price', models.IntegerField()),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tour')),
            ],
        ),
        migrations.CreateModel(
            name='TourImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tour')),
            ],
        ),
        migrations.AddField(
            model_name='tour',
            name='type',
            field=models.ManyToManyField(to='main.TourType'),
        ),
        migrations.AddField(
            model_name='tour',
            name='zone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.zone'),
        ),
        migrations.AddField(
            model_name='villa',
            name='cancellation_policy',
            field=models.ManyToManyField(blank=True, to='main.CancellationPolicy'),
        ),
        migrations.AddField(
            model_name='villa',
            name='features',
            field=models.ManyToManyField(blank=True, to='main.VillaFeature'),
        ),
    ]
