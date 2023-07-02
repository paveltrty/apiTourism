from django.urls import path
from . import views
urlpatterns = [
    path('create/post', views.add_post, name='create_post'),
    path('posts/', views.view_posts, name='veiw_posts'),
    path('posts/filtering/', views.PlaceList.as_view(), name="filtered_pos"),
    # path('moderating-posts', views.view_moderating-posts, name='veiw_posts'),
    path('post/update/<int:pk>/', views.update_post, name='update-items'),
    path('post/comment/<int:pk>/', views.view_comments, name='comments_for_post'),
    path('comment/update/<int:pk>/', views.update_comment, name='update-items'),
]