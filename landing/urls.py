from django.urls import path
from landing.views import MyFormView

urlpatterns = [
    path('', MyFormView.as_view())
]
