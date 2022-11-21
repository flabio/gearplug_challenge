from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.users.api.serializers import CustomTokenObtainPairSerializer, CustomUserSerializer
#from user_app import models
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.users.models import Account
from django.contrib import auth

from django.contrib.auth import authenticate

@api_view(['POST',])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'El registro del usuario fue exitoso'
            data['username'] = account.username
            data['email'] = account.email
            data['first_name'] = account.first_name
            data['last_name'] = account.last_name
         
            #token = Token.objects.get(user=account).key
            #data['token'] = token

            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
            return Response(data)

        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def login_view(request):
    data = {}
    if request.method=='POST':
        username = request.data.get('username')
        password = request.data.get('password')
        account = auth.authenticate(username=username, password=password)
      
        if account is not None:
            data['response']='El Login fue exitoso'
            data['username']=account.username
            data['email']=account.email
            data['first_name']=account.first_name
            data['last_name']=account.last_name
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
            return Response(data)
        else:
            data['error'] = "Credenciales incorrectas"
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)



        
# class Login(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer

#     def post(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(
#             username=username,
#             password=password
#         )
       
#         if user:
#             login_serializer = self.serializer_class(data=request.data)
#             user_serializer = CustomUserSerializer(user)
            
#             if login_serializer.is_valid():
#                 user_serializer = CustomUserSerializer(user)
#                 return Response({
#                     'token': login_serializer.validated_data.get('access'),
#                     'refresh-token': login_serializer.validated_data.get('refresh'),
#                     'user': user_serializer.data,
#                     'message': 'Inicio de Sesion Existoso'
#                 }, status=status.HTTP_200_OK)
#             return Response({'error': 'Contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)
#         return Response({'error': 'Contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)


# # class Login(TokenObtainPairView):
# #     serializer_class = CustomTokenObtainPairSerializer

# #     def post(self, request):
# #         username = request.data.get('username')
# #         password = request.data.get('password')
# #         account = auth.authenticate(username=username, password=password)
        
# #         login_serializer = self.serializer_class(data=request.data)
# #         data = {}
# #         print(account)
# #         if login_serializer.is_valid():
# #             user_serializer =  CustomUserSerializer(account)
            
# #             data['response']='El Login fue exitoso'
# #             data['username']=account.username
# #             data['email']=account.email
# #             data['first_name']=account.first_name
# #             data['last_name']=account.last_name
# #             data['user']=user_serializer.data
# #             refresh = RefreshToken.for_user(account)
# #             data['token'] = {
# #                     'refresh': str(refresh),
# #                     'access': str(refresh.access_token)
# #                 }
# #             return Response(data, status=status.HTTP_200_OK)
# #         else:
# #             #return Response({'error': 'Contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)
# #             return Response({'error': 'Contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)