# Generated by Django 2.0 on 2018-01-16 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_usercontact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
