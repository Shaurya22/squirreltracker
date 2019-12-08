from django.db import models
from django.utils.translation import gettext as _

class Squirrels(models.Model):
    TRUE = 'true'
    FALSE = 'false'
    AM = 'AM'
    PM = 'PM'
    ADULT = 'adult'
    JUVENILE = 'juvenile'
    BLANK = ''
    UNKNOWN = '?'
    BLACK = 'black'
    CINNAMON = 'cinnamon'
    GRAY = 'gray'
    GROUND_PLANE = 'ground plane'
    ABOVE_GROUND = 'above ground'
    OTHER = 'other'

    BOOL_CHOICES = (
            (TRUE, 'True'),
            (FALSE, 'False'),
        )
    
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

    Latitude = models.FloatField()

    Longitude = models.FloatField()

    Unique_Squirrel_ID = models.CharField(
            max_length=30,
            help_text=_("Squirrel ID"),
        )

    Shift = models.CharField(
            max_length=2,
            choices=SHIFT_CHOICES,
        )

    Date = models.DateField(
            help_text=_("Date of the sighting"),
        )

    Age = models.CharField(
            max_length=50,
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
            help_text=_("Particular Location of the sighting"),
        )

    Primary_Fur_Colour = models.CharField(
            max_length=20,
            choices=COLOR_CHOICES,
            help_text=_("Color of the squirrel fur"),
        )
    
    Running = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Is it on the run?'),
            )

    Chasing = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Is it chasing something?'),
            )


    Climbing = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Is it climbing something?'),
            
            )

    Eating = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Is it eating something?'),
            )

    Foraging = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Is it looking for food?'),
            )

    Other_Activities = models.CharField(
            max_length=100,
            help_text=_('What else is it doing?'),
            )

    Kuks = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Is it making short noise?'),
            )

    Quaas = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Is it making longer noises?'),
            )

    Moans = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Is it moaning?'),
            )

    Tail_flags = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Is it flagging it’s tail?'),
            )

    Tail_twitches = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Is it twitching it’s tail?'),
            )

    Approaches = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Is it approaching?'),
            )

    Indifferent = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Is it indifferent?'),
            )

    Runs_from = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Is it running away?'),
        )
    def __str__(self):
        return self.Unique_Squirrel_ID
