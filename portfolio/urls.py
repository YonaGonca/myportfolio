from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('me/', views.aboutme, name='aboutme'),
    path('change-language/<str:lang_code>/', views.change_language, name='change_language'),
    path("send-email/", views.contact_view, name="send_email"),
]