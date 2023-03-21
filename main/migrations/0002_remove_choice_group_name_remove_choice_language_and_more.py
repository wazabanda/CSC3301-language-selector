# Generated by Django 4.1.7 on 2023-03-21 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='group_name',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='language',
        ),
        migrations.AddField(
            model_name='language',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.group'),
        ),
        migrations.AddField(
            model_name='language',
            name='taken',
            field=models.BooleanField(default=False),
        ),
    ]