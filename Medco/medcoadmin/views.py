from django.shortcuts import render
from django.contrib.auth import get_user_model
import datetime
from medco_com_bd.models import Status
# from .forms import Add_order
# Create your views here.
def dash_bd(request):
    st_pending= Status.objects.filter(status="pending").count()
    st_accepted= Status.objects.filter(status="accepted").count()
    st_prepairing= Status.objects.filter(status="prepairing").count()
    st_on_the_way= Status.objects.filter(status="on the way").count()
    st_delivered= Status.objects.filter(status="delivered").filter(order_date_no_time=datetime.date.today()).count()
    st_cancel= Status.objects.filter(status="cancel").filter(order_date_no_time=datetime.date.today()).count()
    # today sell
    st_sells= Status.objects.filter(status="delivered").filter(order_date_no_time=datetime.date.today())
    c=0
    for sell in st_sells:
        a=sell.product.unit_price
        c+=a
    st_sell_price=c
    st={"st_pending":st_pending,"st_accepted":st_accepted,"st_prepairing":st_prepairing,"st_on_the_way":st_on_the_way,"st_delivered":st_delivered,"st_cancel":st_cancel,"st_sell_price":st_sell_price}
    
    
    return render(request,"admin_app/dashbord.html",{"st":st})
def user(request):
    User = get_user_model()
    users = User.objects.all()
    st=Status.objects.all()
    return render(request, "admin_app/user.html",{"sta":st,"users":users})


def user_per(request):
    
    # User = get_user_model()
    # users = User.objects.all()

    
    
    return render(request, 'admin_app/test.html')


# Add order

def add_order(request):
    

    return render(request, "admin_app/add_order.html")

