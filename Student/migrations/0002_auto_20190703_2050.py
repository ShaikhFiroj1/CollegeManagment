# Generated by Django 2.2.3 on 2019-07-03 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentlist',
            name='semester',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='studentlist',
            name='test1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='studentlist',
            name='test2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
