# Generated by Django 2.2 on 2019-04-14 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190414_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='LanguageCodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=250)),
                ('language_code', models.CharField(max_length=3)),
            ],
        ),
    ]
