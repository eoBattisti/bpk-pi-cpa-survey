from django.urls import path

from questions import views

app_name = 'questions'
urlpatterns = [
    path("list/", views.QuestionsListView.as_view(), name="list"),
    path("create/", views.QuestionsCreateView.as_view(), name="create"),
    path("update/<uuid:pk>", views.QuestionsUpdateView.as_view(), name="update")
]
