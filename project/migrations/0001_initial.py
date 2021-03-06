# Generated by Django 3.0.8 on 2020-08-09 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.DateField()),
                ('calendar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Calendar')),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_title', models.CharField(help_text='Set the month title', max_length=20)),
                ('details', models.TextField(default='', help_text='Insert general month information', max_length=200)),
                ('bg_image', models.CharField(blank=True, max_length=40, null=True)),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Month')),
            ],
        ),
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos_x', models.IntegerField()),
                ('pos_y', models.IntegerField()),
                ('z_index', models.IntegerField()),
                ('rotation', models.IntegerField()),
                ('scale', models.FloatField(default=1)),
                ('icon_image', models.CharField(blank=True, max_length=40, null=True)),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Month')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(help_text='Set starting time')),
                ('end_time', models.DateTimeField(help_text='Set ending time')),
                ('title', models.CharField(default='Peilut', help_text='Set the activity title', max_length=20)),
                ('content', models.TextField(blank=True, default='', max_length=50)),
                ('age_group', models.CharField(default='ד', help_text='א/ב/ג/ד', max_length=5)),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Month')),
            ],
        ),
    ]
