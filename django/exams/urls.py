from django.urls import path

from exams import views


app_name = 'exams'
urlpatterns = [
    path("list/", views.ExamListView.as_view(), name="list"),
    path("create/", views.ExamCreateView.as_view(), name="create"),
    path("update/<uuid:pk>", views.ExamUpdateView.as_view(), name="update")
]
