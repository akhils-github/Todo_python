#***********function view import**********************
from django.shortcuts import redirect, render
from todo_app.forms import TodoForm
from todo_app.models import Task
#***********************************************************
# Create your views here.
#************************function views // starting*********************************
def home(request):
    tasks=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date')
        task=Task(task=name,priority=priority,date=date)
        task.save()
    return render(request,'Home.html',{'tasks':tasks})

def delete(request,id):
    task=Task.objects.get(id=id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    form=TodoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form})

#************************function views // Ended************************************
#************************ Class views // starting ************************************
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
#************************list views // starting*******************************************
class TaskListView(ListView):
    model=Task
    template_name='Home.html'
    context_object_name='tasks'

#************************list Ended //**************************************************
#************************Detail views /************************************************
class TaskDetailView(DetailView):
    model=Task
    template_name='detail.html'
    context_object_name='tasks'

#************************Detail Ended //**********************************************
#************************Update views // starting*************************************
class TaskUpdateView(UpdateView):
    model=Task
    template_name='update.html'
    context_object_name='task'
    fields=('task','priority','date')
    
    def get_success_url(self):
        return reverse_lazy('todo_app:cvbdetail', kwargs={'pk': self.object.pk})
    
 #************************Update Ended // **********************************************
 #************************Delete views // starting     *********************************
class TaskDeleteView(DeleteView):
    model=Task
    template_name='delete.html'
    success_url=reverse_lazy('todo_app:cvbhome')

#************************Delete Ended // ***********************************************
