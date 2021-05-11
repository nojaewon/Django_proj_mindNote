from django.shortcuts import render, redirect
from .models import Page
from .forms import PageForm

# Create your views here.
def page_list(request):
    object_list = Page.objects.all()
    context = {'object_list':object_list}
    return render(request, 'diary/page_list.html',context)

def page_detail(request,page_id):
    page_obj = Page.objects.get(id=page_id)
    context = {'object' : page_obj}
    return render(request, 'diary/page_detail.html',context)

def info(request):
    return render(request, 'diary/info.html')

def page_create(request):
    if request.method == 'POST':
        new_form = PageForm(request.POST)
        if new_form.is_valid():
            new_page = new_form.save()
            return redirect('page-detail', page_id = new_page.id)
    else:
        new_form = PageForm()
    context = {'form': new_form}
    return render(request, 'diary/page_form.html', context) 


def page_update(request, page_id):
    page = Page.objects.get(id = page_id)
    if request.method == 'POST':
        new_form = PageForm(request.POST, instance=page)
        if new_form.is_valid():
            new_form.save()
            return redirect('page-detail', page_id = page.id)
    else:
        new_form = PageForm(instance=page)
    return render(request,'diary/page_form.html',{'form':new_form})


def page_delete(request, page_id):
    page = Page.objects.get(id = page_id)
    if request.method == 'POST':
        page.delete()
        return redirect('page-list')
    else:
        context = {'form': page }
        return render(request,'diary/page_confirm_delete.html', context)

    return redirect('page-list')

def index(request):
    return render(request,'diary/index.html')