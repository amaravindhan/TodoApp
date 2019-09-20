from django.shortcuts import get_object_or_404, render, redirect

from .models import Todo

# Create your views here.
def home(request):
    if request.method == "POST":
        todo_item = request.POST.get('todo')
        Todo.objects.create(item = todo_item)
    
    todo_list = Todo.objects.all().order_by("-added_date")
    return render(request, 'todo/home.html', {"todo_list": todo_list})

def delete(request, item_id):
    get_object_or_404(Todo, pk=item_id).delete()
    # obj.delete()
    return redirect('todo_app:home')
    