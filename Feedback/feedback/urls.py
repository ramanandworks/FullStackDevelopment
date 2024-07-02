from django.urls import path
from .views import feedback_view, feedback_thanks_view

urlpatterns = [
    path('', feedback_view, name='feedback_form'),
    path('thanks/', feedback_thanks_view, name='feedback_thanks'),
]
