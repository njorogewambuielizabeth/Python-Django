from django.shortcuts import get_object_or_404, render, redirect
from .forms import PaymentForm
from .models import Payment
# Create your views here.


def create_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm()
    return render(request, 'payments/create_payments.html', {'form': form})



def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payments/payment_list.html', {'payments': payments})


def edit_payment(request, id):
    payment = Payment.objects.get(id=id)
    if request.method == "POST":
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
        return redirect('payment_detail_view', id=id)
    else:
        form = PaymentForm(instance=payment)
    return render(request, "payments/edit_payment.html", {"form": form})



def payment_details(request, id):
    product = Payment.objects.get(id=id)
    return render(request, "payments/payment_detail.html",{"product": product})