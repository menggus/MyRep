# Generated by Django 2.1.1 on 2019-08-15 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0003_auto_20190813_0655'),
    ]

    operations = [
        migrations.CreateModel(
            name='Depart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='部门')),
                ('tel', models.CharField(max_length=32, unique=True, verbose_name='部门电话')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='depart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app02.Depart'),
        ),
    ]
