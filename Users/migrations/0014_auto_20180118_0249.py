# Generated by Django 2.0 on 2018-01-18 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0013_auto_20180118_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlanguage',
            name='user_skill1',
            field=models.CharField(blank=True, choices=[('B', 'Beginning'), ('P', 'Proficient'), ('M', 'Mother Tougne'), ('I', 'Influent'), ('L', 'Limilted')], max_length=1),
        ),
        migrations.AlterField(
            model_name='userlanguage',
            name='user_skill2',
            field=models.CharField(blank=True, choices=[('B', 'Beginning'), ('P', 'Proficient'), ('M', 'Mother Tougne'), ('I', 'Influent'), ('L', 'Limilted')], max_length=1),
        ),
        migrations.AlterField(
            model_name='userlanguage',
            name='user_skill3',
            field=models.CharField(blank=True, choices=[('B', 'Beginning'), ('P', 'Proficient'), ('M', 'Mother Tougne'), ('I', 'Influent'), ('L', 'Limilted')], max_length=1),
        ),
    ]