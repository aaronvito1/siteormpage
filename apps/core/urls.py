from django.urls import path
# from apps import views
from apps.core import views
from django.contrib import admin

urlpatterns = [
    # path('', views.home, name='home'),
    # path('about/', views.about, name='about'),
	path('', views.index, name="home"),
	path('about/', views.about, name="about"),
	path('extra/', views.extra, name="extra"),
	path('portfolio/', views.portfolio, name="portfolio"),
	path('blog/', views.blog, name="blog"),
	path('contact/', views.contact, name="contact"),
    path('admin/', admin.site.urls),
]

# Boilerplate to include static files
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)