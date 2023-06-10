from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UsertAll.as_view()),
    path('category/', views.CategoryAll.as_view()),
    path('category/<int:id>', views.CategoryByID.as_view()),
    path('dish/', views.DishAll.as_view()),
    path('item/', views.ItemAll.as_view()),
    path('cart/', views.CartAll.as_view()),
    path('delivery/', views.DeliveryAll.as_view())
]
