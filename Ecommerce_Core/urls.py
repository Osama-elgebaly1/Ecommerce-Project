from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('product/<int:pk>',views.single_product,name='product'),
    path('about/',views.about,name='about'),
    path('category/<int:pk>',views.category,name='category'),
    path('search',views.search,name='search'),
]
