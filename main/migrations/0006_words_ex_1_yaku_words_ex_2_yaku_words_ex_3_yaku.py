# Generated by Django 5.0.1 on 2024-01-26 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_words_ex_1_words_ex_2_words_ex_3'),
    ]

    operations = [
        migrations.AddField(
            model_name='words',
            name='ex_1_yaku',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='words',
            name='ex_2_yaku',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='words',
            name='ex_3_yaku',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
