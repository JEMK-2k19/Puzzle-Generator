# Generated by Django 2.1.5 on 2019-01-20 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpark', '0004_currentround_question_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentround',
            name='link1',
            field=models.CharField(default='asdas', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='currentround',
            name='link2',
            field=models.CharField(default='asdaf', max_length=1000),
            preserve_default=False,
        ),
    ]