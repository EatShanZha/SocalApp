from django.conf.urls import url
from . import views
app_name='SocalApp'
urlpatterns = [
    # url(r'^home/$', views.home, name="home"),
    url(r'^mine/$', views.mine, name="mine"),
    # 登陆
    url(r'^login/$', views.login, name="login"),
    # 注册
    url(r'^register/$', views.register, name="register"),
    # 验证账号是否被注册
    url(r'^checkuserid/$', views.checkuserid, name="checkuserid"),
    # 退出登陆
    # url(r'^quit/$', views.quit, name="quit"),
    # 星球
    url(r'^userlist/$', views.userlist, name="userlist"),
   # 用户详情
    url(r'^userdetail/(.*)/$', views.userdetail, name="userdetail"),
   # 联系人页面
    url(r'^chatlist/$', views.chatlist, name="chatlist"),
   #聊天界面
    url(r'^chat/(.*)/$', views.chat, name="chat"),
    url(r'^send_msg/$', views.send_msg, name="send_msg"),
    url(r'^get_msg/$', views.get_msg, name="get_msg"),
    url(r'^save_chat/$', views.save_chat, name="save_chat"),
    url(r'^article/$', views.article, name="article"),
    url(r'^public/$', views.public, name="public"),
    #动态详情
    url(r'^articledetail/(.*)/$', views.articledetail, name="articledetail"),
    url(r'^matchOnline/$', views.matchOnline, name="matchOnline"),
    url(r'^load/$', views.load, name="load"),
]