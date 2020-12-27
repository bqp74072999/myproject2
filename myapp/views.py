from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect


# Create your views here.
from myapp.models import YoyoPersoninfo


def index(request):
    return HttpResponse("恭喜你登陆成功")


def wanneng(request):
    return HttpResponse("不管访问啥都是我，可以用来提示路径错误")


def duoge(request):
    return HttpResponse("可以多个路径指向一个资源")


def tb(request):
    return HttpResponse("匹配多个层级")


def login(request):
    return render(request,"myapp_t/login.html")#render 转发




def request1(request):
    #request = HttpRequest()
    print(request.path)
    print(request.method)
    print(request.encoding)

    return HttpResponse("获取基本信息")


def doRegist(request):
    #request = HttpRequest()
    requestm = None
    if request.method == "GET":
        requestm = request.GET
    elif request.method == "POST":
        requestm = request.POST

    username = requestm.get("username1")
    password = requestm.get("password1")

    if username == "txn" and password == "a123a123":
        return redirect("/index/")
    return render(request,"myapp_t/login.html")


#查询
def cha(request):
    '''
    #all = YoyoPersoninfo.objects.all()#查所有
    all = YoyoPersoninfo.objects.all()[0:2]#切片，不能切负到
    for i in all:
        print(i.id,i.qq,i.name)
    '''


    '''
    one = YoyoPersoninfo.objects.get(name="你好")## 名称为 xx的一条，多条会报错
    print(one.name,one.id)
    '''


    '''
    get是用来获取一个对象的，如果需要获取满足条件的一些人，就要用到filter
    Person.objects.filter(name="abc") # 等于
    Person.objects.filter(name__contains="abc") # 名称中包含 "abc"的人
    # filter是找出满足条件的，当然也有排除符合某条件的
    Person.objects.exclude(name__contains="刘") # 排除包含 WZ 的Person对象
    Person.objects.filter(name__contains="刘").exclude(age=20) # 找出名称含有abc, 但是排除年龄是23岁的

    Person.objects.all().count() 返回当前查询的总条数
    Person.objects.filter(name="男").count() 返回男到的总条数
    排序
    Person.objects.all().order_by("age")  正序 类似 select * from person order by age asc
    Person.objects.all().order_by("-age")  倒序 类似select * from person order by age desc
    Person.objects.filter(age__in=[30,20]) in 语句 字段__in集合 类似select * from person where age in (30,20)
    Person.objects.filter(age=30).filter(username__contains="张")
 


    yixie = YoyoPersoninfo.objects.filter(name="你好")         # 等于
    for i in yixie:
        print(i.id,i.name)


    baohan = YoyoPersoninfo.objects.filter(name__contains="你好")         # 名称中包含 "abc"的人
    for i in baohan:
        print(i.id,i.name)


    paichu = YoyoPersoninfo.objects.exclude(name__contains="你好")        # 排除包含 你好 的Person对象
    for i in paichu:
        print(i.id,i.name)


    shuangtiaojian = YoyoPersoninfo.objects.filter(name__contains="你好").exclude(qq="45") #查询包含"你好"的 并且排除 qq为"45"的人
    for i in shuangtiaojian:
        print(i.id,i.name)


    zongshuliang = YoyoPersoninfo.objects.all().count() #查询总数
    print(zongshuliang)
    '''

    return HttpResponse("查数据喽")

#删除目前只用get
def delete(request):
    delete = YoyoPersoninfo.objects.get(qq=45).delete()
    print("123",delete)
    return HttpResponse("删除成功")

#修改
def update(request):
    name = request.GET.get("name")
    qq = request.GET.get("qq")
    update = YoyoPersoninfo.objects.get(qq="123423")
    update.name = name
    update.qq = qq
    update.save()
    return HttpResponse("修改成功")


def add(request):
    add = YoyoPersoninfo.objects.create(name="haha",qq=999)
    add.save()
    print("hello")
    print("hello2")
    print("hello3")
    print("hello4")
    return HttpResponse("添加成功")


def info(request):
    # username = request.GET.get("u1")
    # password = request.GET.get("p1")
    # age = request.GET.get("a1")
    # dict = ["zhang","wang","li"]
    dict = [{"username":"汤晓宁","sex":"女"},{"username":"小小汤","sex":"女"},{"username":"赵萌呀","sex":"男"}]


    return render(request,"myapp_t/info.html",context={"dict1":dict})


def ifpd(request):
    cj = int(request.GET.get("cj"))
    print(cj)
    return render(request,"myapp_t/ifpanduan.html",{"cj":cj})