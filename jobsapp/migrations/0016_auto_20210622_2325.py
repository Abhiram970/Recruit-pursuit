# Generated by Django 3.1.2 on 2021-06-22 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0015_colors'),
    ]

    operations = [
        migrations.CreateModel(
            name='skillset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_qualifications', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'skillset',
            },
        ),
        migrations.DeleteModel(
            name='colors',
        ),
    ]
