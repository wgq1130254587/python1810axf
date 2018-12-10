from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from app.models import Wheel, Nav, Mustbuy, Shop, MainShow, Foodtype, Goods


def home(request):

    wheels = Wheel.objects.all()
    navs = Nav.objects.all()
    mustbuys = Mustbuy.objects.all()
    shops = Shop.objects.all()
    shophead = shops[0]
    shoptabs = shops[1:3]
    shopclass = shops[3:7]
    shopcommends = shops[7:11]
    mainShows = MainShow.objects.all()


    data = {
        'wheels':wheels,
        'navs':navs,
        'mustbuys':mustbuys,
        'shophead':shophead,
        'shoptabs':shoptabs,
        'shopclass':shopclass,
        'shopcommends':shopcommends,
        'mainShows': mainShows
    }



    return render(request,'home/home.html',context=data)

def marketbase(request):
    return redirect('axf:market',104749)



def cart(request):
    return render(request,'cart/cart.html')
# 参数一:categoryid分类

def market(request,categoryid):

    #分类信息
    foodtypes = Foodtype.objects.all()

    # 商品信息
    goodslist = Goods.objects.filter(categoryid = categoryid)

    data = {
        'foodtypes':foodtypes,
        'goodslist':goodslist,
    }

    return render(request, 'market/market.html', context=data)


def mine(request):
    return render(request,'mine/mine.html')


