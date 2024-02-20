from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Project
from .forms import ClientForm
from django.http import HttpResponse


def user_projects(request):
    if request.user.is_authenticated:
        user_projects = Project.objects.filter(users=request.user.id)
        return render(request, 'user_projects.html', {'user_projects': user_projects})
    else:
        return render(request, 'user_projects.html', {'user_projects': []})

def client_list(request):
    client_list = Client.objects.all()
    return render(request, 'client_list.html', {'client_list': client_list})

def edit_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'edit_client.html', {'form': form, 'client': client})


def register_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'register_client.html', {'form': form})

#----------------

def delete_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    client.delete()
    return redirect('client_list')




