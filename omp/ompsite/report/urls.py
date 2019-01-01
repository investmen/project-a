from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('evaluator/<evaluator_id>/', views.evaluator_detail, name = 'evaluator_detail'),
    path('evaluator/list/', views.list_evaluator, name='evaluator_list'),
    path('evaluator/create/', views.create_evaluator, name='evaluator_create'),
]