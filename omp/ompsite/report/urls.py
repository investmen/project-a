from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('evaluator/<int:evaluator_id>/', views.evaluator_detail, name = 'evaluator_detail'),
    path('evaluator/list/', views.list_evaluator, name='evaluator_list'),
    path('evaluator/create/', views.create_evaluator, name='evaluator_create'),
    path('user/<int:user_id>/', views.user_detail, name = 'user_detail'),
    path('user/list/', views.user_list, name='user_list'),
    path('user/create/', views.user_create, name='user_create'),
    path('report/<int:report_id>/', views.report_detail, name = 'report_detail'),
    path('report/list/', views.report_list, name='report_list'),
    path('report/create/', views.report_create, name='report_create'),
]