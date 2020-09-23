"""W URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import os
from django.shortcuts import HttpResponse,render,redirect
import random
import subprocess



def generate_code():
    seeds = "1234567890"
    random_str = []

    for i in range(6):
        random_str.append(random.choice(seeds))

    return "" . join(random_str)



import datetime
def makedir():
    uid = generate_code()
    now = datetime.datetime.now()
    struid = now.strftime("%Y%m%d%H%M%S") + uid
    print(struid)
    # location = "temp/Inputdata/"+struid
    location = "temp/Inputdata/" + struid
    print(location)
    if not os.path.exists(location):
        os.makedirs(location)
        #print("S")
    return struid

def Server(request):
    global struid
    file = request.FILES.get("fileSeq", None)
    print(type(file))
    Sequence = request.POST.get("sequences")


    print('Sequence',Sequence)
    flag = False
    if file or Sequence: flag=True
    #print("sdasd",file.name)
    if request.method == "POST" and flag ==True:
        flag=False
        struid = makedir()
        file_path = "../W/temp/Inputdata/" + struid
        output_path =file_path+"/Output"
        if file:
            destination = open(os.path.join(file_path,file.name), 'wb+')
            for chunk in file.chunks():
                destination.write(chunk)
            destination.close()
            #print(request.FILES)
            os.chdir("../EnACP-web")
            subprocess.check_call('python EnACP_Predict.py '+os.path.join(file_path,file.name))
        else:
            file_path_web =file_path+'/sequence.fasta'
            #ame = struid+'.fasta'
            with open(file_path_web,'wb+') as wf:
                wf.write(Sequence)
            os.chdir("../EnACP-web")
            subprocess.check_call('python EnACP_Predict.py ' + os.path.join(file_path, 'sequence.fasta'))
        print "pp",os.getcwd()
        os.chdir('../W')
        #os.chdir("E:\W")
        return redirect('/Result/')
        #return render(request,'Result',{'output_path':output_path})
    return render(request,'Server.html')

def Result(request):
    import pandas as pd
    from glob import glob
    #print(os.getcwd())
    f=glob("temp/Inputdata/"+struid+'/Output*/*.csv')
    #print("f",f[0])
    data_set = pd.read_csv(f[0])
    print(data_set)
    print type(data_set)
    data = data_set.values[:,:]
    print type(data)
    test_data = [['','Non-ACP','ACP']]
    for line in data:
        ls = []
        x=0
        for j in line:
            if(x==0):j=int(j)+1
            else: j = j.round(10)
            ls.append(j)
            x+=1
        test_data.append(ls)

    return render(request,"Result.html", {'test_data':test_data})

urlpatterns = [
    #path('admin/', admin.site.urls),
    url('Server/', Server),
    url('Result/',Result)

]

