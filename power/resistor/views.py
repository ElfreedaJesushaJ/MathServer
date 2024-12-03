from django.shortcuts import render 
def powerlamp(request): 
    context={} 
    context['area'] = "0" 
    context['l'] = "0" 
    context['b'] = "0" 
    if request.method == 'POST': 
        print("POST method is used")
        i = request.POST.get('intensity','0')
        r = request.POST.get('resistance','0')
        print('request=',request) 
        print('intensity=',i) 
        print('resistance=',r) 
        power= (int(i) * int(i))*int(r)
        context['power'] = power 
        context['i'] = i
        context['r'] = r 
        print('power=',power) 
    return render(request,'resistor/math.html',context)
