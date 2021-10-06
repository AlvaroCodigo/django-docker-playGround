from django.urls import path
from . import views
from .views import pageListView, PageDetailView

urlpatterns = [
    path('', pageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
] 