from django.conf.urls import url
from pmptwo import views

urlpatterns = [
    url(r'^$',views.help ,name='help')
]