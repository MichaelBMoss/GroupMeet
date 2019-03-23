from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
import main.views
from main.views import IndexPageView, ChangeLanguageView, questions_page, search_page, questions_error

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexPageView.as_view(), name='index'),

    path('i18n/', include('django.conf.urls.i18n')),
    path('language/', ChangeLanguageView.as_view(), name='change_language'),

    path('accounts/', include('accounts.urls')),
    path('questions', main.views.questions_page),
    path('search', main.views.search_page),
    path('questions_error', main.views.questions_error),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
