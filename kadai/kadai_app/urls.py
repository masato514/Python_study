from django.urls import path

from . import views

app_name = 'kadai_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name = "index"),
    path('inquiry/', views.InquiryView.as_view(), name = "inquiry"),
    path('play-list/', views.PlayListView.as_view(), name= "play_list"),
    path('play-detail/<int:pk>/', views.PlayDetailView.as_view(), name = "play_detail"),
    path('play-create/', views.PlayCreateView.as_view(), name = "play_create"),
    path('play-update/<int:pk>/', views.PlayUpdateView.as_view(), name = "play_update"),
    path('play-delete/<int:pk>/', views.PlayDeleteView.as_view(), name = "play_delete"),
]