from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

def attachment_path(instance, filename):
    return "characters/" + str(instance.characters.id) + "/attachments/" + filename
def poster_path(instance, filename):
    return "characters/" + str(instance.id) + "/poster/" + filename

# Create your models here.


class Type(models.Model):
    type = models.CharField(max_length=20, unique=True, verbose_name="Agent type", help_text='Enter an agent type')

    class Meta:
        ordering = ["type"]

    def __str__(self):
        return self.type

class Agent(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name="Agent name", help_text='Enter an agent name')
    personality = models.TextField(blank=True, null=True, verbose_name='Personality')
    date_added = models.DateField(blank=True, null=True,
                                  help_text="Please use the following format: <em>DD/MM/YYYY</em>",
                                  verbose_name="Release Date")
    poster = models.ImageField(upload_to=poster_path, blank=True, null=True, verbose_name="Poster")
    country_origin = models.TextField(blank=True, null=False, verbose_name='Country of origin')
    types = models.ManyToManyField(Type, help_text="Select a type for this agent")


class Meta:
    ordering = ["-date_added","types"]

    def __str__(self):
        return f"{self.name}, year: {str(self.date_added.year)}, type: {str(self.Type)}"
    def get_absolute_url(self):
        return reverse('Agent-detail', args=[str(self.id)])

class Attachment(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    file = models.FileField(upload_to=attachment_path, null=True, verbose_name="File")
    TYPE_OF_ATTACHMENT = (
        ('audio', 'Audio'),
        ('image', 'Image'),
        ('text', 'Text'),
        ('video', 'Video'),
        ('other', 'Other'),
    )
    type = models.CharField(max_length=5, choices=TYPE_OF_ATTACHMENT, blank=True, default='image',
                            help_text='Select allowed attachment type', verbose_name="Attachment type")
    characters = models.ForeignKey(Agent, on_delete=models.CASCADE)

    class Meta:
        ordering = ["type"]

    def __str__(self):
        return f"{self.title}, ({self.type})"