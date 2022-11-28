from django.shortcuts import render
from .forms import UploadFileForm
from .models import Dados





def uploadfile(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            # teste = request.FILES['file']
            uploaded_file = form.save()
            return render(request, 'dados/form.html', {
            'uploaded_file': uploaded_file
            })

            
    else:
        form = UploadFileForm()
    return render(request, "dados/form.html", {'form':form})

    
