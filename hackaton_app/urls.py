from django.urls import path
from . import views
from .views import PostCreate
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Pages.home, name = 'home page'),

    path('problem/', views.Pages.problem, name = 'problem dimostration page'),
    path('solution/', views.Pages.solution, name = 'solution dimostration page'),

    path('forum/', views.Pages.post, name = 'post forum'),
    path('create/', PostCreate.as_view(), name = 'create post'),
    path('about/', views.Pages.about, name = 'about page'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)