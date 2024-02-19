
from django.urls import path

from Arch_app.views import get_period, get_periods_style, get_style, get_substyles, search, style_photo, get_style_by_slug

urlpatterns = [
    path('period', get_period),
    path("period/<int:period_id>/styles", get_periods_style),
    path("styles/<int:id>", get_style ),
    path("styles/<int:parent_id>/substyles", get_substyles),
    path("search", search),
    path("styles/<int:style_id>/photos", style_photo),
    path("styles/<str:slug>", get_style_by_slug),
]