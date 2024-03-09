# Generated by Django 5.0.3 on 2024-03-09 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0004_interview_duration_alter_interview_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=200)),
                ('first_name', models.CharField(default='', max_length=200)),
                ('gender', models.CharField(choices=[('ML', 'Male'), ('FM', 'Female'), ('DV', 'Diverse'), ('US', 'Not specified')], default='US', max_length=2)),
                ('date_of_birth', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'people',
            },
        ),
    ]