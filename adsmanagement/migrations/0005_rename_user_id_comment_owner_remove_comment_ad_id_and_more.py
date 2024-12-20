# Generated by Django 5.1.3 on 2024-12-02 14:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsmanagement', '0004_rename_user_id_ad_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user_id',
            new_name='owner',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='ad_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='ad',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='adsmanagement.ad'),
        ),
    ]
