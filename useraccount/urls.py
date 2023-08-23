from django.urls import path
from useraccount.views import user_login,user_logout,signup


app_name = "user"


urlpatterns = [
    path('login/',user_login,name="login"),
    path('logout/',user_logout,name="logout"),
    path('signup/',signup,name="signup"),
]