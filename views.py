from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Students, Registration, Post, Comment
from .forms import userforms, CommentForm
from datetime import datetime
# from django.template.loader import render_to_string

# Create your views here.exit()



books={
    'thebook1':'this is chemistery book',
    'thebook2':'this is physics book',
    'thebook3':'this is math book',
    'thebook4':'this is science book',
    'thebook5':'this is java book',
    'thebook6':'this is python book',
    'thebook7':'this is javacript book',
    'thebook8':'this is css book',
    'thebook9':'this is html book',
    'thebook10':'this is php book'
}





def PostDetail(request,pk):
   if 'user' not in request.session:
      return HttpResponseRedirect('/book/loginpage')
   PostDetail=Post.objects.get(id=pk) 
   num_comment = Comment.objects.filter(post=PostDetail).count()
   return render(request,'post_detail.html',{'PostDetail':PostDetail,'num_comment':num_comment})

def blog(request):
   if 'user' not in request.session:
      return HttpResponseRedirect('/book/loginpage')
   postdata=Post.objects.all()
   return render(request,'blog.html',{'postlist':postdata})


def post_detail(request):
   if 'user' not in request.session:
      return HttpResponseRedirect('/book/loginpage')
   return render(request,'post_detail.html')

def addblog(request):
   if 'user' not in request.session:
      return HttpResponseRedirect('/book/loginpage')
   if request.method=="POST":      
      title=request.POST.get('title')
      author=request.POST.get('author')
      content=request.POST.get('content')
      status=request.POST.get('status')
      ab=Post(title=title,author=author,content=content,status=status)
      ab.save()
      return HttpResponseRedirect('/book/blog')
      
   return render(request,'addblog.html')

def addcomment(request,pk): 
   if 'user' not in request.session:
      return HttpResponseRedirect('/book/loginpage')     
   PostDetail = Post.objects.get(id=pk)
   form = CommentForm(instance=PostDetail)
   if request.method=="POST":
      form = CommentForm(request.POST, instance=PostDetail)
      if form.is_valid():
         name = request.user.username
         body = form.cleaned_data['body']
         ac = Comment(post=PostDetail,name=name,body=body,date_added=datetime.now())
         ac.save()
         return HttpResponseRedirect(reverse('PostDetail', args=[pk]))
      else:
          print('form is invalid')
   else:
      form = CommentForm()
      return render(request,'addcomment.html',{'form':form})

def delete_comment(request,pk):
   comment = Comment.objects.filter(post=pk).last()
   post_id = comment.post.id
   comment.delete()
   return HttpResponseRedirect(reverse('PostDetail', args=[post_id]))

def loginpage(request):
   if request.method=='GET':
    return render(request,'login.html')
   else:
      email=request.POST.get('email')
      password=request.POST.get('password')
   user=Registration.objects.get(email=email)
   if(not(user)):
      return render(request,'login.html')
   if(user.password==password):
      request.session['user']=email
      return HttpResponseRedirect('blog')
   else:
      return HttpResponse("Your username and password didn't match.")   

      
def logout(request):
    try:
        del request.session["user"]
    except KeyError:
        pass
    return HttpResponseRedirect("/book/loginpage")

def registrationpage(request):
   print(request.GET)
   firstname=request.GET['firstname']     
   last_name=request.GET['last_name']
   email=request.GET['email']
   password=request.GET['password']
   address=request.GET['address']
   reg=Registration(firstname=firstname,last_name=last_name,email=email,password=password,address=address)
   reg.save()
   return HttpResponse('sign up')

def registration(request):
   return render(request,'registration.html')
   
def showregistration(request):
   registration=Registration.objects.all()
   return render(request,'showregistration.html',{"registration":registration})

def regupdate(request,id):
   registration=Registration.objects.get(id=id)
   template=loader.get_template('regupdate.html')
   context={
      'registration':registration,
   } 
   return HttpResponse(template.render(context,request))

def regupdated(request,id):
  firstname = request.POST['firstname']
  last_name = request.POST['last_name']
  email = request.POST['email']
  password = request.POST['password']
  address = request.POST['address']
  registration = Registration.objects.get(id=id)
  registration.firstname = firstname
  registration.last_name = last_name
  registration.email = email
  registration.password = password
  registration.address = address
  registration.save()
  return HttpResponseRedirect(reverse('showregistration'))

def regdelete(request,id):
   registration=Registration.objects.get(id=id)
   registration.delete()
   return HttpResponseRedirect(reverse('showregistration'))

def count(request):
   if request.session==count:
      request.session['count']+=1
   return HttpResponse('count')

def addstudent(request):
   return render(request,'addstudent.html')

def addstudentform(request):
   print(request.GET)
   name=request.GET['name']
   f_name=request.GET['f_name']
   roll_no=request.GET['roll']
   s=Students(name=name,roll_no=roll_no,f_name=f_name)
   s.save()
   return HttpResponse('Data Received')

def showall(request):
   students=Students.objects.all()
   return render(request,'showall.html',{"students":students})

def update(request,id):
   students=Students.objects.get(id=id)
   template=loader.get_template('update.html')
   context={
      'students':students,
   } 
   return HttpResponse(template.render(context,request))


def updated(request,id):
  name = request.POST['name']
  f_name = request.POST['f_name']
  roll_no = request.POST['roll']
  students = Students.objects.get(id=id)
  students.name = name
  students.f_name = f_name
  students.roll_no = roll_no
  students.save()
  return HttpResponseRedirect(reverse('showall'))

def delete(request,id):
   students=Students.objects.get(id=id)
   students.delete()
   return HttpResponseRedirect(reverse('showall'))


def userform(request):
      userform=userforms()
      if request.method=="POST":
         n1=int(request.POST.get('num1'))
         n2=int(request.POST.get('num2'))
         finalans=n1+n2
      return render(request,'userforms.html',{'form':userform})


def base(request):
   return render(request,'base.html')

def homepage(request):
   return render(request,'homepage.html')

def about(request):
   return render(request,'about.html')

def shop(request):
   return render(request,'shop.html')

def contact(request):
   return render(request,'contact.html')

def header(request):
   return render(request,'header.html')

def footer(request):
   return render(request,'footer.html')


def bookpage(request):
   flist=list(books.keys())
   return render(request,'index.html',{'books':flist})

def bookdetails(request):
   return render(request,'bookdetails.html')
def thebook_no(request,thebook_no):
   booklist = list(books.keys())
   if thebook_no <= len(booklist):
      return HttpResponse(books[booklist[thebook_no-1]])
   else:
      return HttpResponseNotFound('not a right book')


def thebook(request,thebook):
    if thebook in books.keys():
       return HttpResponse(books[thebook])
    else:
       return HttpResponseNotFound('this is not a right book')





# def bookpage(request):
#    return render(request,'index.html')


# def bookdetails(request):
#    flist=''
#    for i in books.keys():
#       flist+= f"<li><a href='/book/bookdetails{i}'>{i}</a></li>"
#    return HttpResponse(f"<ol>{flist}</ol>")


   #return HttpResponse("<a href='/book/thebook1'>thebook1</a>")
   #return render(request,'bookdetails.html')
# def thebook_no(request,thebook_no):
#    booklist = list(books.keys())
#    if thebook_no <= len(booklist):
#       return HttpResponse(books[booklist[thebook_no-1]])
#    else:
#       return HttpResponseNotFound('not a right book')


# def thebook(request,thebook):
#     if thebook in books.keys():
#        return HttpResponse(books[thebook])
#     else:
#        return HttpResponseNotFound('this is not a right book')

# def thebook1(request):
#     return HttpResponse('chemistery')  
# def thebook2(request):
#     return HttpResponse('english')
# def thebook3(request):
#     return HttpResponse('physics')
# def thebook4(request):
#     return HttpResponse('math')
# def thebook5(request):
#     return HttpResponse('javascript')
# def thebook6(request):
#     return HttpResponse('php')
# def thebook7(request):
#     return HttpResponse('python')
# def thebook8(request):
#     return HttpResponse('java')
# def thebook9(request):
#     return HttpResponse('html')
# def thebook10(request):
#     return HttpResponse('css')

