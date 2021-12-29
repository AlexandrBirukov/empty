from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/empty/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),

    # robots.txt
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
]

urlpatterns += i18n_patterns(
    # TODO: сюда урлы приложений
)

handler404 = 'project.utils.error_views.error_404'
handler500 = 'project.utils.error_views.error_500'
handler403 = 'project.utils.error_views.error_403'

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
                       path('__debug__/', include(debug_toolbar.urls)),
                   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
