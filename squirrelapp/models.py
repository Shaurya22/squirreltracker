from django.db import models
from django.utils.translation import gettext as _

class Squirrels(models.Model):
    AM = 'AM'
    PM = 'PM'
    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    BLANK = ''
    UNKNOWN = '?'
    BLACK = 'Black'
    CINNAMON = 'Cinnamon'
    GRAY = 'Gray'
    GROUND_PLANE = 'Ground Llane'
    ABOVE_GROUND = 'Above Ground'
    OTHER = 'Other'

    SHIFT_CHOICES = (
            (AM, 'AM'),
            (PM, 'PM'),
        )
    
    AGE_CHOICES = (
            (ADULT, 'Adult'),
            (JUVENILE, 'Juvenile'),
            (BLANK, ''),
            (UNKNOWN, '?'),
        )

    COLOR_CHOICES = (
            (BLACK, 'Black'),
            (CINNAMON, 'Cinnamon'),
            (GRAY, 'Gray'),
        )

    LOC_CHOICES = (
            (GROUND_PLANE, ' Ground Plane'),
            (ABOVE_GROUND, 'Above Ground'),
            (OTHER, 'Other'),
        )

    Latitude = models.FloatField(help_text=_("Latitude"),)

    Longitude = models.FloatField(help_text=_("Longitude"),)

    Unique_Squirrel_ID = models.CharField(
            primary_key = True,
            max_length=30,
            help_text=_("Squirrel ID"),
        )

    Shift = models.CharField(
            max_length=2,
            choices=SHIFT_CHOICES,
            help_text=_("Shift"),
        )

    Date = models.DateField(
            help_text=_("Date of the sighting"),
        )

    Age = models.CharField(
            max_length=50,
            default=BLANK,
            choices=AGE_CHOICES,
            help_text=_("Age"),
        )

    Location = models.CharField(
            max_length=100,
            choices=LOC_CHOICES,
            default=OTHER,
            help_text=_("Location of the Squirrel"),
        )

    Specific_location = models.CharField(
            max_length=30,
            default="",
            help_text=_("Specific Location of the sighting"),
        )

    Primary_Fur_Colour = models.CharField(
            max_length=20,
            default=BLACK,
            choices=COLOR_CHOICES,
            help_text=_("Color of the squirrel fur"),
        )
    
    Running = models.BooleanField(
            default=False,
            help_text=_('Is it on the run?'),
            )

    Chasing = models.BooleanField(
            default=False,
            help_text=_('Is it chasing something?'),
            )


    Climbing = models.BooleanField(
            default=False,
            help_text=_('Is it climbing something?'),
            
            )

    Eating = models.BooleanField(
            default=False,
            help_text=_('Is it eating something?'),
            )

    Foraging = models.BooleanField(
            default=False,
            help_text=_('Is it looking for food?'),
            )

    Other_Activities = models.CharField(
            max_length=100,
            default=None,
            help_text=_('What else is it doing?'),
            )

    Kuks = models.BooleanField(
            default=False,
            help_text=_('Is it making short noise?'),
            )

    Quaas = models.BooleanField(
            default=False,
            help_text=_('Is it making longer noises?'),
            )

    Moans = models.BooleanField(
            default=False,
            help_text=_('Is it moaning?'),
            )

    Tail_flags = models.BooleanField(
            default=False,
            help_text=_('Is it flagging it’s tail?'),
            )

    Tail_twitches = models.BooleanField(
            default=False,
            help_text=_('Is it twitching it’s tail?'),
            )

    Approaches = models.BooleanField(
            default=False,
            help_text=_('Is it approaching?'),
            )

    Indifferent = models.BooleanField(
            default=False,
            help_text=_('Is it indifferent?'),
            )

    Runs_from = models.BooleanField(
            default=False,
            help_text=_('Is it running away?'),
        )
    def __str__(self):
        return self.Unique_Squirrel_ID
