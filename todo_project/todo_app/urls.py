
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
      path('',views.task_view,name='task_view'),
      # path('task',views.task,name='task')
      path('delete/<int:taskid>/', views.delete,name='delete'),
      path('update/<int:id>/',views.update,name='update'),
      path('cbvtask/',views.Tasklistview.as_view(), name='cbvtask'),
      path('cbvdetail/<int:pk>/',views.Taskdetailview.as_view(),name='cbvdetail'),
      path('cbvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cbvdelete')
]