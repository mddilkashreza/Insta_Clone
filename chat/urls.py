from django.urls import path
from chat.views import user_chat,message,delete_message


app_name = "chat"


urlpatterns = [
    path('message/',message, name="message"),
    path('delete/',delete_message, name="delete_message"),
    path('message/<str:username>/',user_chat,name="user_chat"),
    
    
]



# path('remove-post/', delete_post, name="delete_post"),