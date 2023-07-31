from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib import messages


def index(request):
    # user = request.user
    todo = Todo.objects.all().order_by('due_date')
    if request.method =='POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            # todo.user = user
            todo.description = 'this is the default description'
            print(todo)
            todo.save()
            messages.success(request, 'Todo successfully added')
            return redirect('core:index')
    else:
        form = TodoForm()
    
    context = {
        'todo': todo,
        'form': form}
    return render(request, 'index.html', context)

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id).delete()
    return redirect('core:index')

