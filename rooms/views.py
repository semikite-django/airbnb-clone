# from datetime import datetime
# from math import ceil
# from django.shortcuts import render, redirect
# from django.core.paginator import Paginator, EmptyPage
from django_countries import countries
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.http import Http404
from . import models

class HomeView(ListView):
    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    page_kwarg = 'page'
    ordering = 'created'
    context_object_name = 'rooms'
    # template_name = 'rooms/room_list.html'

    def get_context_data(self, **kwargs):
        """ 클래스 뷰에서 Context를 넘길 때 사용 """
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context['now'] = now    # {{ now }} 로 사용할 수 있음.
        # context = {}
        return context



# 두번째
# def all_rooms(request):
#     page = request.GET.get('page', 1)
#     page = int(page or 1)
#     room_list = models.Room.objects.all()
#     paginator = Paginator(room_list, 10, orphans=5)
#     try:
#         rooms = paginator.page(int(page))
#         return render(request, 'rooms/room_list.html', {
#             'page': rooms,
#         })
#     except EmptyPage:
#         return redirect("/")


# 첫번째
# page = request.GET.get('page', 1)
    # page = int(page or 1) # 페이지가 없으면 1을 기본 값으로 설정
    # page_size = 10  # 한페이지에 볼 게시물 수
    # limit = page_size * page
    # offset = limit - page_size
    # all_rooms = models.Room.objects.all()[offset:limit]
    # page_count = ceil(models.Room.objects.count() / page_size)
    # return render(request, 'rooms/room_list.html', context={
    #     'rooms': all_rooms,
    #     'page': page,
    #     'page_count': page_count,
    #     'page_range': range(1, page_count),
    # })


class RoomDetail(DetailView):
    model = models.Room

# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, 'rooms/room_detail.html', context={
#             'room': room,
#         })
#     except models.Room.DoesNotExist:
#         raise Http404()
#         # return redirect(reverse('core:home'))
#



# function based view 로 진행
def search(request):
    # print(request.GET)
    city = request.GET.get('city', 'Anywhere')
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))
    price = int(request.GET.get("price", 0))
    guests = int(request.GET.get("guests", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    beds = int(request.GET.get("beds", 0))
    baths = int(request.GET.get("baths", 0))
    instant = bool(request.GET.get("instant", False))
    superhost = bool(request.GET.get("superhost", False))

    s_amenities = request.GET.getlist('amenities')
    s_facilities = request.GET.getlist('facilities')

    form = {
        'city': city,
        's_room_type': room_type,
        's_country': country,
        'price': price,
        'guests': guests,
        'bedrooms': bedrooms,
        'beds': beds,
        'baths': baths,
        'instant': instant,
        'superhost': superhost,
        's_amenities': s_amenities,
        's_facilities': s_facilities,

    }

    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()

    choices = {
        'countries': countries,
        'room_types': room_types,
        'amenities': amenities,
        'facilities': facilities,
    }

    filter_args = {}

    if city != "Anywhere":
        filter_args["city__startswith"] = city

    filter_args['country'] = country

    if room_type != 0:
        filter_args['room_type__pk'] = room_type
        # filter_args['room_type__pk__exact'] = room_type

    if price != 0:
        filter_args['price__lte'] = price

    if guests != 0:
        filter_args['guests__gte'] = guests

    if bedrooms != 0:
        filter_args['bedrooms__gte'] = bedrooms

    if beds != 0:
        filter_args['beds__gte'] = beds

    if baths != 0:
        filter_args['baths__gte'] = baths

    if instant is True:
        filter_args['instant_book'] = True

    if superhost is True:
        filter_args['host__superhost'] = True

    if len(s_amenities) > 0:
        for s_amenity in s_amenities:
            filter_args["amenities__pk"] = int(s_amenity)

    if len(s_facilities) > 0:
        for s_facility in s_facilities:
            filter_args["facilities__pk"] = int(s_facility)

    rooms = models.Room.objects.filter(**filter_args)

    return render(
        request,
        'rooms/search.html',
        {
            **form, **choices, "rooms": rooms,
        },
    )

