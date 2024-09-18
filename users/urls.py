from . import views
from django.urls import path
from rest_framework.views import APIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView
urlpatterns = [
    path('index/',views.index,name='user_index_page'),
    path('signup/',views.create_user,name='add_new_user'),
    path('signup/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('login/',TokenObtainPairView.as_view(),name='login_api'),
    path('list/',views.user_list_api,name='login_api'),
    path('<int:pk>/',views.get_user,name='get_user'),
    path('update/',views.update_user_profile,name='update_user'),
    path('delete/<int:pk>/',views.delete,name='delete_user'),
    path('edge/',views.UserNetworkEdgeView.as_view(),name='Network_edge')
    ]


