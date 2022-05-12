from django.contrib import admin
from django.utils.html import mark_safe
from . import models

class PhotoInline(admin.TabularInline):
    model = models.Photo

# class CustomRoomAdmin(admin.ModelAdmin):
@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition"""

    inlines = (PhotoInline,)

    fieldsets = (
        (
            'Basic Info',
            {'fields': ('name', 'description', 'country', 'city', 'address', 'price')}
        ),
        (
            'Times',
            {'fields': ('check_in', 'check_out', 'instant_book',)}
        ),
        (
            'Spaces',
            {'fields': ('guests', 'beds', 'bedrooms', 'baths')}
        ),
        (
            'More About the Spaces',
            {
                'classes': ('collapse',),   # 섹션을 접을 수 있게 하는 옵션
                'fields': ('amenities', 'facilities', 'house_rules',)
            }
        ),
        (
            'Last Detail',
            {'fields': ('host',)}
        )


    )

    list_display = (
        'name',
        'country',
        'city',
        'price',
        'guests',
        'beds',
        'bedrooms',
        'baths',
        'check_in',
        'check_out',
        'instant_book',
        'count_amenities',
        'count_photos',
        'total_rating',
    )

    ordering = ('name', 'price', 'bedrooms',)

    list_filter = ('instant_book', 'host__superhost', 'host__gender', 'room_type', 'amenities', 'facilities', 'house_rules','city', 'country',)

    raw_id_fields = ("host",)

    # search_fields = ("city",)
    search_fields = ('=city', '^host__username',)

    filter_horizontal = ('amenities', 'facilities', 'house_rules',)

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()

    # count_amenities.short_description = "Hello"

@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin Definition"""

    list_display = (
        'name',
        'used_by',
    )

    def used_by(self, obj):
        return obj.rooms.count()

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo Admin Definition """
    list_display = ('__str__', 'get_thumbnail')

    # mark_safe = HTML을 만들어 줌
    def get_thumbnail(self, obj):
        tag = mark_safe(f'<img width="50px" height="50px" src="{obj.file.url}" />')
        return tag
    get_thumbnail.short_description = 'Thumbnail'


