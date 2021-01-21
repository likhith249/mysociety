from . import views
from django.urls import path
urlpatterns = [
    path('add_soc/',views.create_society),
    path('add_mem/',views.add_member),
]
