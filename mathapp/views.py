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
