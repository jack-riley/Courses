from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('<int:id>/delete', views.delete),
    path('<int:id>/process_delete', views.process_delete),
    path('process_new_course', views.process_new_course),
    path('<int:id>', views.comment),
    path('<int:id>/comment', views.process_comment)

]