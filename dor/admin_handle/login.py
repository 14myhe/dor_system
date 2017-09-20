from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, render_to_response
from dor.models import DorAdminAccount,DormitoryAdmin,Student
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.sessions.models import Session

def admin_sign_in(request):
    if request.method=="POST":
        user = request.POST.get("username", '')
        pwd = request.POST.get("password", '')
        try:
            obj = DorAdminAccount.objects.get(username=user)
            request.session['userno'] = obj.ad_no
        except Exception as err:
            print(err)
            return render(request, "index.html", {'error': "用户名不存在"})

        if check_password(pwd, obj.password)==False:
            return render(request, "index.html", {'error': "用户名和密码不匹配"})


        try:
            admin = DormitoryAdmin.objects.get(dorm_admin_no=obj.ad_no)
            request.session['username']=admin.dorm_admin_name
            return render(request, "admin/index.html", {'username': admin.dorm_admin_name})
        except Exception as err:
            print(err)

        return render(request, "index.html", {'error': "数据库中没有该管理员"})
