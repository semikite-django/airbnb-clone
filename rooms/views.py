# from datetime import datetime
# from math import ceil
# from django.shortcuts import render, redirect
# from django.core.paginator import Paginator, EmptyPage
from django.utils import timezone
from django.views.generic import ListView
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