from django.http import HttpResponse
from django.shortcuts import render

from dor.models import ActvityApplyment, Student


def stu_activity_applyment(request):
    activity_no=1
    activity_name="十大歌手"
    sno=request.POST.get('sno',None)
    apply_time=request.POST.get('apply_time',None)
    ad_no='张敏华'
    apply_status="申请中"
    test1=ActvityApplyment(actvity_no=activity_no,activity_name=activity_name,sno=sno,apply_time=apply_time,ad_no=ad_no,apply_status=apply_status)
    test1.save()
    return HttpResponse("<p>申请活动成功</p>")

def stu_show_activity_info(request):
    pass