# Generated by Django 5.0.1 on 2024-01-26 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_words_yaku'),
    ]

    operations = [
        migrations.AddField(
            model_name='words',
            name='ex_1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='words',
            name='ex_2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='words',
            name='ex_3',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
