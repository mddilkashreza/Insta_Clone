from django.urls import path
from post.views import Home_feed,link,add_post,edit_post,delete_post,like_post,comment_post


app_name = "post"


urlpatterns = [
    path('home/',Home_feed,name="home"),
    path('link/',link,name="link"),
    path('create-post/',add_post, name="add_post"),
    path('update-post/<int:post_id>/',edit_post,name="edit_post"),
    path('remove-post/', delete_post, name="delete_post"),
    path('like-post/<int:post_id>/',like_post, name="like_post"),
    path('comment/<int:post_id>/',comment_post,name="comment_post"),
]