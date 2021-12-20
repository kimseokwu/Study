# 자바스크립트

- 웹페이지는 한 번 화면에 출력되면 자기 자신을 바꾸는 능력이 없다. 그것을 가능하게 해주는 것이 자바스크립트이다.



## \<script> 태그

- 자바스크립트 코드를 넣을 때는 웹 브라우저에게 지금부터 자바스크립트 코드가 시작된다는 사실을 알려야 한다. 그때 사용하는 태그가 script 태그다.



## 이벤트

- 이벤트는 자바스크립트가 사용자와 상호작용하는 데 핵심적인 역할을 한다.
- \<input type="button" value="이름" onclick="alert('hi')"> 라고 작성하면 누르면 경고창이 뜨는 버튼을 생성할 수 있다.
- \<input type="text"> 라고 작성하면 텍스트창을 띄울 수 있으며 onkeydown, onchange등의 속성을 추가할 수 있다.
- 이렇게 on으로 시작하는 속성들을 자바스크립트에서 이벤트라고 하며 웹 브라우저에서 일어나는 여러 사건중 기념할 만한 10~20개의 이벤트를 정의해놨고 이것들을 이용해 사용자와 상호작용할 수 잇는 코드를 작성할 수 있다.



## 콘솔

- 브라우저에서 오른쪽 마우스 버튼을 누르면 검사 탭이 있고 여기에 들어가면 console을 사용할 수 있다.
- console은 자바스크립트 코드르 즉석에서 실행할 수 있는 도구다.



## 데이터 타입 - 문자열과 숫자

- 자바스크립트에는 6개의 데이터 타입이 있고 객체라는 것이 있다.
- 자바스크립트의 데이터 타입
  - boolean
  - Null
  - undefined
  - Number
  - string
  - symbol
- 숫자는 산술연산자(+, - , *, /)를 통해 더하기 빼기 곱하기 나누기가 가능하다.

- 문자열은 따옴표 혹은 작은 따옴표로 표시되어 있다
- 문자열 함수
  - .length: 문자열의 길이 출력
  - .trim(): 공백 제거
  - .indexOf(): 해당 문자열의 시작 인덱스
  - toUpperCase(): 대문자로 변환



## 변수와 대입 연산자



- 변수(variable): 바뀔 수 있는 값, x = 1;과 같은 식으로 선언
- 상수(constant): 바뀌지 않는것

- 변수를 선언할 때는 var 키워드를 앞에 써준다.



## 웹브라우저 제어

- document.querySelector(selectors); 로 스타일을 적용할 태그를 선택할 수 있다.
- 버튼을 눌렀을 때 배경색을 바꾸고싶으면 input 태그에onclick="document.querySelector(body).style.backgroundColor = 'black'" 속성을 추가한다



## 조건문

- 토글(toggle): 버튼 하나로 어떤 기능을 변화시켰다가 원래로 돌아왔다가 하게하는 것

- 이 기능은 if 조건문으로 구현될 수 있다.



__비교연산자와 불리언(boolean)__

- 비교연산자 '===': 같으면 true, 다르면 false를 출력한다. true와 false 두 가지 값을 묶어서 불리언(boolean)이라고 부른다.
- \&lt; : HTML에선 <가 태그를 여는 데 사용되기 때문에 < 부등호를 표시할 때 less than이라는 뜻에서 '\&lt;'이라고 쓴다.

```javascript
if (true or false) {
    // 조건문
} else {
    // 조건문
}
```



## 중복의 제거를 위한 리팩터링

- 리팩터링(refactoring): 코드 자체를 효율적으로 만들어서 그 코드의 가독성을 높이고, 유지보수를 편리하게 만들고, 중복된 코드를 줄이는 방향으로 코드를 개선하는 작업

- this: onclick과 같이 이벤트 안에서 실행되는 코드에서 현재 코드가 속해 있는 태그를 가리키도록 약속돼 있는 특수한 키워드

```html
     <input id="night_day" type="button" value="night" onclick="
    if(document.querySelector('#night_day').value === 'night') {
      document.querySelector('body').style.backgroundColor = 'black';
      document.querySelector('body').style.color = 'white';
      document.querySelector('#night_day').value = 'day';
    } else {
      document.querySelector('body').style.backgroundColor = 'white';
      document.querySelector('body').style.color = 'black';
      document.querySelector('#night_day').value = 'night';
    }">

<!-- 바꾼 후 -->

    <input type="button" value="night" onclick="
    if(this.value === 'night') {
      document.querySelector('body').style.backgroundColor = 'black';
      document.querySelector('body').style.color = 'white';
      this.value = 'day';
    } else {
      document.querySelector('body').style.backgroundColor = 'white';
      document.querySelector('body').style.color = 'black';
      this.value = 'night';
    }">
```



__중복되는 부분 변수에 할당하기__

- var로 target 변수를 선언하고 document.querySelector('body')를 변수에 넣어준다.

```html
    <input type="button" value="night" onclick="
    var target = document.querySelector('body');
    if(this.value === 'night') {
      target.style.backgroundColor = 'black';
      target.style.color = 'white';
      this.value = 'day';
    } else {
      target.style.backgroundColor = 'white';
      target.style.color = 'black';
      this.value = 'night';
    }">
```



## 반복문

- night 버튼을 눌렀을 때 <a> 태그에 style 속성이 추가 되며 powderblue 색상이 적용되도록 하려고 한다.

- 이를 위해서 웹페이지의 모든 \<a> 태그를 가져와서 하나하나에 반복적으로 powderblue 색상을 적용하도록 한다. 



__배열(Array)__

- 데이터 중에서 서로 연관된 데이터들을 잘 정리 정돈해서 담아두는 일종의 수납 상자를 배열이라고 한다.

- 배열은 대괄호 안에 값들을 따옴표와 콤마로 구분하여 변수에 넣는다.

``` javascript
var coworker = ["egoing", "leezche"]
```

- 배열 안의 값들은 인덱스(index)를 통해 가리킬 수 있다. (coworker[0])
- coworker.length를 이용하면 배열안에 몇개의 값이 있는지 알려준다.
- coworker.push()를 이용해 배열 끝에 아이템을 추가할 수 있다.



__while 문__

- 제어문의 값이 true일 동안 코드를 반복적으로 실행한다.
- while 반복문을 이용해 2, 3번째 코드를 3번 반복

```html
<script>
	document.write('<li>1</li>');
    var i = 0;
    while(i < 3) {
        document.write('<li>2</li>')
        document.write('<li>3</li>')
        i = i + 1
    }
    document.write('<li>4</li>')
</script>
```



- 코드를 배열의 길이만큼 반복하기

```html
<script>
	var coworkers = ["egoing", "leezche", "duru", "taeho"]
</script>
<h2>co workers</h2>
<ul>
   <scipt>
       var i = 0;
       while(i < coworkers.length) {
                   document.write('<li><a href="http://"a.com/' + coworkers[i] + '">"' + coworkers[i] + '</a></li>');
                   i = i + 1;
       }
   </scipt> 
</ul>
```



__배열과 반복문의 활용__

- querySelectorAll(): 현재 코드의 모든 태그를 가져오는 명령어
- 모든 a 태그의 색을 powderblue로 바꾸기

```javascript
var alist = document.querySelectorAll('a');
      var i = 0;
      while(i < alist.length) {
        alist[i].style.color = 'powderblue';
        i = i + 1;
```



## 함수

- 함수의 기본적인 문법

```html
<script>
	function two() {
        document.write('<li>2-1</li>')
        document.write('<li>2-1</li>')
    }
</script>
```



- 매개변수(parameter): 함수의 입력
- 인자(argument): 출력, return과 관련이 있음

```html
<script>
	function sum(left, right){
        document.write(left + right + '<br>')
    }
</script>
```



- return 문

```html
<script>
	function sum2(left, right) {
        return left + right
    }
</script>
```



- 최종 night 버튼 함수

```html
  <script>
      function nightDayHandler(self) {
        var target = document.querySelector('body');
        if(self.value === 'night') {
          target.style.backgroundColor = 'black';
          target.style.color = 'white';
          self.value = 'day';

          var alist = document.querySelectorAll('a');
          var i = 0;
          while(i < alist.length) {
            alist[i].style.color = 'powderblue';
            i = i + 1;
          }
        } else {
          target.style.backgroundColor = 'white';
          target.style.color = 'black';
          self.value = 'night';

          var alist = document.querySelectorAll('a');
          var i = 0;
          while(i < alist.length) {
            alist[i].style.color = 'blue';
            i = i + 1;
          }
        }
      }
    </script>
```



## 객체(object)

- 객체: 서로 연관된 함수와 변수를 정리 정돈하기 위한 수납상자, 객체는 정보를 순서없이 저장할 수 있음
- 객체 리터럴(object literal): 객체를 만들 때 사용하는 기호

```html
<script>
	var coworkers = {
        "programmer":"egoing",
        "designer":"leezche"
    }
    document.write("programmer :" + coworkers.programmer + "<br>");
    document.write("designer :" + coworkers.designer + "<br>");
    
    <!-- 객체에 데이터 추가 -->
    coworkers.bookkeeper = "duru";
    document.write("bookkeeeper :" + coworkers.bookkeeper + "<br>");
</script>
<h2>Iterate</h2>
<script>
    <!-- 객체 반복문으로 순회하기 -->
	for (var key in coworkers) {
        document.write(coworkers[key] + '<br>')
    }
</script>
```



__객체 프로퍼티와 메서드__

- 객체에는 문자열, 배열, 숫자, 함수등을 담을 수 있다.

```html
<h2>property & Method</h2>
<script>
  coworkers.showAll = function() {
      for(var key in this) {
          document.write(key + ' : ' + coworkers[key] + '<br>')
      }
  }
</script>
```



__객체의 활용__

- 배경색 변경, 글자색 변경, 링크색 변경을 객체로 관리하기

```html
<script>
      var Body = {
        setColor: function(color) {
          document.querySelector('body').style.color = color;
        },
        setBackgroundColor: function(color) {
          document.querySelector('body').style.backgroundColor = color;
        }
      }
      var Links = {
        setColor: function(color) {
          var alist = document.querySelectorAll('a');
          var i = 0;
          while(i < alist.length) {
            alist[i].style.color = color;
            i = i + 1;
          }
        }
      }
      function nightDayHandler(self) {
        var target = document.querySelector('body');
        if(self.value === 'night') {
          Body.setBackgroundColor('black');
          Body.setColor('white');
          self.value = 'day';

          Links.setColor('powderblue');
        } else {
          Body.setBackgroundColor('white');
          Body.setColor('black');
          self.value = 'night';

          Links.setColor('blue');
        }
      }
    </script>
```



## 파일로 쪼개서 정리 정돈하기

- .js 파일에 script 태그 안 코드들을 옮겨 적고 \<script src="color.js">\</script>로 불러온다.

  

- 이렇게  js를 다른 파일로 쪼개서 정리하면 웹 브라우저가 페이지를 불러올 때 js를 캐시로 저장하기 때문에 한 번 파일을 읽은 뒤 그 파일을 다시 읽지 않아도 된다.



## 라이브러리와 프레임 워크

- 라이브러리: 내가 만들고자 하는 프로그램에 필요한 부품들이 되는 소프트웨어들을 잘 정리 정돈 해놓은 곳
- 프레임워크:  만들고자 하는 기능이나 특성에 따라 달라지는 부분만 살짝살짝 수정하는 방법으로 우리가 만들고자 하는 것을 처음부터 끝까ㅏ지 만들지 않게 해주는 거의 반제품과 같은 것
