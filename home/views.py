from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting, ContactForm


def index(request):
    setting=Setting.objects.get(pk=1)
    #context buraya yükleyeceğimiz veriler ürün listesi kategori listesi vs
    context = {'setting': setting, 'page':'home'}
    return render(request, 'index.html', context)
def hakkimizda(request):
    setting=Setting.objects.get(pk=1)
    #context buraya yükleyeceğimiz veriler ürün listesi kategori listesi vs
    context = {'setting': setting, 'page':'hakkimizda'}
    return render(request, 'hakkimizda.html', context)

def referanslar(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'referanslar.html', context)

def iletisim(request):
    setting=Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'iletisim.html', context)


    """form=ContactForm(request.POST)
    if form.is_valid():
        data=ContactForm() #model ile bağlantı kur
        data.name=form.clean_data['name']  #formdan bilgiyi al
        data.email = form.clean_data['email']
        data.subject = form.clean_data['subject']
        data.message = form.clean_data['message']
        data.save() #veritabanına kaydet
        messages.success(request,'Mesajınız başarıyla gönderilmiştir. Teşekkür ederiz...')
        return HttpResponseRedirect('/iletisim')


    form=ContactForm()
    context={'setting':setting, 'form': form}
    return render(request, 'iletisim.html', context)"""