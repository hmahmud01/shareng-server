from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from application import views

urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('ticketDetail/', views.ticketDetail, name="ticketdetail"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)