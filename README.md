# Ex.05 Design a Website for Server Side Processing
## Date:03.12.2024

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
current.html

<html>
  <head>
    <title>Power</title>
    <style>
      body{
        background-color: aqua;
      }
      h1{
        background-color: blanchedalmond;
      }
      form{
        background-color: aquamarine;
      }
    </style>
  </head>
  <body>
    <h1 align="center">Power of a lamp</h1>
    <form align="center"method="post">
      {%csrf_token%}
      Intensity<input type="number" name="intensity" id="intensity" value={{i}}>
      <br>
      Resistance<input type="number" name="resistance" id="resistance" value={{r}}>
      <br>
      <button type="submit" >Calculate</button>
      <br>
      Power<input type="number" name="power" id="power" value={{power}}>
      <br>
    </form>
    
  </body>
</html>

views.py

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


urls.py

from django.contrib import admin 
from django.urls import path 
from resistor import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('powerlamp/',views.powerlamp,name="powerlamp"),
    path('',views.powerlamp,name="powerlamp")
]

```




## SERVER SIDE PROCESSING:

![alt text](<Serverside processing.png>)


## HOMEPAGE:

![alt text](<Home page.png>)


## RESULT:
The program for performing server side processing is completed successfully.
