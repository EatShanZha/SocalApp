from django.db import models
import os
import uuid

# Create your models here.
class User(models.Model):
    userAccount = models.CharField(max_length=20,unique=True)
    userPasswd = models.CharField(max_length=20)
    userName = models.CharField(max_length=20)
    userImg = models.CharField(max_length=150)
    userGender = models.BooleanField(default=True)
    userBirth = models.DateField(max_length=20)
    userContent =models.TextField(default='nothing...')
    userToken = models.CharField(max_length=50)
    createTime = models.DateTimeField(auto_now_add=True)
    contacts = models.ManyToManyField('self', blank=True, related_name='my_friends')
    def __str__(self):
        return self.userName
    @classmethod
    def create_user(cls,userAccount,userPasswd,userName,userImg,userGender,userBirth,userContent,userToken,createTime):
        stu = cls(userAccount=userAccount,userPasswd=userPasswd,userName=userName,userImg=userImg,userGender=userGender,userBirth=userBirth,userContent=userContent,userToken=userToken,createTime=createTime)
        return stu

class Contact(models.Model):
    userAccount = models.CharField(max_length=20)
    userContact = models.CharField(max_length=20)
    latestTime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.userAccount
    @classmethod
    def create_user(cls, userAccount, userContact,latestTime):
        contact = cls(userAccount, userContact,latestTime)
        return  contact

def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    # return the whole path to the file
    return os.path.join(instance.author.pk, "img", filename)

def upload_to(instance, filename):
    return 'upload/photo/%s/%s' % (instance.author.pk,filename)

# 用户动态表
class Article(models.Model):
    content = models.CharField(u"内容",max_length=200)
    # 在当前目录子目录
    head_img =models.ImageField(default='',upload_to=upload_to,blank=True)
    author = models.ForeignKey('User',on_delete=models.CASCADE,verbose_name='作者')
    # 时间不用自己写
    publish_data = models.DateTimeField(auto_now= True,verbose_name='发布时间')
    # 动态是给别人看，还是只能自己
    hidden = models.BooleanField(default=False,verbose_name="是否隐藏")
    # 动态顺序有些制定
    priority = models.IntegerField(u"优先级",default=1000)
    #所属标签
    category = models.ForeignKey("Category", default='',blank=True,on_delete=models.CASCADE,verbose_name="标签")


#动态评论表
class Comment(models.Model):
    article = models.ForeignKey("Article",on_delete=models.CASCADE)
    user = models.ForeignKey('User',on_delete=models.CASCADE)
     #评论下面可以还有多个评论，sql不能自关联。python提供，有多层。父字段，自己。
    # parent_comment = models.ForeignKey('Commenthpy',)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE,related_name='p_comment', blank=True, null=True)
    #blank admin ,null数据库
    comment = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "<user:%s>" % ( self.user)

#动态点赞表
class ThumbUp(models.Model):
    #点赞
    article = models.ForeignKey('Article',on_delete=models.CASCADE)
    user = models.ForeignKey('User',on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return u"<user:%s>" % (self.user,)

#动态标签表
class Category(models.Model):
    name =models.CharField(max_length=64, unique=True)
    def __str__(self):
        return self.name