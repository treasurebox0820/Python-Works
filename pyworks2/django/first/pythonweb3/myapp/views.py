from django.shortcuts import render
…
def index(request,my_dict):
    …
    return render(request, 'index.html', my_dict)
from .forms import TestForm
def formtest(request):
    my_dict = {
        'form':TestForm(),
        'insert_data':'DATA',
    }
    if (request.method == 'POST'):
        my_dict['insert_data'] = '文字:' + request.POST['txt'] + '<br>数値:' + request.POST['num']
        my_dict['form'] = TestForm(request.POST)
    return render(request, 'formtest.html', my_dict)