from django.urls import path
from store import views


urlpatterns = [
    path('offers/', views.OfferList.as_view()),
    path('offers/<int:pk>/', views.OfferDetails.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetails.as_view()),
]

# from django.urls import path
# from store import views
#
# urlpatterns = [
#     path('offers/', views.offer_list),
#     path('offers/<int:pk>/', views.offer_detail),
# ]
