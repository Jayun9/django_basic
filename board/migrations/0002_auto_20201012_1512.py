# Generated by Django 3.1.2 on 2020-10-12 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='title',
            field=models.CharField(max_length=128, verbose_name='제목'),
        ),
    ]