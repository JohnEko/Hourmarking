from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q 
from post.models import Userhour
from .forms import Userform

# Create your views here.
def index(request):
    users = Userhour.objects.all()
    form = Userform()
    context = {'users':users, 'form': form}
    
    return render(request, "home.html", context)



def detail(request, pk):
    user_id =get_object_or_404(Userhour, id=pk)
    
    context = {"user_id": user_id}

    return render(request, "detail.html", context)



def search(request):
    query = request.GET.get("q", None)
    qs = Userhour.objects.all()
    if query is not None:
        qs = qs.filter(last_name__icontains=query)
    context = {
                   "qs" : qs
            }
            #return render(request, "home.html", context)

    return render(request, "home.html", context)

def create_view(request):
    form = Userform()
    if request.method == 'POST':
        form = Userform(request.POST or None)
        if form.is_valid():
            form.save()
            all_user = Userhour.objects.all()
            
            
            context = {"all_user":all_user}
            #return render(request, "base.html", context)
            return redirect('index')

    
        
    
    context = {'form': form}
    return render(request, "forms.html", context)


def update(request, pk):
    update_user = get_object_or_404(Userhour, id=pk) #create form and update form are same just this differences 1 & 2
    form = Userform(instance=update_user)
    
    if request.method == 'POST':
        form = Userform(request.POST, instance=update_user)
        if form.is_valid():
            form.save()
        return redirect("index")
    context ={'form': form}
    return render(request, 'forms.html', context)
    


def delete_view(request, user):
    user =get_object_or_404 (Userhour, id=user)
    if request.method == 'POST':
        user.delete()
        return redirect('index')

    context = {'user' : user}

    return render(request, "delete.html", context)