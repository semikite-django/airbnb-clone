"""
1. django importlib
2. ext import
3. my pkg import
"""
from django.db import models
from django.utils.safestring import mark_safe
from django.urls import reverse
from core import models as core_models
from django_countries.fields import CountryField

# from users import models as user_models

class AbstractItem(core_models.TimeStampedModel):

    """" Abstract Item """
    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class RoomType(AbstractItem):

    """ Room Type Object Definition """
    class Meta:
        verbose_name = 'Room Types'
        ordering = ['created']

class Amenity(AbstractItem):

    """ Amenity Type Object Definition """
    class Meta:
        verbose_name_plural = 'Amenities'

class Facility(AbstractItem):

    """ Facility Object Definition """
    class Meta:
        verbose_name_plural = 'Facilities'

class HouseRule(AbstractItem):

    """ HouseRule Object Definition """
    class Meta:
        verbose_name = 'House Rules'

class Room(core_models.TimeStampedModel):

    """ Room Model Definition """

    description = models.TextField()
    name = models.CharField(max_length=140)
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey('users.User', related_name='rooms', on_delete=models.CASCADE)
    room_type = models.ForeignKey('RoomType', related_name='rooms', on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField('Amenity', related_name='rooms', blank=True)
    facilities = models.ManyToManyField('Facility', related_name='rooms', blank=True)
    house_rules = models.ManyToManyField('HouseRule', related_name='rooms', blank=True)

    def __str__(self):
        return self.name

    # Method Override
    def save(self, *args, **kwargs):
        print(self.city)
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('rooms:detail', kwargs={'pk': self.pk})

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return round(all_ratings / len(all_reviews), 2)
        return 0

    # def total_rating(self):
    #     all_reviews = self.reviews.all()
    #     # all_ratings = 0
    #     all_ratings = []
    #
    #     for review in all_reviews:
    #         all_ratings += review.rating_average()
    #         # print(review.rating_average())
    #     # return all_ratings / len(all_reviews)
    #     return all_ratings

class Photo(core_models.TimeStampedModel):

    """ Photo Object Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to='room_photos')
    room = models.ForeignKey('Room', related_name='photos', on_delete=models.CASCADE)

    def __str__(self):
        return self.caption