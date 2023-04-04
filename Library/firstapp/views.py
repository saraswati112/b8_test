from django.shortcuts import render, HttpResponse, redirect
from .models import Book
# Create your views here.

# transaction atomic

def home(request):
    if request.method == "POST":
        # print(request.POST)   # for car as well # csrf token generates along with post request, getting data filled in html chrome page # <QueryDict: {'csrfmiddlewaretoken': ['ZaHEyiuuq87uDlpy1KFZCwBHjOPhXtHecpaVGxbouW34eXndIMM6eRPoCvJSWpfG'], 'book_name': ['book3'], 'book_qty': ['26'], 'book_price': ['785'], 'book_author': ['pok'], 'book_is_pub': ['on']}>
        # print(request.POST.get("cars"))   # mercedes  -- for single value
        # print(request.POST.getlist("cars"))   # ['mercedes', 'audi'] (can select  multiple cars) -- for multiple values
        name = request.POST.get("book_name")
        qty = request.POST.get("book_qty")
        price = request.POST.get("book_price")
        author = request.POST.get("book_author")
        is_pub = request.POST.get("book_is_pub")
        # print(name, qty, price, author,  is_pub)  # book3 50 150 xyz Yes (getting single-single values as well. fill the details in chrome html page)
        if is_pub == "Yes":
            is_pub = True
        else:
            is_pub = False
        Book.objects.create(name=name, qty=qty, price=price, author=author, is_published=is_pub)
        return redirect("home_page")
        # return HttpResponse("Success")
    elif request.method == "GET":
        # print(request.GET)   # <QueryDict: {'surname': ['patil']}>  this is query  parameter hit in postman
        # return render(request, "home.html", context = {"person_names": ["ABC", "XYZ", "WXY"]}) # dynamic data(everytime changes data, you have to register these it in html as well, html page will shoe different output as we make changes in backend)
        # return render(request, "home.html", context = {"all_books": Book.objects.all()})  # sees books along with thier id, name, prices as defined in home.html
        return render(request, "home.html", context = {"person_name": "mohini"})
    
def show_books(request):
    return render(request, "show_books.html", {"all_books": Book.objects.all()})
    
def update_book(request, id):  # pk=1
    book_obj = Book.objects.get(id=id)
    return render(request, "home.html", context={"single_book": book_obj})
    
    
    
    
    
    
    
    