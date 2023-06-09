# Generated by Django 4.1.7 on 2023-03-21 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_choice_group_name_remove_choice_language_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='paradigms',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='language',
            name='group',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.group'),
        ),
    ]
