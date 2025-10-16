# Ex.05 Design a Website for Server Side Processing
## Date:

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
math.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Power calculation</title>
<style>
    body{
        align-items:center;
        margin-left:20%;
        margin-top:5%;
        margin-right:20%;
        border:20px groove blueviolet;
        margin-bottom:15%;
        font-family:Lucida Calligraphy;
        background:linear-gradient(to bottom right,rgba(255,0,255,0),rgba(255,0,255,2));
        
    }  
    form{
        padding-left: 30px;
    }  
    h1{
        text-align:center;
        color:red;
        font-family:Algerian;
        font-size:50px;
        font-weight:200px;
    }   
    input,label,div,button,body{
        font-size:30px;
    }  
    button{
        margin-left:auto;
        margin-right:auto;
        align:center;
    }  
    div{
        margin-bottom:20px;
    }                                
</style>
</head>
<body>
    <h1>Power Calculation</h1>
    <form method="post">
        {% csrf_token %}
        <div >
        <label for ='current'>Current: &emsp;&emsp;&emsp;&emsp;&emsp;</label>
        <input type="number" id="current" name="current" value="{{i}}"/>(in A)<br>
        </div>
        <div>
        <label for ='resistance'>Resistance:&emsp;&emsp;&emsp;&emsp;</label>
        <input type="number" id="resistance" name="resistance" value="{{r}}"/>(in ohm)<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
        </div>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
        <button type="submit" value="Calculate" style="font-family:Lucida Calligraphy">Calculate Power</button>
    <div style="margin-top: 20px;">
            Power produced:&emsp;<input type="text" value="{{power}}">(in W)<br>
    </div>
    </form>
</body>
</html>

views.py
from django.shortcuts import render
def power(request):
    context={}
    context['power']='0'
    context['i']='0'
    context['r']='0'
    if request.method=="POST":
        i=request.POST.get('current','0')
        r=request.POST.get('resistance','0')
        print("request=",request)
        print('Current=',i)
        print('Resistance=',r)
        
        isquare=int(i)*int(i) 
        power=isquare*int(r)
        print('Power=',power)
        context['power']=power
        context['i']=i
        context['r']=r
    return render(request,'math.html',context)

urls.py
from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('powerproduced/',views.power,name='powerproduced'),
    path('',views.power,name='powerproducedroot'),
]

```

## SERVER SIDE PROCESSING:

![alt text](<Screenshot 2025-10-16 163010.png>)

## HOMEPAGE:
![alt text](<Screenshot 2025-10-16 154059.png>)

## RESULT:
The program for performing server side processing is completed successfully.

