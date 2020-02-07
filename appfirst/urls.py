from django.contrib import admin
from django.urls import path
from .views import hello,hello1
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',hello),
    path('hello1',hello1,name='klm'),
]
