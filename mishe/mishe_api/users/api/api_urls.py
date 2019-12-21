from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from.api_views import UserList

urlpatterns = [
    path('users/',UserList.as_view(), name='user_list'),
]


urlpatterns = format_suffix_patterns(urlpatterns)