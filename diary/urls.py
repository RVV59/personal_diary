from django.urls import path
from .views import (
    EntryListView,
    EntryDetailView,
    EntryCreateView,
    EntryUpdateView,
    EntryDeleteView,
    SignUpView,
)

app_name = 'diary'  # Определяем пространство имен

urlpatterns = [
    path('', EntryListView.as_view(), name='entry_list'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('entry/<int:pk>/', EntryDetailView.as_view(), name='entry_detail'),
    path('entry/new/', EntryCreateView.as_view(), name='entry_create'),
    path('entry/<int:pk>/edit/', EntryUpdateView.as_view(), name='entry_edit'),
    path('entry/<int:pk>/delete/', EntryDeleteView.as_view(), name='entry_delete'),
]
