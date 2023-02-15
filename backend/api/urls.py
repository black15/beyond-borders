from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('items/', views.ItemsList.as_view()),
    path('item/<int:pk>', views.ItemDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)