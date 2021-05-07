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
        new_from = PageForm(request.POST)
        new_page = new_form.save()
        return redirect('page-detail', page_id = new_page.id)
    else:
        form = PageForm()
        context = {'form': form}
        return render(request, 'diary/page_form.html', context) 