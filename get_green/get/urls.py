from django.urls import path
from . import views

urlpatterns=[
    path('',views.first),
    path('back',views.first),
   path('home',views.home),
   path('invest',views.invest),
   path('report',views.report),
   path('clean',views.clean),
   path('buy1',views.buy),
   path('buyorsell',views.buyorsell),
   path('sell1',views.sell),
   path('orientation',views.orr),
   path('buy',views.buy),
   path('map',views.map),
   path('submit',views.sub),
    path('confirm2',views.con),
    path('add',views.action)
]