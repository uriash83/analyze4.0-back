from django.urls import path
from factors.views import (
    FactorDetailView,
    FactorListView, 
    FactorCreateView,
    FactorUpdateView,
    FactorDeleteView
)


urlpatterns = [
    path('',FactorListView.as_view()),    
    path('<pk>',FactorDetailView.as_view()),
    path('create/',FactorCreateView.as_view()),
    path('<pk>/update/',FactorUpdateView.as_view()),
    path('<pk>/delete/',FactorDeleteView.as_view()),]