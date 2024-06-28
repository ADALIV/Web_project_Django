from .models import WhatToDo, do_type
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone

# Create your views here.

def index(request):
    list = WhatToDo.objects.order_by('-pub_date')
    template = loader.get_template('to_do/index.html')
    return render(request, 'to_do/index.html', {'list':list})

def detail(request, do_id):
    try:
        do = get_object_or_404(WhatToDo, pk=do_id)
        doType = get_object_or_404(do_type, todo=do)
    except Http404:
        raise Http404("list does not exist")
    priority_choices = doType._meta.get_field('priority').choices
    progress_choices = doType._meta.get_field('progress').choices
    return render(request, 'to_do/detail.html', {'do':do, 'doType':doType, 'priority_choices': priority_choices, 'progress_choices': progress_choices})

def modify(request, do_id):
    do = get_object_or_404(WhatToDo, pk=do_id)
    doType = get_object_or_404(do_type, todo=do)
    try:
        # 필수 필드 가져오기
        text = request.POST['text']
        priority = request.POST["priority"]
        progress = request.POST["progress"]
    except KeyError:
        # 필수 필드가 비어있는 경우
        do.delete()
        return HttpResponse('''
        <script>
            alert("폼이 비어있습니다.");
            window.location.href = "/to_do/";
        </script>
        ''')
        
    do.text = text  # 텍스트 업데이트
    doType.priority = priority  # 우선순위 업데이트
    doType.progress = progress  # 진행 상태 업데이트
        
    # 변경된 내용 저장
    do.save()
    doType.save()
    return HttpResponseRedirect(reverse('to_do:detail', args=(do.id,)))

def addDo(request):
    do = WhatToDo.objects.create(text="New to_do", pub_date=timezone.now())
    doType = do_type.objects.create(todo=do)
    priority_choices = doType._meta.get_field('priority').choices
    progress_choices = doType._meta.get_field('progress').choices
    return render(request, 'to_do/add.html', {'do':do, 'doType':doType, 'priority_choices': priority_choices, 'progress_choices': progress_choices})

def delete(request, do_id):
    if request.method == 'POST':
        do = get_object_or_404(WhatToDo, pk=do_id)
        do.delete()
        return HttpResponseRedirect(reverse('to_do:index'))
    else:
        return HttpResponse('''
        <script>
            alert("잘못된 요청");
            window.location.href = "/to_do/";
        </script>
        ''')