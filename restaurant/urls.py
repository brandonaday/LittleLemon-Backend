from django.urls import path, include
from .views import index, home, MenuItemsView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Default index view
    path('', index, name='index'),

    # Alias for the index view as 'home'
    path('home/', home, name='home'),

    # Menu Items API views
    path('menu/', MenuItemsView.as_view(), name='menu-list-create'),
    path('menu/<int:pk>', SingleMenuItemView.as_view(), name='menu-detail'),

    # API Token authentication view
   # path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    #path('api-auth/', include('rest_framework.urls')),

]
