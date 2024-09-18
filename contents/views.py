from django.shortcuts import render
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics,viewsets
from rest_framework import mixins
from .models import UserPost, UserPostMedia,PostLikes,PostComment
from .serializers import UserMediaSerializer, UserPostCreationSerializer,PostFeedSerializer,PostMediaViewSerializer,PostLikeCreateSerializer,PostCommentCreateSerializer
from .filters import CurrentUserFollowingFilterBacked
from rest_framework.response import Response
from .permissions import HasLikingPermission

# Create your views here.


class UserPostCreateFeed(mixins.CreateModelMixin,mixins.ListModelMixin ,generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = UserPost.objects.all()
    serializer_class = UserPostCreationSerializer
    filter_backends = [CurrentUserFollowingFilterBacked]
    def get_serializer_context(self):
        return {'current_user': self.request.user.profile}

    def get_serializer_class(self):

        if self.request.method == 'GET':
            return PostFeedSerializer
        return self.serializer_class


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self,request,*args,**kwargs):
        return self.list(request, *args, **kwargs)


class UserPostMedia(mixins.CreateModelMixin,mixins.RetrieveModelMixin, generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    serializer_class = UserMediaSerializer




    def put(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class UserPostUpdateView(mixins.UpdateModelMixin,mixins.RetrieveModelMixin, generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = UserPost.objects.all()
    serializer_class = UserPostCreationSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get_serializer_class(self):

        if self.request.method == 'GET':
            return PostFeedSerializer
        return self.serializer_class
    def get(self,request,*args,**kwargs):
        return self.retrieve(request, *args, **kwargs)


class PostLikeViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated,HasLikingPermission]
    authentication_classes = [JWTAuthentication]
    serializer_class = PostLikeCreateSerializer
    queryset = PostLikes.objects.all()

    def get_serializer_context(self):
        return {'current_user':self.request.user.profile}

    def list(self, request):
        post_likes= self.queryset.filter(post_id=request.query_params['post_id'])

        page=self.paginate_queryset(post_likes)

        if page :

            serializer=self.get_serializer(page,many=True)
            return  self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(post_likes,many=True)

        return Response(serializer.data)



class PostCommentViewSet(viewsets.ModelViewSet):

        permission_classes = [IsAuthenticated]
        authentication_classes = [JWTAuthentication]
        serializer_class = PostCommentCreateSerializer
        queryset = PostComment.objects.all()

        def get_serializer_context(self):
            return {'current_user': self.request.user.profile}

        def list(self, request):
            post_comment = self.queryset.filter(post_id=request.query_params['post_id'])

            page = self.paginate_queryset(post_comment)

            if page:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(post_comment, many=True)

            return Response(serializer.data)