from django.urls import path, include

urlpatterns = [
    path('', include('hackaton_app.urls')),
]