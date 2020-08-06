from django.urls import path
from . import views
urlpatterns = [
    path('todos/', views.TodoView.as_view(), name="get_request"),
    path('todos/<pk>', views.give_data_of_this_id, name="get_one_request"),
    path('add-todos/', views.create_todo.as_view(), name="post_request" ),
]
