from django.shortcuts import render,HttpResponseRedirect,HttpResponse,redirect
from django.views import View
from .models import Cart,Product,Status,Customer,UserOtp
from .forms import CustomerRegistrationForm,LoginForm,ChangePassword,CustomerProfile,Edit_Address
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login as login_auth
from django.contrib.auth import logout as logout_auth
from django.contrib.auth import update_session_auth_hash
import random
from Medco.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.db.models import Q
from django.http import JsonResponse
import datetime
from .database import Database




class home(View):
    def get(self,request):
        baby=Product.objects.filter(Catagory="BABY")[:5]
        female=Product.objects.filter(Catagory="FEMALE")[:5]
        male=Product.objects.filter(Catagory="MALE")[:5]
        adult=Product.objects.filter(Catagory="SEX")[:5]
        home="home"
        return render(request, 'app/index.html',{"fm":female,"bb":baby,"ml":male,"home":home,"ad":adult})

def product_detail(request,pk):
    pd=Product.objects.get(pk=pk)
    return render(request, 'app/productdetail.html',{"pd":pd})


def allmedicine(request,data=None):
    cat=["baby","female","male","sex"]
    if data ==None:
        btn="active"
        pd=Product.objects.all()
        return render(request, 'app/allmedicine.html',{"pd":pd,"btn":btn})
    else:
        if data in cat:
            pd=Product.objects.filter(Catagory=data.upper())
            if data == "baby":
                bb="active"
                bf="none"
                bm="none"
                bs="none"
            elif data == "female":
                bb="none"
                bf="active"
                bm="none"
                bs="none"
            elif data == "male":
                bb="none"
                bf="none"
                bm="active"
                bs="none"
            else:
                bb="none"
                bf="none"
                bm="none"
                bs="active"
            
            return render(request, 'app/allmedicine.html',{"pd":pd,"bb":bb,"bf":bf,"bm":bm,"bs":bs})
        
    
        
    




class customerregistration(View):
    
        def get(self,request):
            if request.user.is_authenticated:
                return HttpResponseRedirect("/")

            else:
                form=CustomerRegistrationForm()
                return render(request, 'app/customerregistration.html',{"fm":form})
        def post(self,request):
            get_otp = request.POST.get('otp')
            if get_otp:
                get_usr = request.POST.get('usr')
                # print(get_usr)
                usr = User.objects.get(username=get_usr)
                if int(get_otp) == UserOtp.objects.filter(user = usr).last().otp:
                    usr.is_active = True
                    usr.save()
                    messages.success(request, f'Account is Created For {usr.email}')
                    return redirect('login')
                else:
                    messages.warning(request, f'You Entered a Wrong OTP')
                    return render(request, 'app/customerregistration.html', {'otp': True, 'usr': usr})
            form=CustomerRegistrationForm(request.POST)
            if form.is_valid():
                number_us=form.cleaned_data["number"]
                address_us=form.cleaned_data["address"]
                city_us=form.cleaned_data["city"]
                first_name_usr=form.cleaned_data["first_name"]
                email_usr=form.cleaned_data["email"]
                form.save()
                usrname_usr=User.objects.get(email=email_usr)
                suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
                username_datefield = "_".join([first_name_usr, suffix])
                usrname_usr.username=username_datefield
                usrname_usr.save()
                cc=Customer(user=usrname_usr,name= first_name_usr,number= number_us,locality=address_us,city=city_us.capitalize())
                cc.save()

                email_usr = form.cleaned_data.get('email')
                    
                usr = User.objects.get(email=email_usr)
                usr.is_active =False
                usr.save()
                usr_otp = random.randint(100000, 999999)		    
                UserOtp.objects.create(user = usr, otp = usr_otp)
                mess = f"Hello {first_name_usr.capitalize()},\nYour OTP is {usr_otp}\nThanks!"

                send_mail(
                        "Welcome to Medco - Verify Your Email",
                        mess,
                        EMAIL_HOST_USER,
                        [usr.email],
                        fail_silently = False
                        )
                    
                    
                    
                return render(request, 'app/customerregistration.html',{'otp': True, 'usr': usr})
            else:
                return render(request, 'app/customerregistration.html',{"fm":form})
    

def add_to_cart(request):
    if request.user.is_authenticated:
        usr=request.user
        prod_id =request.GET["prod_id"]
        # print(prod_id)
        
        product_id=request.GET.get("prod_id")
        # print(product_id)
        product_name= Product.objects.get(id=product_id)
        try:
            c =Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        except:
            c=False
        if c:
            c.quantity+=1
            c.save()
            return redirect("/cart")
        else:
            crt=Cart(user=usr,product=product_name)
            crt.save()
            return redirect("/cart")
    else:
        return HttpResponseRedirect("/login/")


def show_cart(request):
    if request.user.is_authenticated:
        usr=request.user
        cart=Cart.objects.filter(user=usr)
        
        
        total_amount =0.0
        cartproduct=[crp for crp in cart]
        if cartproduct:
            for p in cartproduct:
                temp_amount=(p.quantity*p.product.unit_price)
                total_amount += temp_amount
        return render(request, 'app/carts.html',{"cart":cart,"tm":total_amount})
    else:
        return HttpResponseRedirect("/login/")
        







def buy_now(request):
 return render(request, 'app/buynow.html')




def address(request):
    if request.user.is_authenticated:
        btn="btn-primary"
        usr=request.user
        ad=Customer.objects.filter(user=usr)

        return render(request, 'app/address.html',{"btn":btn,"ad":ad})
    else:
        return HttpResponseRedirect("/login/")
# delete address
def delete_ad(request,id):
    if request.user.is_authenticated:
        usr=request.user
        ad=Customer.objects.filter(user=usr)
        ad_id=[d_id.id for d_id in ad]
        if id in ad_id:
            ad_del=Customer.objects.get(pk=id)
            ad_del.delete()
            return HttpResponseRedirect("/address/")
        else:
            return HttpResponseRedirect("/address/")
    else:
        return HttpResponseRedirect("/login/")

# edit address 
def edit_ad(request,pd):
    if request.user.is_authenticated:
        usr=request.user
        ad=Customer.objects.filter(user=usr)
        ad_id=[d_id.id for d_id in ad]
        if pd in ad_id:
            form=Edit_Address(request.POST)
            if form.is_valid():
                print("vslid")
                use=request.user
                name=form.cleaned_data["name"]
                number=form.cleaned_data["mobile"]
                address=form.cleaned_data["address"]
                city=form.cleaned_data["city"]
                ad_del=Customer(id=pd,user=use,name=name,number=number,locality=address,city=city)
                
                ad_del.save()
                
                # fs=Customer(user=use,name=name,number=number,locality=address,city=city)/////////////////////////////////////////////////
                # fs.save()
                messages.success(request,"congratulation! Profile update successful.")
                return HttpResponseRedirect("/profile/")
            else:
                # pi=Customer.objects.get(pk=pd)
                print("this is a get req")
                fm=Edit_Address()
                #customer_field_edit
                cs=Customer.objects.get(pk=pd)
                nm=cs.name
                mobile=cs.number
                ad=cs.locality
                ct=cs.city
                return render(request, 'app/profile.html',{"fm":fm,"edit":"edit","name":nm,"mobile":mobile,"ad":ad,"ct":ct})
        else:
            return HttpResponseRedirect("/address/")






def orders(request):
    if request.user.is_authenticated:
        usr=request.user
        st=Status.objects.filter(user=usr)
        return render(request, 'app/orders.html',{"sta":st})
    else:
        return HttpResponseRedirect("/login/")

def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
    
            form=ChangePassword(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                messages.success(request,"password changed successfully")
                return HttpResponseRedirect("/profile/")
        else:
            form=ChangePassword(user=request.user)
        return render(request, 'app/changepassword.html',{"fm":form})



    else:
        return HttpResponseRedirect("/login/")


    
def logout(request):
    logout_auth(request)
    return HttpResponseRedirect("/login/")

def login(request):
    
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        get_otp = request.POST.get('otp')
        if get_otp:
            get_usr = request.POST.get('usr')
            # print(get_usr)
            usr = User.objects.get(username=get_usr)
            if int(get_otp) == UserOtp.objects.filter(user = usr).last().otp:
                usr.is_active = True
                usr.save()
                messages.success(request, f'Account is Created For {usr.email}')
                return redirect('login')
            else:
                messages.warning(request, f'You Entered a Wrong OTP')
                return render(request, 'app/login.html', {'otp': True, 'usr': usr})

    
        if request.method == 'POST':
            form=LoginForm(request.POST)
            if form.is_valid():
                email=form.cleaned_data["email"]
                password=form.cleaned_data["password"]
                
                try:
                    log_cus=User.objects.get(email=email)
                    
                except:
                    log_cus=User.objects.filter(email=email)

                if log_cus:
                    
                    
                    if log_cus.is_active:
                        
                        flag=check_password(password,log_cus.password)
                        if flag:
                                
                                
                            login_auth(request,log_cus)
                                
                                
                                
                            return HttpResponseRedirect("/profile/")

                        else:
                            messages.warning(request, f'You Entered a Wrong Email and Password if you forget your password you can reset it! ')

                            return render(request, 'app/login.html',{"fm":form})
                    else:
                        
                        username = request.POST.get('email')
                        
                        usr = User.objects.get(email=email)
                        usr_otp = random.randint(100000, 999999)		    
                        UserOtp.objects.create(user = usr, otp = usr_otp)
                        mess = f"Hello {usr.first_name.capitalize()},\nYour OTP is {usr_otp}\nThanks!"

                        send_mail(
                                "Welcome to Medco - Verify Your Email",
                                mess,
                                EMAIL_HOST_USER,
                                [usr.email],
                                fail_silently = False
                            )
                    
                    
                    

                        return render(request,'app/login.html',{'otp': True, 'usr': usr})


                else:
                    messages.warning(request, f'You Entered a Wrong Email and Password if you forget your password you can reset it! ')

                    return render(request, 'app/login.html',{"fm":form})
                
            else:
                return render(request, 'app/login.html',{"fm":form})



        else:
            form=LoginForm()
            
            
            return render(request, 'app/login.html',{"fm":form})



def checkout(request):
    usr=request.user
    add =Customer.objects.filter(user=usr)
    cart_iteam = Cart.objects.filter(user=usr)
    total_amount =0.0
    cartproduct=[crp for crp in cart_iteam]
    if cartproduct:
        for p in cartproduct:
            temp_amount=(p.quantity*p.product.unit_price)
            total_amount += temp_amount

    return render(request, 'app/checkout.html',{"add":add,"ta":total_amount,"cart":cartproduct})



def resend_otp(request):
	if request.method == "GET":
		get_usr = request.GET['usr']
		if User.objects.filter(username = get_usr).exists() and not User.objects.get(username = get_usr).is_active:
			usr = User.objects.get(username=get_usr)
			usr_otp = random.randint(100000, 999999)
			UserOtp.objects.create(user = usr, otp = usr_otp)
			mess = f"Hello {usr.first_name},\nYour OTP is {usr_otp}\nThanks!"

			send_mail(
                                "Welcome to Medco - Verify Your Email",
                                mess,
                                EMAIL_HOST_USER,
                                [usr.email],
                                fail_silently = False
                            )
			return HttpResponse("Resend")

	return HttpResponse("Can't Send ")


 




class Profile_View(View):
    def get(self,request):
        if request.user.is_authenticated:
            btn="btn-primary"
            form=CustomerProfile()
            return render(request, 'app/profile.html',{"fm":form,"btn":btn})
        else:
            return HttpResponseRedirect("/login/")

    def post(self,request):
        form=CustomerProfile(request.POST)
        if form.is_valid():
            use=request.user
            name=form.cleaned_data["name"]
            number=form.cleaned_data["number"]
            address=form.cleaned_data["locality"]
            city=form.cleaned_data["city"]

            fs=Customer(user=use,name=name,number=number,locality=address,city=city)
            fs.save()
            messages.success(request,"congratulation! Profile update successful.")
            return HttpResponseRedirect("/profile/")
        else:
            btn="btn-primary"
            return render(request, 'app/profile.html',{"fm":form,"btn":btn})





def plus_cart(request):
    if request.method =="GET":
        prod_id =request.GET["prod_id"]
        c =Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        cart=Cart.objects.filter(user=request.user)
        total_amount =0.0
        cartproduct=[crp for crp in cart]
        if cartproduct:
            for p in cartproduct:
                temp_amount=(p.quantity*p.product.unit_price)
                total_amount += temp_amount
            data ={
                "quantity":c.quantity,
                "totalamount":total_amount
            }
            return JsonResponse(data)





def minus_cart(request):
    if request.method =="GET":
        prod_id =request.GET["prod_id"]
        c =Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        cart=Cart.objects.filter(user=request.user)
        total_amount =0.0
        cartproduct=[crp for crp in cart]
        if cartproduct:
            for p in cartproduct:
                temp_amount=(p.quantity*p.product.unit_price)
                total_amount += temp_amount
        data ={
            "quantity":c.quantity,
            "totalamount":total_amount
            }
        return JsonResponse(data)


def remove_cart(request):
    if request.method =="GET":
        prod_id =request.GET["prod_id"]
        c =Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        
        cart=Cart.objects.filter(user=request.user)
        total_amount =0.0
        cartproduct=[crp for crp in cart]
        if cartproduct:
            for p in cartproduct:
                temp_amount=(p.quantity*p.product.unit_price)
                total_amount += temp_amount
        data ={
            
            "totalamount":total_amount
            }
        return JsonResponse(data)


def payment_done(request):
    usr=request.user
    cusid=request.GET.get("custid")
    customer=Customer.objects.get(id=cusid)
    cart =Cart.objects.filter(user=usr)
    for c in cart:
        Status(user=usr,customer=customer,product=c.product,quantity=c.quantity).save()
        c.delete()
    return redirect("orders")



def terms(request):
    return render(request, 'app/terms.html')



def search(request):
    src=request.GET.get("search")
    # print("the search option is "+ src)
    if src:
        try:
            pd=Product.objects.get(titel=src)
            return render(request, 'app/productdetail.html',{"pd":pd})
        except:
            return HttpResponseRedirect("/allmedicine/")


def autocompleted(request):
    if "term" in request.GET:
        qs=Product.objects.filter(titel__istartswith=request.GET.get("term"))
        titels=list()
        for product in qs:
            titels.append(product.titel)
        return JsonResponse(titels,safe=False)

def data(request):

    for a in range(1,18133):
        dt=Database(a)
        dtl=dt.print_data_test()
        try:
            tl=dtl[0]
        except:
            pass
        try:    
            sm_tl=dtl[1]
        except:
            pass
        try:
            gn_nm=dtl[2]
        except:
            pass
        try:
            st=dtl[3]
        except:
            pass
        try:
            ma_nm=dtl[4]
        except:
            pass
        try:
            unt_p=dtl[5]
        except:
            pass
        try:
            pck_p=dtl[6]
        except:
            pass
        try:
            indi=dtl[7]
        except:
            pass
        try:
            ther=dtl[8]
        except:
            pass
        try:
            phar=dtl[9]
        except:
            pass
        try:
            dos=dtl[10]
        except:
            pass
        try:
            inter=dtl[11]
        except:
            pass
        try:
            contra=dtl[12]
        except:
            pass
        try:
            side_ef=dtl[13]
        except:
            pass
        try:
            preg=dtl[14]
        except:
            pass
        try:
            preca=dtl[15]
        except:
            pass
        try:
            overd=dtl[17]
        except:
            pass
        try:
            sto=dtl[18]
        except:
            pass




        cc=Product(titel=tl,small_name=sm_tl,generic_name=gn_nm,strength=st,
        manufactured_by=ma_nm,unit_price=float(unt_p),pack_price=pck_p,indications=indi,
        therapeutic_class=ther,pharmacology=phar,dosag_and_administration=dos,interaction=inter,
        contraindications=contra,side_effects=side_ef,pregnancy_and_lactation=preg,
        precautions_and_warnings=preca,overdose_effects=overd,storage_conditions=sto)
        cc.save()
    
    return render(request, 'app/data.html')

        












        
        