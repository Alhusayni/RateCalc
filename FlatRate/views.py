from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from FlatRate.forms import CalcForm
from .models import News
from django.views.generic import ListView


# Create your views here.
def home(request):
    info = False
    form = CalcForm()

    if request.method == 'POST':
        form = CalcForm(request.POST)
        if form.is_valid():
            form.save()
            info = True
            price = form.cleaned_data['Price']
            salary = form.cleaned_data['Salary']
            years = form.cleaned_data['Years']
            isSupported = form.cleaned_data['isSupported']
            downPay = form.cleaned_data['DownPay']
            intrstRate = form.cleaned_data['IntrestRate']
            # # check supported or not
            if isSupported == 'Yes':
                if salary <= 10000:
                    support = 150000
                else:
                    support = 100000
            else:
                support = 0
            newPrice = price - support - downPay
            intrstPrice = (newPrice * (intrstRate / 100)) * years
            totalPrice = newPrice + intrstPrice
            estatePrice = price + intrstPrice
            monthlyPay = (totalPrice / years) / 12
            diff = (monthlyPay / salary) * 100

    if info == True:
        context = {'form': form, 'info': info, 'monthlyPay': monthlyPay, 'totalPrice': totalPrice,
                   'intrstPrice': intrstPrice, 'newPrice': newPrice, 'support': support, 'diff': diff,
                   'estatePrice': estatePrice}
        return render(request, 'home.html', context)
    else:
        context = {'form': form}
        return render(request, 'home.html', context)


def policy(request):
    return render(request, 'policy.html')


def about(request):
    return render(request, 'about.html')

def news(request):
    posts = News.objects.all().order_by('-created')
    context = {'posts': posts}
    return render(request, 'news.html', context)


def contact(request):
    return render(request, 'contact.html')


class NewsList(ListView):
    model = News
    template_name = 'news.html'
    context_object_name = 'posts'
    ordering = '-created'
    paginate_by = 3