from django.urls import path

from axis import views

app_name = 'axis'
urlpatterns = [
    path("list/", views.AxleListView.as_view(), name="list")
]
