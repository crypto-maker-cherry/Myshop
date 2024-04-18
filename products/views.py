from django.shortcuts import render
from django.http import HttpResponse
from . models import product,Brand,Feedback
from django.contrib import messages
from django.views import View

from . forms import FeedbackForm
# Create your views here.
class IndexView(View):
    def get(self, request):
        user="tom"
        product_numb="4"
        products=product.objects.all().order_by('-id')[:4]
        return render(request,"products/home.html",{
            "name":user,"number":product_numb,
            "products":products,
        })
    def post(self, request):
        pass
        
'''def index(request):
    user="tom"
    product_numb="4"
    products=product.objects.all().order_by('-id')[:4]
    return render(request,"products/home.html",{
        "name":user,"number":product_numb,
        "products":products,
    })
'''
 
def signup(request):
    return render(request,"products/signup.html")

def product_cat(request,product):
    if(product == "suit" or product == "dress" or product == "shirt" or product == "shoes"):
        return HttpResponse(f"Here is the list of our {product}")
    else:
        return HttpResponse("The page you are looking for doesnt exist.")
    
class ProductPageView(View):
    def get(self, request, product_brand, product_slug):
        Product = product.objects.get(slug=product_slug)
        my_feedback = Feedback.objects.get(product = Product, id = 2)
        form = FeedbackForm(instance = my_feedback)
        reviews = Feedback.objects.filter(product = Product)

        return render(request, "products/product.html", {
        "product": Product,
        "form": form,
        "reviews" : reviews,
        })

    def Post(self, request, product_brand, product_slug):
        Product = product.objects.get(slug=product_slug)
        my_feedback = Feedback.objects.get(product = Product, id = 2)
        form = FeedbackForm(request.POST, instance = my_feedback)
        
        if form.is_valid():

            form.save()
            messages.success(request,"your feedback is submitted successfully.")
            
        
        return render(request, "products/product.html", {
        "product": Product,
       
        "form": form,
    })
    
'''def product_page(request,product_brand,product_slug):
    Product = product.objects.get(slug=product_slug)
    my_feedback = Feedback.objects.get(product = Product, id = 1)
    form = FeedbackForm(request.POST, instance = my_feedback)
    reviews = Feedback.objects.filter(product = Product)
    if request.method == "GET":
        return render(request, "products/product.html", {
        "product": Product,
        "form": form,
        "reviews" : reviews,
    })

    else:
        form = FeedbackForm(request.POST, instance = my_feedback)
        if form.is_valid():

            form.save()
            messages.success(request,"your feedback is submitted successfully.")
            
        
        return render(request, "products/product.html", {
        "product": Product,
       
        "form": form,
    })
    '''