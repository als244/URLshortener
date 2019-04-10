from django.urls import path
from django.contrib import admin
from .views import index, shorten, recent, top, count, redirectShortened, all_links


urlpatterns = [
	path('', index),
	path('admin/', admin.site.urls),
	path('shorten/', shorten),
	path('recent/', recent),
    path('top/', top),
    path('count/', count),
    path('all-links/', all_links),
    path('shorten/<longURL>/', shorten),
    path('count/<shortURL>/', count),
    path('<shortURL>', redirectShortened),
]
