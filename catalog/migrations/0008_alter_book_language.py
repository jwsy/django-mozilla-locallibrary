# Generated by Django 3.2.6 on 2021-08-15 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_language_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.ForeignKey(default='English', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.language'),
        ),
    ]
