"""searching_top URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from searching_app.views import (send_form, contacts_view, result_seo, result_student,
                                 about_view, result_view, exportdate, export_csv, export_xls)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^contacts/', contacts_view),
    url(r'^result_boss/', result_view),
    url(r'^about/', about_view),
    url(r'^$', send_form, name='form'),
    url(r'^result_seo/', result_seo),
    url(r'^result_student/', result_student),
    url(r'^exportdate/', exportdate),
    url(r'^xls_formats/', export_xls),
    url(r'^csv_formats/', export_csv)
]
