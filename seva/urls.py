from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin
import seva.views
admin.autodiscover()


urlpatterns = patterns("",
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/signup/$", seva.views.SignupView.as_view(), name="account_signup"),
    url(r"^account/", include("account.urls")),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
