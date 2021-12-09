from django.urls import path
from .views import FlowersListView, FlowersDetailView, FlowersCreateView, FlowersUpdateView, FlowersDeleteView

urlpatterns = [
  
    path('flower/', FlowersListView.as_view(), name='flowers_list'),
    path('flower/<int:pk>/', FlowersDetailView.as_view(), name='flowers_detail'),
    path('flower/create/', FlowersCreateView.as_view(), name='flowers_create'),
    path('flower/<int:pk>/update/', FlowersUpdateView.as_view(), name='flowers_update'),
    path('flower/<int:pk>/delete/', FlowersDeleteView.as_view(), name='flowers_delete'),
]