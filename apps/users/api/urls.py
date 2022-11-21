from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from apps.users.api.views import registration_view, logout_view,login_view,Login

urlpatterns = [
   # path('login/', obtain_auth_token, name='login'),
   # path('', Login.as_view(), name='login'),
    path('logout/',logout_view,name='logout'), 
    path('register/',registration_view,name='register'), 
    # path('token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),

]