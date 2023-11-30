from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

def index(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {'todos': todos})

def details(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    context = {'todo': todo}
    return render(request, 'details.html', context)


def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        current_status = request.POST.get('current_status', '')  # Get current status from POST data
        todo = Todo.objects.create(title=title, text=text, current_status=current_status)
        return redirect('index')
    else:
        return render(request, 'create.html')


def update_status(request, pk):
    todo = Todo.objects.get(pk=pk)

    if request.method == 'POST':
        current_status = request.POST['current_status']
        updated_datetime = request.POST.get('updated_datetime', None)  # Updated line

        todo.current_status = current_status
        if updated_datetime:
            todo.updated_at = updated_datetime
        else:
            # Handle the case where updated_datetime is not provided
            pass
        todo.save()

        return redirect('details', todo.id)
    else:
        return render(request, 'details.html', {'todo': todo})

