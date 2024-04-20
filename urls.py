from django.urls import path
from .import views

urlpatterns = [
    # path('',views.bookpage),
    path('blog',views.blog,name='blog'),
    path('PostDetail/<int:pk>',views.PostDetail,name='PostDetail'),
    path('addblog',views.addblog,name='addblog'),
    path('PostDetail/<int:pk>/addcomment',views.addcomment,name='addcomment'),
    path('PostDetail/<int:pk>/delete_comment',views.delete_comment,name='delete_comment'),
    path('post_detail',views.post_detail,name='post_detail'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('update/updated/<int:id>',views.updated,name='updated'),
    path('count',views.count,name='count'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('logout',views.logout,name='logout'),
    path('registration',views.registration,name='registration'),
    path('registrationpage',views.registrationpage,name='registrationpage'),
    path('showregistration',views.showregistration,name='showregistration'),
    path('regupdate/<int:id>',views.regupdate,name='regupdate'),
    path('regupdate/regupdated/<int:id>',views.regupdated,name='regupdated'),
    path('regdelete/<int:id>',views.regdelete,name='regdelete'),
    path('userforms',views.userform,name='userforms'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('addstudentform',views.addstudentform,name='addstudentform'),
    path('showall',views.showall,name='showall'),
    path('homepage',views.homepage,name='homepage'),
    path('about',views.about,name='about'),
    path('shop',views.shop,name='shop'),
    path('contact',views.contact,name='contact'),
    path('header',views.header),
    path('footer',views.footer),
    path('base',views.base),
    path('bookdetails',views.bookdetails),
    
    # path('<int:thebook_no>',views.thebook_no),
    # path('<str:thebook>',views.thebook), 
]



# urlpatterns = [
#     path('thebook1', views.thebook1),
#     path('thebook2', views.thebook2),
#     path('thebook3', views.thebook3),
#     path('thebook4', views.thebook4),
#     path('thebook5', views.thebook5),
#     path('thebook6', views.thebook6),
#     path('thebook7', views.thebook7),
#     path('thebook8', views.thebook8),
#     path('thebook9', views.thebook9),
#     path('thebook10', views.thebook10)
# ]
