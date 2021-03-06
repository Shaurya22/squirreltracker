# Generated by Django 3.0 on 2019-12-10 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrelapp', '0004_auto_20191210_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrels',
            name='Age',
            field=models.CharField(choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile'), ('', ''), ('?', '?')], default='', help_text='Age', max_length=50),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Approaches',
            field=models.BooleanField(default=False, help_text='Is it approaching?'),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Chasing',
            field=models.BooleanField(default=False, help_text='Is it chasing something?'),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Climbing',
            field=models.BooleanField(default=False, help_text='Is it climbing something?'),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Eating',
            field=models.BooleanField(default=False, help_text='Is it eating something?'),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Foraging',
            field=models.BooleanField(default=False, help_text='Is it looking for food?'),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Indifferent',
            field=models.BooleanField(default=False, help_text='Is it indifferent?'),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Kuks',
            field=models.BooleanField(default=False, help_text='Is it making short noise?'),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Moans',
            field=models.BooleanField(default=False, help_text='Is it moaning?'),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Other_Activities',
            field=models.CharField(default=None, help_text='What else is it doing?', max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Primary_Fur_Colour',
            field=models.CharField(choices=[('Black', 'Black'), ('Cinnamon', 'Cinnamon'), ('Gray', 'Gray')], default='Black', help_text='Color of the squirrel fur', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Quaas',
            field=models.BooleanField(default=False, help_text='Is it making longer noises?'),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Running',
            field=models.BooleanField(default=False, help_text='Is it on the run?'),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Runs_from',
            field=models.BooleanField(default=False, help_text='Is it running away?'),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Shift',
            field=models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], help_text='Shift', max_length=2),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Specific_location',
            field=models.CharField(default='', help_text='Specific Location of the sighting', max_length=30),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Tail_flags',
            field=models.BooleanField(default=False, help_text='Is it flagging it’s tail?'),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Tail_twitches',
            field=models.BooleanField(default=False, help_text='Is it twitching it’s tail?'),
        ),
    ]
