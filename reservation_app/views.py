from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Customer, TableCategory, Table, ReservationStatus, Reservation, Payment, AuditLog
from .forms import CustomerForm, TableCategoryForm, TableForm, ReservationStatusForm, ReservationForm, PaymentForm


# --- CUSTOMER VIEWS ---
class CustomerListView(ListView):
    model = Customer

class CustomerDetailView(DetailView):
    model = Customer

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('reservation_app:customer_list')

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('reservation_app:customer_list')

class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('reservation_app:customer_list')

# --- TABLE CATEGORY VIEWS ---
class TableCategoryListView(ListView):
    model = TableCategory

class TableCategoryDetailView(DetailView):
    model = TableCategory

class TableCategoryCreateView(CreateView):
    model = TableCategory
    form_class = TableCategoryForm
    success_url = reverse_lazy('reservation_app:table_category_list')

class TableCategoryUpdateView(UpdateView):
    model = TableCategory
    form_class = TableCategoryForm
    success_url = reverse_lazy('reservation_app:table_category_list')

class TableCategoryDeleteView(DeleteView):
    model = TableCategory
    success_url = reverse_lazy('reservation_app:table_category_list')

# --- TABLE VIEWS ---
class TableListView(ListView):
    model = Table

class TableDetailView(DetailView):
    model = Table

class TableCreateView(CreateView):
    model = Table
    form_class = TableForm
    success_url = reverse_lazy('reservation_app:table_list')

class TableUpdateView(UpdateView):
    model = Table
    form_class = TableForm
    success_url = reverse_lazy('reservation_app:table_list')

class TableDeleteView(DeleteView):
    model = Table
    success_url = reverse_lazy('reservation_app:table_list')

# --- RESERVATION STATUS VIEWS ---
class ReservationStatusListView(ListView):
    model = ReservationStatus

class ReservationStatusCreateView(CreateView):
    model = ReservationStatus
    form_class = ReservationStatusForm
    success_url = reverse_lazy('reservation_app:reservation_status_list')

class ReservationStatusUpdateView(UpdateView):
    model = ReservationStatus
    form_class = ReservationStatusForm
    success_url = reverse_lazy('reservation_app:reservation_status_list')

class ReservationStatusDeleteView(DeleteView):
    model = ReservationStatus
    success_url = reverse_lazy('reservation_app:reservation_status_list')

# --- RESERVATION VIEWS ---
class ReservationListView(ListView):
    model = Reservation
    
    def get_queryset(self):
        # Provide filtering capabilities by customer or date
        queryset = super().get_queryset()
        customer_id = self.request.GET.get('customer')
        res_date = self.request.GET.get('date')
        if customer_id:
            queryset = queryset.filter(customer_id=customer_id)
        if res_date:
            queryset = queryset.filter(reservation_date=res_date)
        return queryset

class ReservationDetailView(DetailView):
    model = Reservation

class ReservationCreateView(CreateView):
    model = Reservation
    form_class = ReservationForm
    success_url = reverse_lazy('reservation_app:reservation_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Create an audit record programmatically
        AuditLog.objects.create(
            reservation=self.object,
            action="CREATED",
            performed_by="System" # In a real app, use self.request.user.username
        )
        return response

class ReservationUpdateView(UpdateView):
    model = Reservation
    form_class = ReservationForm
    success_url = reverse_lazy('reservation_app:reservation_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        AuditLog.objects.create(
            reservation=self.object,
            action="UPDATED",
            performed_by="System"
        )
        return response

class ReservationDeleteView(DeleteView):
    # Requirement specified "Delete/Cancel View"
    model = Reservation
    success_url = reverse_lazy('reservation_app:reservation_list')
    
    def form_valid(self, form):
        AuditLog.objects.create(
            reservation=self.object,
            action="DELETED/CANCELLED",
            performed_by="System"
        )
        return super().form_valid(form)

# --- PAYMENT VIEWS ---
class PaymentListView(ListView):
    model = Payment

class PaymentDetailView(DetailView):
    model = Payment

class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentForm
    success_url = reverse_lazy('reservation_app:payment_list')

class PaymentUpdateView(UpdateView):
    model = Payment
    form_class = PaymentForm
    success_url = reverse_lazy('reservation_app:payment_list')

# --- AUDIT LOG VIEWS ---
class AuditLogListView(ListView):
    model = AuditLog
    
    def get_queryset(self):
        # Allow audit logs to be filtered by reservation
        queryset = super().get_queryset()
        reservation_id = self.request.GET.get('reservation')
        if reservation_id:
            queryset = queryset.filter(reservation_id=reservation_id)
        return queryset

class AuditLogDetailView(DetailView):
    model = AuditLog


