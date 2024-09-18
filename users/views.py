from django.shortcuts import render
from django.http import HttpResponse
from .models import User,UserProfile,NetworkEdge
from rest_framework.decorators import api_view,authentication_classes,permission_classes,APIView
from rest_framework.response import Response
from rest_framework import status,mixins,generics
from .serializers import UserCreateSerializer,UserProfileViewSerializer,UserProfileUpdateSerializer,NetworkEdgeCreateSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.permissions import IsAuthenticated
# Create your views here.


def index(request):
    return HttpResponse('Server is working for index')


@api_view(['POST'])
def create_user(request):
    print("on line 20->", request.data)


    serializer = UserCreateSerializer(data=request.data)

    response_data = {
        "errors" :None,
        "data" : None

    }

    if serializer.is_valid():
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        response_data["data"] = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        response_status = status.HTTP_201_CREATED
    else :
        response_data['errors'] = status.HTTP_400_BAD_REQUEST



    return Response(response_data, status=response_status)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def user_list_api(request):

    users = UserProfile.objects.all()

    serialized_data = UserProfileViewSerializer(instance=users,many=True)

    return Response(serialized_data.data,status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_user(request,pk=None):

    user=UserProfile.objects.filter(id=pk).first()

    if user:
        serializer=UserProfileViewSerializer(instance=user)
        response_data={
            "data":serializer.data,
            "error":None
        }
        response_status = status.HTTP_200_OK
    else:
        response_data = {
            "data": None,
            "error": "User nhi h"

        }
        response_status=status.HTTP_404_NOT_FOUND

    return Response(response_data,status=response_status)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_user_profile(request,pk=None):

    user_profile_serializer = UserProfileUpdateSerializer(instance=request.user.profile,
                                                          data=request.data)

    response_data={
        "data":None,
        "errors":None
    }

    if user_profile_serializer.is_valid() :
        user_profile=user_profile_serializer.save()

        response_data['data']=UserProfileViewSerializer(instance=user_profile).data

        response_status= status.HTTP_200_OK
    else:
        response_data['errors']=user_profile_serializer.errors
        response_status = status.HTTP_400_BAD_REQUEST

    return Response(response_data,status=response_status)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete(request,pk=None):

    user=request.user

    user.delete()

    response_data = {
        "data": None,
        "message": "User user is deleted successfully"
    }

    return Response(response_data,status=status.HTTP_200_OK)



class UserNetworkEdgeView(mixins.CreateModelMixin,generics.GenericAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = NetworkEdgeCreateSerializer
    queryset = NetworkEdge.objects.all()

    def get(self,request):
        pass

    def post(self,request,*args,**kwargs):
        request.data['from_user'] = request.user.profile.id

        return self.create(request,*args,**kwargs)

    def delete(self,request):
        pass
