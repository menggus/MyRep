# Generated by Django 2.1.1 on 2019-08-24 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courserecord',
            name='teacher',
            field=models.ForeignKey(blank=True, limit_choices_to={'depart_id_in': [7, 8, 9]}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.UserInfo', verbose_name='讲师'),
        ),
    ]
