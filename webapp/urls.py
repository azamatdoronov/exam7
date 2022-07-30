from django.urls import path

from webapp.views import IndexView, PollView, CreatePoll, UpdatePoll, DeletePoll

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('poll/<int:pk>', PollView.as_view(), name='PollView'),
    path('poll/create/', CreatePoll.as_view(), name='CreatePoll'),
    path('poll/update/<int:pk>/', UpdatePoll.as_view(), name='UpdatePoll'),
    path('poll/delete/<pk>/', DeletePoll.as_view(), name='DeletePoll'),
]
