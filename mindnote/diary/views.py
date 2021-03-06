from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse
from .models import Page
from .forms import PageForm

# def page_list(request):
#     object_list = Page.objects.all()
#     paginator = Paginator(object_list, 8)
#     curr_page_number = request.GET.get('page')

#     if curr_page_number is None:
#         curr_page_number = 1
    
#     page = paginator.page(curr_page_number)
#     return render(request, 'diary/page_list.html',{'page':page})

class PageListView(ListView):
    model = Page
    template_name = 'diary/page_list.html'
    conetext_object_name = 'obj'
    ordering = ['-dt_created']
    paginate_by = 8
    page_kwarg = 'page'

# def page_detail(request,page_id):
#     page_obj = Page.objects.get(id=page_id)
#     context = {'object' : page_obj}
#     return render(request, 'diary/page_detail.html',context)

class PageDetailView(DetailView):
    model = Page
    template_name = 'diary/page_detail.html'
    pk_url_kwarg = 'page_id'
    context_object_name = 'object'

def info(request):
    return render(request, 'diary/info.html')

class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    template_name = 'diary/page_form.html'

    def get_success_url(self):
        return reverse('page-detail', kwargs={'page_id':self.object.id})

class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'diary/page_form.html'
    pk_url_kwarg = 'page_id'

    def get_success_url(self):
        return reverse('page-detail', kwargs = {'page_id':self.object.id})


# def page_delete(request, page_id):
#     page = Page.objects.get(id = page_id)
#     if request.method == 'POST':
#         page.delete()
#         return redirect('page-list')
#     else:
#         context = {'form': page }
#         return render(request,'diary/page_confirm_delete.html', context)
    
#     return redirect('page-list')

class PageDeleteView(DeleteView):
    model = Page
    template_name = 'diary/page_confirm_delete.html'
    pk_url_kwarg = 'page_id'
    context_object_name = 'page'

    def get_success_url(self):
        return reverse('page-list')

def index(request):
    return render(request,'diary/index.html')