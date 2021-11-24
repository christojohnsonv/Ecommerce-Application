from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from client import views
from client import apiviews




urlpatterns = [
    path('usignup',views.Usignup,name='usignup'),
    path('',views.Ulogin,name='ulogin'),
    path('logout',views.signout,name='logout'),
    path('updusr<int:userid>',views.updusr,name='updusr'),
    path('addusr',views.addusr,name='addusr'),
    path('addord',views.addord,name='addord'),
    path('disusr',views.disusr,name="disusr"),
    path('disord',views.disord,name="disord"),
    path('delusr<int:userid>',views.delusr,name='delusr'),
    path('disses',views.disses,name="disses"),
    path('disusrrest',apiviews.disusrrest,name='disusrrest'),
    path('updupw<int:userid>',views.updupw,name="updupw"),
    path('updupc<int:userid>',views.updupc,name='updupc'),
    path('ad2car',views.ad2car,name='ad2car'),
    path('discar',views.discar,name='discar'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('usersignup',views.usersignup,name='usersignup'),
    path('disordrest',apiviews.disordrest,name='disordrest')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

