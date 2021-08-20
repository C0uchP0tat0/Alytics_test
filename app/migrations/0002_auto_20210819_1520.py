# Generated by Django 2.2.10 on 2021-08-19 12:20

from django.db import migrations, models
import django_matplotlib.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FunctionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('function', models.CharField(max_length=50, verbose_name='Функция')),
                ('interval', models.IntegerField(verbose_name='Интервал t,дней')),
                ('processing_date', models.DateTimeField(auto_now=True, verbose_name='Дата обработки')),
                ('image', models.ImageField(upload_to='')),
                ('function_plot', django_matplotlib.fields.MatplotlibFigureField()),
            ],
        ),
        migrations.DeleteModel(
            name='CompositeModel',
        ),
    ]