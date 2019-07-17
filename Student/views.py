from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . models import StudentList
from django.urls import reverse_lazy


# Create your views here.
class IndexView(ListView):
    model = StudentList
    template_name = 'index.html'

class StudentCreateView(CreateView):
    model = StudentList
    fields = '__all__'
    template_name = 'studentnew.html'


class StudentUpdateView(UpdateView):
    model = StudentList
    fields = ['RollNo','name','test1','test2','semester']
    template_name = 'updatestudent.html'



class StudentDeleteView(DeleteView):
    model = StudentList
    template_name = 'studentdelete.html'
    success_url = reverse_lazy('home')