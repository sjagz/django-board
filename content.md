```
 pip install django
```
장고설치
```
django-admin startproject crud .

```
장고 관리자로 프로젝트를 만드는데 
crud 라는 폴더 이름으로 경로는 기존경로
```
settings.py 의 값을 바꿔줌 

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

```


```
python manage.py startapp boards

```
boards라는 이름의 어플리케이션을 생성

```
settings.py 의 값을 바꿔줌 
INSTALLED_APPS = [
    # new app
    'boards',

```
축약해서 쓰고 app의 경로를 찍어줘야함
```
from django.urls import path , include

urlpatterns = [
path('boards/', include('boards.urls')),
]
```
boards 안에 urls.py로 보냄
```
boards 안에 urls.py 를 만들고 
from django.contrib import admin
from django.urls import path , include
urlpatterns = [
]

```
```
def index(request):
    return render(request ,)
```
함수를 만듬 
```
http://bit.do/m44-docs 자료
base.html 을 복붙하는데 
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
이 부분은 부트스트랩을 이용하기위해서?
```
```
indexl html 에서 
{% extends 'base.html' %}
{% block body %}
    <h1>welcome</h1>
{% endblock %}

extends 연장 (상속이라고하는데 이미가 약간 애매한듯?)
```
```
models.py 에 들어가서 

from django.db import models

# Create your models here.

class Board(models.Model):
    title =models.CharField(max_length=20)
    content = models.TextField( )
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    auto_now 는 시간을 찍어주는것
```
```
python manage.py makemigrations

생성해줌

python manage.py migrate

반영
```
```
사용자 입력페이지(new)와 받아서 디비에저장하고 보여주는(create)
페이지 제작 
```

<form action="/boards/create/">

은 url 주소를 찍어주는것

```
form 을 methos = post 로만 바꿔주면 오류가뜸
CSRF 검증에 실패했습니다. 요청을 중단하였습니다.
그래서 포스트를 쓴 form 안에
{% csrf_token %}
추가

settings.py 미들웨어에 

'django.middleware.csrf.CsrfViewMiddleware',

이구문이 서버에서 토큰을 보내고
사용자가 이 토큰을 확인과정을 거치는 부분을 자동으로 해줌

```
id 값은 모델에서 지정안해줘도 장고내에서 만들어짐

migrations -> initial.py

('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

```

```
주소를 한꺼번에 바꾸어야할 상황이온다면
urls.py

app_name='boards'

urlpatterns = [
 path('', views.index , name='index'),
 ]
  3번째 인자  추가
```









