# Generated by Django 3.2.4 on 2021-06-06 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='neighborhood_id',
            new_name='neighborhood',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='neighborhood_id',
            new_name='neighborhood',
        ),
        migrations.AddField(
            model_name='imagepost',
            name='neighbourhood',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.neighbourhood'),
        ),
        migrations.AddField(
            model_name='textpost',
            name='neighbourhood',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.neighbourhood'),
        ),
    ]
