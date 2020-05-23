import json

from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.forms import SearchForm, SignUpForm
from home.models import Setting, ContactFormMessage, ContactFormu
from product.models import Product, Category, Images, Comment


def index(request):
    setting=Setting.objects.get(pk=1)
    sliderdata=Product.objects.all()[:4]
    category=Category.objects.all()
    dayimages=Product.objects.all()
    lastimages = Product.objects.all().order_by('-id')[:4]
    randimages = Product.objects.all().order_by('?')[:4]
    #context buraya yükleyeceğimiz veriler ürün listesi kategori listesi vs
    context = {'setting': setting,
               'category': category,
               'page':'home',
               'sliderdata':sliderdata,
               'dayimages':dayimages,
               'lastimages': lastimages,
               'randimages': randimages,
               }
    return render(request, 'index.html', context)
def hakkimizda(request):
    setting=Setting.objects.get(pk=1)
    category = Category.objects.all()
    sliderdata = Product.objects.all()[:4]
    #context buraya yükleyeceğimiz veriler ürün listesi kategori listesi vs
    context = {'setting': setting,
               'page':'hakkimizda',
               'sliderdata':sliderdata,
               'category': category}
    return render(request, 'hakkimizda.html', context)

def referanslar(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    sliderdata = Product.objects.all()[:4]
    context = {'setting': setting,
               'category': category,
               'sliderdata':sliderdata}
    return render(request, 'referanslar.html', context)

def iletisim(request):

    if request.method == 'POST':
        form=ContactFormu(request.POST)
        if form.is_valid():
            data=ContactFormMessage() #model ile bağlantı kur
            data.name=form.cleaned_data['name']  #formdan bilgiyi al
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip=request.META.get('REMOTE_ADDR')
            data.save() #veritabanına kaydet
            messages.success(request,'Mesajınız başarıyla gönderilmiştir. Teşekkür ederiz...')
            return HttpResponseRedirect('/iletisim')

    setting = Setting.objects.get(pk=1)
    form=ContactFormu()
    category = Category.objects.all()
    sliderdata = Product.objects.all()[:4]
    context={'setting':setting,
             'form': form,
             'sliderdata': sliderdata,
             'category': category}
    return render(request, 'iletisim.html', context)

def category_galery(request,id,slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    pictures=Product.objects.filter(category_id=id)
    sliderdata = Product.objects.all()[:4]
    context={'pictures':pictures,
             'category': category,
             'sliderdata': sliderdata,
             'categorydata':categorydata,
             'slug':slug}
    return render(request, 'galery.html',context)

def pictures_detail(request,id,slug):
    category = Category.objects.all()
    pictures = Product.objects.get(pk=id)
    images=Images.objects.filter(product_id=id)
    comment = Comment.objects.filter(pictures_id=id, status='True')
    context={'pictures':pictures,
             'category': category,
             'images':images,
             'comment': comment}
    return render(request, 'pictures_detail.html',context)

def pictures_search(request):
    if request.method=='POST':
        form= SearchForm(request.POST)
        if form.is_valid():
            category=Category.objects.all()

            query=form.cleaned_data['query']
            catid = form.cleaned_data['catid']
            if catid == 0:
                pictures = Product.objects.filter(title__icontains=query)
            else:
                pictures = Product.objects.filter(title__icontains=query, category_id=catid)



            context= {'pictures': pictures,
                      'category': category,
                      }
            return render(request,'pictures_search.html',context)
    return HttpResponseRedirect('/')

def pictures_search_auto(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    picture = Product.objects.filter(title__icontains=q)
    results = []
    for rs in picture:
      picture_json = {}
      picture_json = rs.title
      results.append(picture_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Login Hatası ! Kullanıcı adı yada şifre yanlış ")
            return HttpResponseRedirect('/login')
    category = Category.objects.all()
    context = {'category': category,
               }
    return render(request,'login.html',context)

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            return HttpResponseRedirect('/')

    form = SignUpForm()
    category = Category.objects.all()
    context = {'category': category,
                'form': form,
               }

    return render(request, 'signup.html', context)