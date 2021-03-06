#  생활 코딩! HTML + CSS + 자바스크립트



## 코딩과 HTML

- 사람이 하는 일: 코드, 소스, 프로그래밍 언어

- 기계가 하는 일: 애플리케이션, 응용 프로그램, 앱, 웹페이지, 웹사이트(페이지가 모이면)

- 웹페이지를 만드는 언어는 __HTML__(HyperText Markup Language)



## HTML 코딩과 실습 환경 준비

- Atom 에디터 사용 (https://atom.io/)

- 바탕화면에 웹사이트 제작 프로젝트에 사용되는 파일들을 저장할  'web' 폴더 만들기

- Add project folder를 이용해 폴더를 프로젝트 폴더로 추가하고 new file을 이용해서 html파일 만들기
- 브라우저를 열고 ctrl + o를 누르면 html파일을 열 수 있다.



## 기본문법과 태그



- \</strong>: 글자를 굵게 강조

- \</u>: 글자에 밑줄을 침

- 태그는 <> ... </>식으로 열리는 태그와 닫히는 태그를 사용해준다.
- \<h1>...\<h6>: heading을 지정하는 태그



## 통계에 기반한 학습

- 전 세계에 있는 수 많은 웹페이지들 중 25~26개의 태그로 구성되어 있는 웹페이지가 가장 많다.
- 어떤 태그를 외울 것인지는 그 태그가 얼마나 널리 쓰이는지를 기반으로 정한다.



## 줄바꿈: \<br> vs. \<p>

- __\<br>__ 태그를 이용하면 줄바꿈을 할 수 있다. 두개를 사용하면 문단을 표현할 수 있다. 이 태그는 닫히는 태그가 존재하지 않는다.
- __\<p>__ 태그는 paragraph 단어에서 p를 따와서 만들어졌으며 어디까지가 한 단락인지 보여준다. 그래서 열리는 태그와 닫히는 태그가 존재한다.



__두 태그의 차이점__

- \<br> 태그는 줄바꿈일 뿐이고 문단을 바꿀때에는 \<p> 태그가 더 가치있다.

- \<p> 태그는 CSS를 이용해서 공백의 범위를 조절할 수 있다.



## HTML이 중요한 이유

- 검색엔진은  html 태그를 본래의 의미에 맞게 사용한 글을 위 페이지에 올려준다. 
- 바르게 쓴 html 태그는 접근성 측면에서도 중요하다.



## 촤후의 문법 속성과 img 태그



__\<img> 태그__

- src(source의 줄임말) 속성을 이용하여 원하는 이미지의 주소를 적을 수 있다.



__속성이란?__

- 속성(attribute)은 태그안에 아무 위치에나 쓰면 된다. 태그의 이름만으론 정보가 부족할 때 더 많은 의미를 부가하는 역할을 한다.



## 부모 자식과 목록

- 태그가 서로 포함관계에 있을 때, 포함하고 있는 태그를 부모 태그, 포함된 태그를 자식 태그라고 한다.
- \<li>는 목차 또는 목록을 입력할 때 사용하는 태그이다.



> __다중 커서__
>
> - 컨트롤을 누른 채 에디터 화면을 클릭하면 여러개의 커서가 생성되고 그 다음 입력을 하면 커서가 위치한 곳에 한꺼번에 태그를 입력할 수 있다.



- 서로 다른 목록을 구분하고자 할 때 \<ul>이라는 부모 태그를 사용한다.
- \<ol> (ordered list)태그를 ul 대신 이용하면 숫자를 자동으로 달아준다.



## 문서의 구조와 슈퍼스타들

- \<title>: 페이지의 제목을 설정할 때 사용
- \<meta charset="utf-8">: 브라우저가 웹페이지를 utf-8로 열도록 하는 태그
- 본문은 \<body>, 본문을 설명하는 태그는 \<head>
- \<head>와 \<body>를 감싸는 태그는 \<html>
- 가장 위에는 관용적으로 이 문서에  html이 담겨있다는 뜻에서 \<IDOTYPE HTML>을 써준다.



## HTML 태그의 제왕



__\<a> 태그__

- anchor의 앞글자를 따서 a태그임
- HyperText가 이 태그를 의미
- 링크를 넣고 싶은 곳을 a 태그로 감싸고 href(reference 의 약자)로 링크를 써줌



## 웹사이트 완성

- 링크는 본드와 실과같이 서로 연관된 웹페이지를 결합해서 하나의 책으로 엮어내는 존재
- html들을 링크로 연결해서 하나의 사이트로 만든다.



## 원시 웹

- https://info.cern.ch



## 인터넷을 여는 열쇠 서버와 클라이언트

- 웹서버가 담긴 컴퓨터에는 html 파일들이 모여 있다.
- 브라우저를 통해 인터넷으로 웹서버에 특정 html 파일을 요청하는 신호를 보내면 html 코드를 웹 브라우저에 전달하고 웹 브라우저가 html을 읽어서 정보를 전달한다.
- 요청(request)를 하는 컴퓨터를 클라이언트(client), 응답(response)하는 컴퓨터를 서버(server)라고 함

- 서버를 사용하는 방법은 두가지가 있는데 한가지는 내 컴퓨터에 서버를 설치하는 방법이고 다른 하나는 이런 일을 대행하는 다른 업체에 맡기는 것이다.



## 웹 호스팅 - 깃허브 페이지

- 웹 서버를 운영하기 위한 컴퓨터, 호스트(host)를 빌려주는 회사를 웹 호스팅 업체라고 한다.
- 깃허브를 웹 호스팅으로 사용할 수 있다. 깃허브 리포지토리에 html파일들을 올리고 setting 탭에 들어가 github pages 메뉴에서 source를 선택하고 save를 누르면 깃허브 페이지 링크가 뜨게 된다.
- html만을 서비스하는 웹 호스팅을 스태틱 웹 호스팅(static web hosting)이라고 한다.

- 나중에 PHP, 파이썬, 루비 같은 언어를 배운다면 다이내믹 웹 호스팅(Dynamic web hosting)이 필요해진다.



## 웹서버 운영하기

- 웹서버 제품군에는 아파치, IIS, 엔진엑스 등의 여러 제품이 있다.
- 아파치는 웹 서버 제품군중 점유율 1등을 차지하고 있는 웹서버이며 오픈소스이고 무료다.



__웹서버를 통해 페이지를 여는 것과 그냥 브라우저를 통해 파일을 여는 것의 차이__

- 파일을 열였을땐 file://, 웹 서버로 열었을 땐 http://가 붙는다. http는 HyperText Transfer Protocol이라는 뜻으로 웹서버가 서로 웹페이지를 주고 받기 위한 규약이다.