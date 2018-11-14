from django.db import models
from django.core.validators import FileExtensionValidator, validate_image_file_extension


class Pictogram(models.Model):
    """
    A picture representing a word/idea.

    https://simple.wikipedia.org/wiki/Pictogram
    """

    audio = models.FileField(help_text='The spoken version of the pictogram',
                             upload_to='audio/',
                             validators=[FileExtensionValidator(['mp3'])])
    images = models.ImageField(help_text='The image version of the pictogram',
                               upload_to='images/',
                               validators=[validate_image_file_extension])
    text = models.CharField(help_text='The text version of the pictogram',
                            max_length=255)
