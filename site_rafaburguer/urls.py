from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from site_rafaburguer import views

app_name = "site_rafaburguer"

urlpatterns = [
    path("", views.index, name="index"),
]
