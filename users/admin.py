from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


# admin.site.register(models.User, CustomUserAdmin)
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """
    # UserAdmin.fieldsets 기본 장고에서 만들어주는 관리화면에 우리가 추가한 필드셋을 추가
    fieldsets = UserAdmin.fieldsets + (
        (
            "Banana",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            }
        ), # fieldsets 는 튜플이라서 하나만 추가할 경우 뒤에 , 콤마 해줘야 함.
    )
    # avatar = models.ImageField(null=True, blank=True)
    # gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True, blank=True)
    # bio = models.TextField(default='', blank=True)
    # birthdate = models.DateField(null=True)
    # language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True)
    # currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, null=True, blank=True)
    # superhost = models.BooleanField(default=False)

    list_filter = UserAdmin.list_filter + (
        "superhost",
    )

    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'is_active',
        'language',
        'currency',
        'superhost',
        'is_staff',
        'is_superuser',
     )

""" 


아래 것들은 제거하고, 어드민 패널을 확장해서 쓰기로 함.
간단하게 사용하려면 아래 어드민으로 처리 가능할 것 같음. 

@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    # 장고어드민에서 테이블에 나타낼 항목들을 정할 수 있음.
    list_display = ('username', 'email', 'gender', 'language', 'currency', 'superhost')
    # 장고어드민에서 필터(조건을 걸어서 볼 수 있음)
    list_filter = ('language', 'currency', 'superhost',)
"""

