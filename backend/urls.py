from django.contrib.auth import admin
from django.urls import path, include, re_path as url
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include('accounts.urls')),
    path('files/', include('userfiles.urls')),
    path('red/', include('redirects.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += [
#     url(r'^.*', TemplateView.as_view(template_name='index.html'))
# ]

##activation link demo:
#http://127.0.0.1:8000/#/activate/MTE/b71ute-e00c6d5571024948a4f48badc9cf6410