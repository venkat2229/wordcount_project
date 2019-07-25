
from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,"home.html")
def counts(request):
    mytext=request.GET['mytext']
    list=mytext.split()

    dic={}
    for word in list:
        if word in dic:
            dic[word]+=1
        else:
            dic[word]=1


    sort=(sorted(dic.items(),key=operator.itemgetter(1),reverse=True))

    return render(request,"count.html",{'mytext':mytext,'list':len(list),"dic":sort})
def tha(request):
    return render(request,"thank.html")
