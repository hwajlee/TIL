# Generated by Django 3.2.16 on 2023-01-17 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0002_alter_feed_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='like_people',
            field=models.ManyToManyField(related_name='like_feeds', to='facebook.Person'),
        ),
    ]
