from django.urls import path

from pages.views import Index

app_name = 'pages'

urlpatterns = [
    path('', Index.as_view(), name='index')
]
