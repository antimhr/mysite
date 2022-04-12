

from django.contrib import admin
from django.urls import include, path
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('blog/', include('blog.urls')),
    path('pages/', include('pages.urls'))
]
