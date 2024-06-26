from django.urls import path

from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', ChoperHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add_page/', AddPage.as_view(), name='add_page'),
    path('contacts/', ContactFormView.as_view(), name='contacts'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', ChoperCategory.as_view(), name='category'),


]
