from django.shortcuts import render
import matplotlib.pyplot as plt
import scipy.special
from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'index.html')

def calc_clk(request):
    print("in")
    t=int(request.GET.get('t', None))
    ri=int(request.GET.get('r', None))
    v = int(request.GET.get('v', None))
    print(v)
    m=15
    ro=0.01    
    w = 5
    n=t-((ri-1)*(m-1))-v
    tot=0
    xi=[]
    for r in range(1,ri+1):
        tot =0
        n=t-((r-1)*(m-1)) - v
        for i in range(r,n):
                tot=tot+ (scipy.special.binom(n,i)*pow(ro,i)*pow(1-ro,n-i))
        xi.append(tot)  
    return HttpResponse(xi)