# Generated by Django 3.0.3 on 2020-04-23 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_candidate_candidateid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='id',
        ),
        migrations.AlterField(
            model_name='candidate',
            name='candidateID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
