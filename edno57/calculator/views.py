from django.template.response import TemplateResponse

def calculator(request):
    if request.method == "POST":
        a = int(request.POST['a'])
        b = int(request.POST['b'])
        result = a + b

    return TemplateResponse(request, 'calculator.html', locals())


