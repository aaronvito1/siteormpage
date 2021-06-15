from django.urls import path

from apps.accounts import views

from django.urls import path
# from djangoapp import views
from apps.core import views
from django.contrib import admin

urlpatterns = [
    # path('login/', views.log_in, name='login'),
    # path('signup/', views.sign_up, name='signup'),
    # path('logout/', views.logout_view, name='logout'),
    # path('edit-profile/', views.edit_profile, name='edit_profile'),
    # path('users/', views.view_all_users, name='view_all_users'),
    # path('users/<username>/', views.view_profile, name='view_profile'),
]


# Boilerplate to include static files
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)