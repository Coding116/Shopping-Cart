from django.shortcuts import render, redirect

# Create your views here.
cart = {
    'foods': [],
    'prices': [],
    'total': 0
}

def index(request):
    if request.method == 'POST':
        food = request.POST.get('food')
        price = request.POST.get('price')

        if food and price:
            try:
                price = float(price)
                cart['foods'].append(food)
                cart['prices'].append(price)
                cart['total'] += price
            except ValueError:
                pass  # You can handle invalid input better

        return redirect('index')  # Prevent form resubmission on reload

    return render(request, 'shoppingcart.html', cart)