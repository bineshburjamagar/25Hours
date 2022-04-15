from unicodedata import name
from xml.dom.minidom import Document
from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [

    path("roomAdd",views.addRoom, name="roomAdd"),
    path("availableRooms",views.room, name="rm"),
    path('search',views.searchbar, name="search"),
    # path('product-detail/<int:id>',views.productDetail,name='productDetail'),
    path('details',views.roomDetails, name="details"),
    path('details/<int:id>',views.roomDetails, name="details"),
    path('payment',views.payment, name="payment")
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)