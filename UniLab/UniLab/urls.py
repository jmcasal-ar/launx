"""UniLab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from courses.urls import courses_patterns
from news.urls import news_patterns
from pages.urls import pages_patterns
from django.conf import settings

urlpatterns = [
    #Paths del core
    path('', include('core.urls')),
    #Path del administrador
    path('admin/', admin.site.urls),
    # Path de courses
    path('courses/', include(courses_patterns)),
    # Path de news
    path('news/', include(news_patterns)),
    # Path de pages
    path('pages/', include(pages_patterns)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)