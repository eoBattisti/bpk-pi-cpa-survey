from django.urls import path

from axis import views

app_name = 'axis'
urlpatterns = [
    path("list/", views.AxleListView.as_view(), name="list"),
    path("create/", views.AxleCreateView.as_view(), name="create"),
    path("update/<uuid:pk>", views.AxleUpdateView.as_view(), name="update")
]
