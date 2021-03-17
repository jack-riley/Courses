from django.shortcuts import render, redirect
from .models import Course, Description, Comment
from django.contrib import messages


# Create your views here.

def index(request):
    context = {"course_list": Course.objects.all()}
    return render(request,  'all.html', context )

def delete(request, id):
    pass
    context = {"course": Course.objects.get(id=id)}
    return render (request, 'delete.html', context)

def process_delete(request, id):
    if request.method == 'POST':
        d_course = (Course.objects.get(id = id))
        d_course.delete()
    return redirect('/')

def process_new_course(request):
    errors = Course.objects.validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
        
    else:
        name = request.POST["name"]
        desc = request.POST["desc"]
        Course.objects.create(name = name)
        new_course = Course.objects.get(name = name)
        Description.objects.create(course = new_course, desc = desc)
        messages.success(request, "Course Sucessfully Created")
        return redirect('/')

def comment(request, id):
    pass
    context = {"course": Course.objects.get(id=id)}
    return render (request, 'comment.html', context)

def process_comment(request, id):
    errors = Course.objects.validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/{id}")
    
    else:
        comm = request.POST["comm"]
        course = Course.objects.get(id=id)
        Comment.objects.create(course = course, comm = comm)
        messages.success(request, "Comment Sucessfully Added")
        return redirect(f"/{id}")

    
