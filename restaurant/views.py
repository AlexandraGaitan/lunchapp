from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Menu, ORDER_SHIPPING, ORDER_PROCESSING
from .forms import MenuForm, OrderForm
from django.shortcuts import render
from django.contrib import messages 
from restaurant.models import Menu, Order
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from restaurant.serializers import MenuSerializer, OrderSerializer
from datetime import datetime, timedelta
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError


# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework import status




def index(request):
    all_menus=Menu.objects.all().order_by('-date_day')
    template=loader.get_template('restaurant/menu_list.html')
    context={
        "all_menus":all_menus,
    }
    return HttpResponse(template.render(context, request))

def detail(request, menu_id):
    #import ipdb; ipdb.set_trace();
    menu=Menu.objects.get(pk=menu_id)
    order_list=Order.objects.filter(title__pk=menu_id)
    template=loader.get_template('restaurant/view_menu.html')
    total=0;
    count=0;
    average=0;
    context={
        "menu":menu,
        "order_list":order_list
    }

    for order in order_list:
        if order.raiting !=0:
            total+=order.raiting
            count+=1
    try:
        average=total/count
    except:
        average=0
    context={
        "menu":menu,
        "order_list":order_list,
        "average":average
}
    return HttpResponse(template.render(context, request))

def index_o(request):
    all_orders=Order.objects.all()
    template=loader.get_template('restaurant/order_list.html')

    context={
        "all_orders":all_orders,
    }
    return HttpResponse(template.render(context, request))

def detail_o(request, order_id):
    #import ipdb; ipdb.set_trace();
    order=Order.objects.get(pk=order_id)
    template=loader.get_template('restaurant/view_order.html')
    context={
        "order":order,
    }
    return HttpResponse(template.render(context, request))

def index_t(request):
    all_menus=Menu.objects.filter(date_day__lte=datetime.now() + timedelta(days=1), date_day__gte=datetime.now() - timedelta(days=1))
    template=loader.get_template('restaurant/todays_menu.html')
    context={
        "all_menus":all_menus,
    }
    return HttpResponse(template.render(context, request))

def post_new(request):
    if request.method == 'GET':
        form = MenuForm()
    elif request.method == 'POST':
        form = MenuForm(data=request.POST)
        # import ipdb; ipdb.set_trace();
        if form.is_valid():
            form.save()
            messages.succes(request, "Comanda a fost adaugata cu succes!")
        else:
            # pass
            messages.error(request, "Nu ati completat corect!")
    return render(request, 'restaurant/post_edit.html', {'form': form})


    # class MenuViewSet(viewsets.ModelViewSet):
    #     # import ipdb; ipdb.set_trace();
    #     queryset = Menu.objects.filter(date_day=datetime.today().date())

    #     serializer_class = MenuSerializer


    # class OrderViewSet(viewsets.ModelViewSet):
    #     queryset = Order.objects.all()
    #     serializer_class = OrderSerializer




def change(request, order_id):
    u = Order.objects.get(pk=order_id)
    if u.status == ORDER_PROCESSING:
        u.status=ORDER_SHIPPING
        u.save()
        messages.success(request, "OK")
    else:
        messages.error(request, "Nu se poate ")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# sandru
def post_order(request):
    
    if request.method == 'GET':
        form = OrderForm()
    elif request.method == 'POST':
        orders = Order.objects.all()
        #data = request.data
        form = OrderForm(data=request.POST) 
        if form.is_valid():
            # import  ipdb; ipdb.set_trace();
            order = form.save()

            send_m(order)
        else:
            # pass
            messages.error(request, "Error la scriere")
    return render(request, 'restaurant/post_order.html', {'form': form})

@api_view(['GET', 'POST'])
def MenuViewSet(request):
    if request.method == 'GET':
        menus = Menu.objects.filter(date_day=datetime.today().date())
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def OrderViewSet(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order=serializer.save()
            # import ipdb; ipdb.set_trace();
            send_m (order)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




def send_m(order):

    subject = "Order confirmation"  
    msg = "Va multumim pentru comanda facuta " + order.name + ". Ati comandat urmatorul meniu :" + order.title.title + " si contine: Felul 1 - " + order.title.dish1 + ", Felul 2 - " + order.title.dish2 +", Desert - " + order.title.desert + ". Numarul dvs de comanda este :" + str(order.title.pk) +"-" + str(order.pk)
    send_mail(subject, msg, "testlunch72@gmail.com", [order.email])