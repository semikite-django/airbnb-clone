from django.contrib.auth.models import AbstractUser
from django.db import models

"""
필드를 추가할 때, 두가지 옵션이 있다.
1. default = "" // 기본값으로 이전 데이터들 모두 default 값으로 처리
2. null = True  // 비어 있는 건 신경 안씀. 비어 있는 필드를 허용 함.
"""

class User(AbstractUser):

    """ Custom User Model  """

    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_OTHER = 'other'

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    """ 
        DB에 들어갈 정보가 위쪽에 변수로 지정되어 있는것임.
        ITEM_A = 'A'
        ITEM_CHOICES = (
            (ITEM_A, 'A')            #("DB에 들어갈 정보", "FORM에 나타날 정보")
        )
    """

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, 'English'),
        (LANGUAGE_KOREAN, 'Korean'),
    )

    CURRENCY_USD = 'usd'
    CURRENCY_KOR = 'krw'

    CURRENCY_CHOICES = (
        (CURRENCY_USD, 'USD'),
        (CURRENCY_KOR, 'KRW'),
    )

    avatar = models.ImageField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)

    """
    null=True 인데도 DB에서 필수값이라고 하냐면!!!!
        null은 데이터베이스에서 사용하게 되는 것이고
        폼은 blank를 사용하기 때문이다.

        따라서 null=True를 하더라도 Form을 통해 입력 받으면, Blank = True를 설정해야 함. 
    """