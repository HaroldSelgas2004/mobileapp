from django.urls import path
from . import views

app_name = 'reservation_app'

urlpatterns = [
    # Customer URLs
    path('customers/', views.CustomerListView.as_view(), name='customer_list'),
    path('customers/add/', views.CustomerCreateView.as_view(), name='customer_add'),
    path('customers/<int:pk>/', views.CustomerDetailView.as_view(), name='customer_detail'),
    path('customers/<int:pk>/edit/', views.CustomerUpdateView.as_view(), name='customer_edit'),
    path('customers/<int:pk>/delete/', views.CustomerDeleteView.as_view(), name='customer_delete'),

    # Table Category URLs
    path('table-categories/', views.TableCategoryListView.as_view(), name='table_category_list'),
    path('table-categories/add/', views.TableCategoryCreateView.as_view(), name='table_category_add'),
    path('table-categories/<int:pk>/', views.TableCategoryDetailView.as_view(), name='table_category_detail'),
    path('table-categories/<int:pk>/edit/', views.TableCategoryUpdateView.as_view(), name='table_category_edit'),
    path('table-categories/<int:pk>/delete/', views.TableCategoryDeleteView.as_view(), name='table_category_delete'),

    # Table URLs
    path('tables/', views.TableListView.as_view(), name='table_list'),
    path('tables/add/', views.TableCreateView.as_view(), name='table_add'),
    path('tables/<int:pk>/', views.TableDetailView.as_view(), name='table_detail'),
    path('tables/<int:pk>/edit/', views.TableUpdateView.as_view(), name='table_edit'),
    path('tables/<int:pk>/delete/', views.TableDeleteView.as_view(), name='table_delete'),

    # Reservation Status URLs
    path('reservation-statuses/', views.ReservationStatusListView.as_view(), name='reservation_status_list'),
    path('reservation-statuses/add/', views.ReservationStatusCreateView.as_view(), name='reservation_status_add'),
    path('reservation-statuses/<int:pk>/edit/', views.ReservationStatusUpdateView.as_view(), name='reservation_status_edit'),
    path('reservation-statuses/<int:pk>/delete/', views.ReservationStatusDeleteView.as_view(), name='reservation_status_delete'),

    # Reservation URLs
    path('reservations/', views.ReservationListView.as_view(), name='reservation_list'),
    path('reservations/add/', views.ReservationCreateView.as_view(), name='reservation_add'),
    path('reservations/<int:pk>/', views.ReservationDetailView.as_view(), name='reservation_detail'),
    path('reservations/<int:pk>/edit/', views.ReservationUpdateView.as_view(), name='reservation_edit'),
    path('reservations/<int:pk>/cancel/', views.ReservationDeleteView.as_view(), name='reservation_cancel'),

    # Payment URLs
    path('payments/', views.PaymentListView.as_view(), name='payment_list'),
    path('payments/add/', views.PaymentCreateView.as_view(), name='payment_add'),
    path('payments/<int:pk>/', views.PaymentDetailView.as_view(), name='payment_detail'),
    path('payments/<int:pk>/edit/', views.PaymentUpdateView.as_view(), name='payment_edit'),

    # Audit Log URLs
    path('audit-logs/', views.AuditLogListView.as_view(), name='audit_log_list'),
    path('audit-logs/<int:pk>/', views.AuditLogDetailView.as_view(), name='audit_log_detail'),

]