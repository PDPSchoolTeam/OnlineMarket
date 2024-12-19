from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView
from .models.category import Category
from django.shortcuts import redirect
from django.contrib.auth.hashers import check_password
from .models.customers import Customer
from django.views import View
from .models.products import Product
from .models.orders import Order
from django.contrib.auth.hashers import make_password

class StoreView(View):
    def get(self, request):
        # Handle the cart session
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')

        if categoryID:
            products = Product.get_all_products_by_category_id(categoryID)
        else:
            products = Product.get_all_products()

        # Prepare the context for the template
        context = {
            'products': products,
            'categories': categories,
        }

        return render(request, 'index.html', context)


class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')

        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        return redirect('homepage')

    def get(self, request):
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')


class Cart(ListView):
    template_name = 'cart.html'
    context_object_name = 'products'

    def get_queryset(self):
        cart_ids = list(self.request.session.get('cart', {}).keys())
        if not cart_ids:
            return Product.objects.none()
        return Product.get_products_by_id(cart_ids)





class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        delivery = request.POST.get('delivery')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))

        for product in products:
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          delivery=delivery,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}

        return redirect('orders')


class OrderView(View):


    def get(self , request ):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        return render(request , 'orders.html'  , {'orders' : orders})


class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get ('return_url')
        return render (request, 'login.html')

    def post(self, request):
        email = request.POST.get ('email')
        password = request.POST.get ('password')
        customer = Customer.get_customer_by_email (email)
        error_message = None
        if customer:
            flag = check_password (password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Login.return_url:
                    return HttpResponseRedirect (Login.return_url)
                else:
                    Login.return_url = None
                    return redirect ('homepage')
            else:
                error_message = "Email yoki parol noto'g'ri"
        else:
            error_message = "Email yoki parol noto'g'ri"

        return render (request, 'login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')


class Signup (View):
    def get(self, request):
        return render (request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get ('firstname')
        last_name = postData.get ('lastname')
        phone = postData.get ('phone')
        email = postData.get ('email')
        password = postData.get ('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer (first_name=first_name,
                             last_name=last_name,
                             phone=phone,
                             email=email,
                             password=password)
        error_message = self.validateCustomer (customer)

        if not error_message:
            customer.password = make_password (customer.password)
            customer.register ()
            return redirect ('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render (request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if (not customer.first_name):
            error_message = "Ismingizni kiriting"
        elif len (customer.first_name) < 3:
            error_message = "Ism haqiqyga o'xshamayabdi kamida 4 ta harfdan ko'p bo'lishi kerak"
        elif not customer.last_name:
            error_message = "Familiyangizni kiriting"
        elif len (customer.last_name) < 3:
            error_message = "Familiya haqiqyga o'xshamayabdi kamida 4 ta harfdan ko'p bo'lishi kerak"
        elif not customer.phone:
            error_message = "Telefon raqamingizni kiriting"
        elif len (customer.phone) < 9:
            error_message = "Telefon raqam kamida 9 ta raqamdan iborat bo'ladi !"
        elif len (customer.password) < 5:
            error_message = "Parolingiz eng kamida 5 ta belgidan iborat bo'lsin"
        elif customer.isExists ():
            error_message = 'Bu email allaqachon ishlatilgan..'

        return error_message
