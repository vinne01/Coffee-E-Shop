from django.shortcuts import render
import razorpay
from .models import Coffee
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Price mapping for coffee types
COFFEE_PRICES = {
    'indian': 100,
    'russian': 150,
    'american': 200
}

# Create your views here
def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        coffee_type = request.POST.get("coffee_type")
        quantity = int(request.POST.get("quantity"))
        
        # Get the price per coffee from the COFFEE_PRICES dictionary
        price_per_coffee = COFFEE_PRICES.get(coffee_type, 100)  # Default to 100 if type is not found

        # Calculate the total amount (in paise)
        amount = price_per_coffee * quantity * 100  # Amount is in paise (1 INR = 100 paise)

        # Create a Razorpay client
        client = razorpay.Client(auth=("rzp_test_kW8rMFTvHKTTSU", "QMeAga0CCVDybdDKhNvd3cc0"))
        payment = client.order.create({
            'amount': amount,
            'currency': 'INR',
            'payment_capture': '1'
        })
        
        # Save the order to the database
        coffee = Coffee(name=name, email=email,coffee_type=coffee_type,quantity=quantity, amount=amount, payment_id=payment['id'])
        coffee.save()

        # Render the page with payment details
        return render(request, "index.html", {
            'payment': payment, 
            'name': name, 
            'email': email
        })
        
    return render(request, "index.html")


@csrf_exempt
def success(request):
    if request.method == "POST":
        a = request.POST
        order_id = ""
        
        for key, val in a.items():
            if key == "razorpay_order_id":
                order_id = val
                break
        
        # Find the user who made the payment
        user = Coffee.objects.filter(payment_id=order_id).first()
        if user:
            user.paid = True
            user.save()

            # Send confirmation email
            # persons=user.amount/100
            msg_plain = render_to_string('email.txt', {'name': user.name, 'coffee_type': user.coffee_type, 'quantity': user.quantity,'amount':user.amount})
            msg_html = render_to_string('email.html', {'name': user.name, 'coffee_type': user.coffee_type, 'quantity': user.quantity,'amount':user.amount})
            
            send_mail("Your Order of Coffee has been Confirmed", msg_plain, settings.EMAIL_HOST_USER, [user.email], html_message=msg_html)
            
    return render(request, "success.html")


def menu(request):
    return render(request,'menu.html')
