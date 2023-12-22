import uuid

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class MyModelA(models.Model):

    def validate_even(value):
        if value % 2 != 0:
            raise ValidationError(
                _('%(value)s is not an even number'),
                params={'value': value},
            )

    class MyChoices(models.TextChoices):
        CHOICE1 = 'CH1'
        CHOICE2 = 'CH2'
        CHOICE3 = 'CH3'

    char_a = models.CharField(max_length=255)
    text_a = models.TextField(blank=True, verbose_name="text_a verbose name")
    integer_a = models.IntegerField(null=True)
    choice_a = models.CharField(choices=MyChoices.choices, max_length=255)
    db_column_a = models.CharField(max_length=255, db_column='db_column_aaaaaa', help_text='this is help text')
    db_index_a = models.CharField(max_length=255, db_index=True, default='This is db_index field')
    editable_false_a = models.CharField(max_length=255)
    date_field_a = models.DateField(null=True)
    even_a = models.IntegerField(validators=[validate_even])
    duration_a = models.DurationField()
    email_a = models.EmailField()
    file_field_a = models.FileField(upload_to='./for_file_field')
    filefield_patch_a = models.FilePathField(path='/home/sa/Documents')
    image_field_a = models.ImageField()
    IP_field_a = models.GenericIPAddressField()
    JSON_field_a = models.JSONField()
    slug_a = models.SlugField()
    time_field_a = models.TimeField()
    URL_field_a = models.URLField()
    uuid_id_a = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class MyModelB(models.Model):
    name = models.CharField(max_length=255)
    data = models.IntegerField()
    my_foreigen = models.ForeignKey('self', on_delete=models.CASCADE)


class Author(models.Model):
    name = models.CharField(max_length=255)


class Genre(models.Model):
    name = models.CharField(max_length=255)


class Producer(models.Model):
    name = models.CharField(max_length=255)


class Book(models.Model):
    name = models.CharField(max_length=255)
    book_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_genre = models.ManyToManyField(Genre)
    book_producer = models.OneToOneField(Producer, on_delete=models.CASCADE)
