from django import forms
from django.core.exceptions import ValidationError
from .models import Customer, TableCategory, Table, ReservationStatus, Reservation, Payment

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone']

class TableCategoryForm(forms.ModelForm):
    class Meta:
        model = TableCategory
        fields = ['name', 'description']

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['table_number', 'category', 'capacity', 'location', 'is_active']

class ReservationStatusForm(forms.ModelForm):
    class Meta:
        model = ReservationStatus
        fields = ['name', 'description', 'is_active']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['customer', 'table', 'reservation_date', 'start_time', 'end_time', 'guests', 'status', 'notes']
        widgets = {
            'reservation_date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
            'guests': forms.NumberInput(attrs={'min': '1'})
        }

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        guests = cleaned_data.get('guests')
        table = cleaned_data.get('table')

        # Validate that the number of guests is positive
        if guests is not None and guests <= 0:
            self.add_error('guests', "The number of guests must be positive.")

        # Validate that the reservation end time is later than the start time
        if start_time and end_time and end_time <= start_time:
            self.add_error('end_time', "End time must be strictly after the start time.")

        # Validate that a selected table can accommodate the specified number of guests
        if guests and table and guests > table.capacity:
            self.add_error('guests', f"The selected table can only accommodate up to {table.capacity} guests.")

        return cleaned_data

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['reservation', 'amount', 'payment_method', 'payment_status', 'transaction_ref', 'paid_at']
        widgets = {
            'paid_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }