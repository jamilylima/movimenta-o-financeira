from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def uploadfile(request):
    
    if request.method == 'POST':
        request_file = request.FILES['document'] if 'document' in request.FILES else None
        if request_file:
            fs = FileSystemStorage()
            file = fs.save(request_file.name, request_file)
            fileurl = fs.url(file)
            return render(request, "dados/form.html",{'fileurl': fileurl})
            
    return render(request, "dados/form.html")



   

