# Generated by Django 3.0.7 on 2020-06-25 03:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=6)),
                ('choice', models.CharField(choices=[('BO', 'BOAST'), ('RO', 'ROAST')], default='BO', max_length=2)),
                ('body', models.TextField(max_length=280)),
                ('up_votes', models.IntegerField(default=0)),
                ('down_votes', models.IntegerField(default=0)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]