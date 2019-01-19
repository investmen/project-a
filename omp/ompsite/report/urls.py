from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('evaluator/<int:evaluator_id>/', views.evaluator_update, name = 'evaluator_update'),
    path('evaluator/list/', views.list_evaluator, name='evaluator_list'),
    path('evaluator/create/', views.create_evaluator, name='evaluator_create'),
    path('evaluator/<int:evaluator_id>/payment_info/create/', views.payment_info_create, name='payment_info_create'),
    path('evaluator/<int:evaluator_id>/payment_info/<int:payment_info_id>/', views.payment_info_update, name = 'payment_info_update'),
    path('evaluator/<int:evaluator_id>/report_list/', views.evaluator_report_list, name='evaluator_report_list'),
    path('user/<int:user_id>/', views.user_detail, name = 'user_detail'),
    path('user/list/', views.user_list, name='user_list'),
    path('user/create/', views.user_create, name='user_create'),
    path('user/<int:user_id>/report_request_list/', views.user_report_request_list, name = 'user_report_request_list'),
    path('report/<int:report_id>/', views.report_update, name = 'report_update'),
    path('report/list/', views.report_list, name='report_list'),
    path('report/create/', views.report_create, name='report_create'),
    path('property/evaluator_search/', views.property_evaluator_search, name='property_evaluator_search'),
    path('property/<int:property_id>/report_create/', views.property_report_create, name='property_report_create'),
    path('property/search/', views.property_search, name='property_search'),
    path('property/<int:property_id>/report_list/', views.property_report_list, name='property_report_list'),
    path('property/<int:property_id>/report_request/<int:report_id>/', views.property_report_request, name='property_report_request'),
    path('report_request/<int:report_request_id>/<int:is_evaluator>/', views.report_request_update, name='report_request_update'),
    path('report_request/<int:report_request_id>/', views.report_request_update, name='report_request_update'),
    path('report_request/list/', views.report_request_list, name='report_request_list'),
    path('evaluator/<int:evaluator_id>/report_request_list/', views.evaluator_report_request_list, name = 'evaluator_report_request_list'),
    path('evaluator/<int:evaluator_id>/payment_info/create/', views.payment_info_create, name='payment_info_create'),
    path('evaluator/<int:evaluator_id>/payment_info/<int:payment_info_id>/', views.payment_info_update, name = 'payment_info_update'),
    path('evaluator/<int:evaluator_id>/dashboard/', views.evaluator_dashboard, name='evaluator_dashboard'),
    path('user/<int:user_id>/dashboard/', views.user_dashboard, name='user_dashboard'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
]