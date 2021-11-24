"""Live_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from product import views

urlpatterns = [
    path('addcat',views.addcat,name="addcat"),
    path('discat',views.discat,name='discat'),
    path('addpro',views.addpro,name="addpro"),
    path("dispro",views.dispro,name="dispro"),
    path('userhome',views.userhome,name='userhome'),
    path('usershop',views.usershop,name="usershop"),
    path('usershopfilter<int:catid>',views.usershopfilter,name='usershopfilter'),
    path('add2cart<int:proid>',views.add2cart,name="add2cart"),
    path('discart',views.discart,name="discart"),
    path('userprofiledis',views.userprofiledis,name='userprofiledis'),
    path('userprofileupd',views.userprofileupd,name='userprofileupd'),
    path('userpasswordupd',views.userpasswordupd,name='userpasswordupd'),
    path('userabout',views.userabout,name='userabout'),
    path('userservice',views.userservice,name='userservice'),
    path('userpricefilter',views.userpricefilter,name='userpricefilter'),
    path('usershopsearch',views.usershopsearch,name="usershopsearch"),
    path('usershopsort',views.usershopsort,name="usershopsort"),
    path('delcart<int:car_id>',views.delcart,name="delcart")

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

