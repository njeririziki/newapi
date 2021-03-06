# Generated by Django 3.2.8 on 2021-10-14 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dependants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('member_type', models.CharField(max_length=30)),
                ('principal_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.principal')),
            ],
        ),
    ]
