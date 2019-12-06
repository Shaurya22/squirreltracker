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

    squirrel_id = models.CharField(
            max_length=30,
            help_text=_("Squirrel ID"),
        )

    shift = models.CharField(
            max_length=2,
            choices=SHIFT_CHOICES,
        )

    date = models.DateField(
            help_text=_("Date of the sighting"),
        )

    age = models.CharField(
            max_length=50,
            choices=AGE_CHOICES,
            help_text=_("Age"),
        )

    location = models.CharField(
            max_length=100,
            choices=LOC_CHOICES,
            default=OTHER,
            help_text=_("Location of the Squirrel"),
        )

    particular_location = models.CharField(
            max_length=30,
            help_text=_("Particular Location of the sighting"),
        )

    color_of_fur = models.CharField(
            max_length=20,
            choices=COLOR_CHOICES,
            help_text=_("Color of the squirrel fur"),
        )
    
    Run = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Is it on the run?'),
            )

    Chase = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Is it chasing something?'),
            )


    Climb = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Is it climbing something?'),
            
            )

    Eat = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Is it eating something?'),
            )

    forage = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Is it looking for food?'),
            )

    other_activities = models.CharField(
            max_length=100,
            help_text=_('What else is it doing?'),
            )

    kuk = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Is it making short noise?'),
            )

    quaa = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Is it making longer noises?'),
            )

    moans = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Is it moaning?'),
            )

    tail_flags = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Is it flagging it’s tail?'),
            )

    tail_twitches = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Is it twitching it’s tail?'),
            )

    approach = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Is it approaching?'),
            )

    indifferent = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Is it indifferent?'),
            )

    runs_from = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Is it running away?'),
        )
    def __str__(self):
        return self.Unique_Squirrel_Id

# Create your models here.
