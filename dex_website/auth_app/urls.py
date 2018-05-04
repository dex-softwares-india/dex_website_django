from django.urls import re_path
from . import views

app_name='auth_app'

urlpatterns=[
    re_path('success/',views.response_received),
    re_path('',views.index)
]