# Generated by Django 2.0 on 2018-01-18 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0009_auto_20180117_0543'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Users.UserInformation', unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='userlanguage',
            name='user_skill1',
            field=models.CharField(blank=True, choices=[('L', 'Limilted'), ('I', 'Influent'), ('P', 'Proficient'), ('M', 'Mother Tougne'), ('B', 'Beginning')], max_length=1),
        ),
        migrations.AlterField(
            model_name='userlanguage',
            name='user_skill2',
            field=models.CharField(blank=True, choices=[('L', 'Limilted'), ('I', 'Influent'), ('P', 'Proficient'), ('M', 'Mother Tougne'), ('B', 'Beginning')], max_length=1),
        ),
        migrations.AlterField(
            model_name='userlanguage',
            name='user_skill3',
            field=models.CharField(blank=True, choices=[('L', 'Limilted'), ('I', 'Influent'), ('P', 'Proficient'), ('M', 'Mother Tougne'), ('B', 'Beginning')], max_length=1),
        ),
    ]
