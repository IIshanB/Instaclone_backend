from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('like',views.PostLikeViewSet,basename='test')
router.register('comment',views.PostCommentViewSet,basename='test1')
urlpatterns = [
    path('',views.UserPostCreateFeed.as_view(),name='user_post_view'),
    path('media/',views.UserPostMedia.as_view(),name='user_post_view'),
    path('<int:pk>/',views.UserPostUpdateView.as_view(),name='user_post_view'),
    path('',include(router.urls)),
    path('silk/', include('silk.urls', namespace='silk'))

]