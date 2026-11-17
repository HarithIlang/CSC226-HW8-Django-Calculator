from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    no1 = int(request.GET.get('no1'))
    no2 = int(request.GET.get('no2'))
    op = request.GET.get('op')

    if op in ['/', '%', '//'] and no2 == 0:
        answer = 'cannot divide by zero'
    elif op == '+':
        answer = no1 + no2
    elif op == '-':
        answer = no1 - no2
    elif op == '*':
        answer = no1 * no2   
    elif op == '/':
        answer = no1 / no2
    elif op == '%':
        answer = no1 % no2
    elif op == '//':
        answer = no1 // no2
    else:
        answer = 'unknown operator'     
    
    return render(request, 'result.html', {'answer': answer})