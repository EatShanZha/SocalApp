from django.shortcuts import render,redirect,HttpResponse
from SocalApp import utils
from .models import User,Contact,Article,Category,Comment
from django.http import JsonResponse
import time
import os
import random
import datetime
import json
import uuid
# Create your views here.
from django.conf import settings

global_msg_dic = {}

def login(request):
    if request.method == "POST":
        Account = request.POST.get("Account")
        Password = request.POST.get("Password")
        user = User.objects.filter(userAccount=Account,userPasswd=Password).first()
        if user:
            token = time.time() + random.randrange(1, 100000)
            user.userToken = str(token)
            user.save()
            request.session["username"] = user.userName
            request.session["token"] = user.userToken
            request.session["userAccount"] = user.userAccount
            return redirect('/mine/')
        else:
            return render(request, 'SocalApp/login.html', {'msg': "用户名/密码错误"})

    else:
        return render(request, 'SocalApp/login.html', {"title": "登陆"})
#注册
def register(request):
    if request.method == "POST":
        userAccount = request.POST.get("userAccount")
        userPasswd = request.POST.get("userPasswd1")
        userName = request.POST.get("userName")
        Gender = request.POST.get("userGender")
        userContent = request.POST.get("userContent")
        userBirth = request.POST.get("userBirth")
        token = time.time() + random.randrange(1, 100000)
        userToken = str(token)
        print(userAccount,userPasswd)
        f = request.FILES["userImg"]
        createTime = datetime.datetime.now().strftime('%Y-%m-%d')
        ImgPath = os.path.join(settings.MDEIA_ROOT, userAccount + ".png")
        with open(ImgPath, "wb") as fp:
            for data in f.chunks():
                fp.write(data)
        if Gender =='Male':
            userGender ='True'
        else:
            userGender = 'False'
        userImg = str(userAccount + '.png')
        user = User.create_user(userAccount,userPasswd,userName,userImg,userGender,userBirth,userContent,userToken,createTime)
        user.save()
        request.session["username"] = userName
        request.session["token"] = userToken
        request.session["userAccount"] = userAccount

        return redirect('/login/')
    else:
        return render(request, 'SocalApp/register.html', {"title":"注册"})

def checkuserid(request):
    userid = request.POST.get("userid")
    user = User.objects.get(userAccount=userid)
    try:
        if user:
            return JsonResponse({"data": "改用户已经被注册", "status": "error"})
    except User.DoesNotExist as e:
        return JsonResponse({"data":"可以注册","status":"success"})

def mine(request):
    token = request.session.get("token")
    user = User.objects.get(userToken=token)
    return render(request, 'SocalApp/mine.html',{"user":user})

def userlist(request):
    userlist = User.objects.all()
    return render(request, 'SocalApp/userlist.html',{"userlist":userlist})

def userdetail(request,Account):
    if request.method == "GET":
        user = User.objects.filter(userAccount=Account).first()
        userimg = os.path.join(r'/static/media', user.userAccount + '.png')
        return render(request, 'SocalApp/userdetail.html', {"user": user,"userimg":userimg})

def chatlist(request):
    token = request.session.get("token")
    user = User.objects.get(userToken=token)
    return render(request, 'SocalApp/chatlist.html', {"user": user})


def chat(request,Account):
    if request.method == "GET":
        pk = User.objects.get(userAccount=Account).pk
        # 聊天记录
        content = request.session.get(str(pk))
        return render(request, 'SocalApp/chat.html', {"ContactAccount": Account,"content":content})

def send_msg(request):
    data = request.POST.get('data')
    data = json.loads(data)
    data['date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    to_id = data.get('to_id')
    token = request.session.get("token")
    user = User.objects.get(userToken=token)
    ToUser = User.objects.get(userAccount=to_id)
    contact_type = data.get('contact_type')
    user.contacts.add(ToUser)

    if contact_type == 'single':
         if  not  to_id in global_msg_dic:
              global_msg_dic[to_id] = utils.Chat()
         global_msg_dic[to_id].msg_queue_hpy.put(data)
         print('\033[31;1mPush msg [%s] into user [%s] queue' % (data['msg'],user.name))
    # elif contact_type == 'group':
    #     group_obj_hpy = User.objects.get(userAccount=to_id)
    #     for member in group_obj_hpy.members.select_related():
    #
    #        if member.id != request.user.userprofilehpy.id:
    #            if  not  member.id in global_msg_dic:
    #               global_msg_dic[member.id] = utils.Chat()
    #        global_msg_dic[to_id].msg_queue_hpy.put(data)
    # return HttpResponse("aaaaaaaaa")


def get_msg(request):
    uid = request.GET.get('uid')
    if uid:
        res = []
        if uid not in global_msg_dic:
            global_msg_dic[uid] = utils.Chat()
        res = global_msg_dic[uid].get_msg(request)
        return HttpResponse(json.dumps(res))
    else:
        return HttpResponse(json.dumps("uid not provided!"))

def save_chat(request):
    if request.method == "POST":

        chatwith = request.POST.get('chatwith')
        chatId = User.objects.get(userAccount= chatwith).pk
        content = request.POST.get('content')
        request.session[chatId] = content
        return HttpResponse(json.dumps(request.session[chatId]))
    else:
        return HttpResponse(json.dumps("兄弟 别搞我"))


def article(request):
    if request.method == "POST":
        token = request.session.get("token")
        user = User.objects.get(userToken=token)
        new_article = Article()
        new_article.author = user
        new_article.content = request.POST.get('content')

        try:
            f = request.FILES["inputfile"]
            new_article.head_img = f
        except:
            pass

        try:
            new_category = Category()
            new_category.name = request.POST.get('category')
            new_category.save()
            new_article.category = Category.objects.get(name=new_category.name)
        except:
            new_article.category = Category.objects.get(name=new_category.name)
        new_article.save()
        return render(request, 'SocalApp/mine.html')
    else:
        return render(request, 'SocalApp/article.html')

def public(request):
    if request.method == "GET":
        articlelist = Article.objects.all()
        return render(request, 'SocalApp/public.html',{"articlelist":articlelist})

def articledetail(request,article_id):
    article = Article.objects.filter(pk=article_id).first()
    token = request.session.get("token")
    user = User.objects.get(userToken=token)
    if request.method == "GET":
        commentlist = Comment.objects.filter(article_id=article_id).all()
        return render(request, 'SocalApp/articledetail.html', {"article": article,"commentlist":commentlist})

    if request.method == "POST":
        new_comment = Comment()
        new_comment.comment = request.POST.get('comment')
        new_comment.article = article
        new_comment.user = user
        try:
            parent_comment = request.POST.getlist('parent_comment')
            comment = Comment.obj.get(pk=parent_comment)
            new_comment.parent_comment = comment
        except:
            pass
        new_comment.save()

        return HttpResponse(json.dumps("兄弟 别搞我"))

import queue
q = queue.Queue()
def matchOnline(request):
    token = request.session.get("token")
    user = User.objects.get(userToken=token)
    q.put(user.userAccount)
    return render(request, 'SocalApp/load.html',{"num":q.qsize()})

dic_match = {}
def load(request):
    token = request.session.get("token")
    user = User.objects.get(userToken=token)
    if user.userAccount in dic_match:
        account = dic_match[user.userAccount]
    else:
        account = q.get()
        if account == user.userAccount:
            q.put(account)
            load(request)
        dic_match[account] = user.userAccount
    return chat(request, account)
