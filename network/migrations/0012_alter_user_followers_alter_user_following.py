# Generated by Django 4.2 on 2023-06-06 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0011_alter_post_user_alter_user_followers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='followers',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='following',
            field=models.IntegerField(default=0),
        ),
    ]