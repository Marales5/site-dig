
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', goods_list, name='goods_list_url'),
    path('digital_list/', GoodsView.as_view(), name='digital_list_url'),
    path('digital_list/<str:slug>/', GoodsDetail.as_view(), name='digital_detail_url'),
    path('login/', MyLoginUserView.as_view(), name='login_my'),

    path('advertisement/', advertisement, name='advertisement_url'),

    path('post/create', PostCreate.as_view(), name='post_create_url'),

    path('post_det/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('post_det/<str:slug>/update/', PostUpdate.as_view(), name='post_update_url'),
    path('post_det/<str:slug>/delete/', PostDelete.as_view(), name='post_delete_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/create', TagCreate.as_view(), name='tag_create_url'),

    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
    path('tag/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url'),

    path('general/', GoodsView.as_view(), name='goods_delete_url'),
    path('general/<str:slug>/details', TagDelete.as_view(), name='single_blog_url'),


]

