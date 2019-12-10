# Generated by Django 3.0 on 2019-12-10 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrelapp', '0003_auto_20191210_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrels',
            name='Age',
            field=models.CharField(choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile'), ('', ''), ('?', '?')], help_text='Age', max_length=50),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Approaches',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], help_text='Is it approaching?', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Chasing',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], help_text='Is it chasing something?', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Climbing',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], help_text='Is it climbing something?', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Eating',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], help_text='Is it eating something?', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Foraging',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], help_text='Is it looking for food?', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Indifferent',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], help_text='Is it indifferent?', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Kuks',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], help_text='Is it making short noise?', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Location',
            field=models.CharField(choices=[('Ground Llane', ' Ground Plane'), ('Above Ground', 'Above Ground'), ('Other', 'Other')], default='Other', help_text='Location of the Squirrel', max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Moans',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], help_text='Is it moaning?', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Primary_Fur_Colour',
            field=models.CharField(choices=[('Black', 'Black'), ('Cinnamon', 'Cinnamon'), ('Gray', 'Gray')], help_text='Color of the squirrel fur', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Quaas',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], help_text='Is it making longer noises?', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Running',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], help_text='Is it on the run?', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Runs_from',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], help_text='Is it running away?', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Tail_flags',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], help_text='Is it flagging it’s tail?', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Tail_twitches',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], help_text='Is it twitching it’s tail?', max_length=20),
        ),
    ]