# Generated by Django 5.0.4 on 2024-04-15 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.IntegerField()),
                ('user', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='from_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='to_date',
            field=models.DateField(),
        ),
    ]