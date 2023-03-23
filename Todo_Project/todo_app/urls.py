
from . import views
from django.urls import path

app_name='todo_app'

urlpatterns = [
    path('', views.home,name='Home'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    # ************class path**************************
    path('cvbhome/',views.TaskListView.as_view(),name='cvbhome'),
    path('cvbdetail/<int:pk>/',views.TaskDetailView.as_view(),name='cvbdetail'),
    path('cvbupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='cvbupdate'),
    path('cvbdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cvbdelete'),

]