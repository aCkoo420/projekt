# Generated by Django 3.2 on 2021-04-30 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(help_text='Enter an agent type', max_length=20, unique=True, verbose_name='Agent type')),
            ],
        ),
        migrations.AddField(
            model_name='agent',
            name='date_added',
            field=models.DateField(blank=True, help_text='Please use the following format: <em>DD/MM/YYYY</em>', null=True, verbose_name='Release Date'),
        ),
        migrations.AddField(
            model_name='agent',
            name='personality',
            field=models.TextField(blank=True, null=True, verbose_name='Personality'),
        ),
        migrations.AddField(
            model_name='agent',
            name='types',
            field=models.ManyToManyField(help_text='Select a type for this agent', to='characters.Type'),
        ),
    ]