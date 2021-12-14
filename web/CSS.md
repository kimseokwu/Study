# CSS



## CSS의 등장

- <!=- ... -->: HTML 주석처리
- \<style> 태그: head에 스타일 태그를 사용하고 스타일 태그 안의 내용은 CSS로 작성한다.
- 모든 a 태그에 대해서 빨간색으로 처리하기

```html
<style>
    a {
        color: red;
    }
</style>
```



- CSS는 여러 태그를 쓸 일을 한 줄로 줄여주면서 코드의 가독성을 높인다.



## CSS의 기본문법

- \<style> 태그 이외에 html속에 CSS를 포함시킬 수 있는 방법이 하나 더 있는데 'style' 속성을 이용하는 방법이다. style 속성을 사용하면 그 속성의 값을 웹 브라우저가 CSS 문법에 따라 해석해서 그 결과를 style 속성이 위치하는 태그에 적용된다.
- style은 html의 속성이고 값으로 반드시 CSS 효과가 들어온다고 약속돼있다.
- \<style> 태그에  CSS를 작성하기 위해선 누구에게 효과를 줄 지 대상이 들어가야한다. 이런 코드를 효과를 누구에게 줄 것인가 선택한다는 점에서 선택자(selector)라고 한다. 그리고 선택자에게 지정될 효과를 declaration이라고 부른다.
- 하나의 선택자에 여러개의 효과를 지정할 땐 세미콜론으로 구분한다.

```html
<li><a href="2.html" style="color:red; text-decoration:underline;">CSS</a></li>
```



## CSS 속성을 스스로 알아내기



- 글씨 크기를 바꾸고 싶다!
  - css text size property 검색
  - font-size 속성과 여러가지 value 찾아냄
- 텍스트를 가운데로 정렬하고 싶다!
  - css text center property 검색
  - text-align 속성 찾아냄



## CSS 선택자의 기본

- 태그 선택자
- 클래스 선택자: 여러 태그를 클래스로 묶어서 제어, 한 태그에 여러 클래스가 부여될 수 있고 띄어쓰기로 구분
- id 선택자: 가장 우선되는 선택자, 중복되는 것이 불가함



## 박스 모델

- html의 태그들은 태그와 성격과 일반적인 쓰임에 따라 화면 전체를 쓰는 것이 편한 것과 자신의 크기만큼의 부피를 갖는 게 편한 것이 있기 때문에 화면 전체를 쓰는 태그가 있고, 자기 크기만큼 쓰는 것들이 있다.
- 화면 전체를 쓰는 태그들을 블록 레벨 엘리먼트(block level element), 자기 자신의 콘텐츠 크기만큼을 쓰는 태그들을 인라인 엘리먼트(inline element)라고 한다.
- display 속성을 이용하면 블록 레벨 엘리먼트도 인라인 엘리먼트처럼 자신의 부피만큼 쓰게 할 수 있다.



__코드의 압축__

- 여러 선택자에 동일한 효과가 적용된다면 콤마로 한꺼번에 효과를 적용해줄 수 있다.

```html
<style>
    a, h1{
        border-width: 5px;
        border-color: red;
        border-style: solid;
    }
</style>
```

- 위의 코드를 보면 border 부분이 중복된다. 다음과 같이 줄일 수 있다.

```html
<style>
    a, h1 {
        border: 5px red solid;
    }
</style>
```



__박스 모델__

- 콘텐츠와 테두리 사이의 여백을 주고 싶다면 padding 값을 추가할 수 있다.
- margin 속성을 0으로 주면 두 엘리먼트의 테두리 사이의 간격을 없앨 수 있다

- h1 태그는 화면 전체를 사용하는 블록레벨 엘리먼트다. 이를 바꾸기 위해 width 값을 지정하면 태그의 크기가 변한다. 높이는 height로 지정한다.
- 태그에서 콘텐츠는 border를 기준으로 밖으로는 margin, 안으로는 padding이 감싸고 있다.





## 박스모델 써먹기

- 제목 부분 아래에 줄을 긋기 위해서 border-bottom을 사용한다.
- ol 오른쪽에 줄을 긋기위해 boder-right를 사용한다
- 각 영역의 margin과 padding을 정해주고 body의 margin을 0으로 설정한다.



## 그리드

- \<div>: 그냥 평범한 개체를 태그로 묶고 싶을 때 무색무취의 태그, division의 약자, 블록레벨 엘리먼트
- \<span>: div와 같은 목적의 태그, 인라인 엘리먼트



__그리드 사용__

- display: grid; 속성 지정
- grid-template-columns: 150px 1fr;
- 두개의 태그를 div id="grid"로 묶은 뒤, grid에 diplay: grid 속성을 지정해준다.



## 미디어 쿼리 

- 반응형 웹디자인: 화면 크기에 따라 웹 페이지의 다양한 요소들이 반응해서 최적화된 모양으로 바뀌는 것
- 미디어 쿼리는 반응형 디자인을 CSS를 통해 구현하는 핵심적인 개념이다.
- 화면크기가 800px를 넘으면 div를 출력하지 않는 코드

```html
<style>
    @media(min-width: 800px) {
        div {
            display: none;
        }
    }
</style>
```



## CSS 코드의 재사용

- 각 페이지마다 중복된 CSS코드를 style.css 파일에 붙여 넣는다.
- \<link>태그를 이용해 CSS 파일을 각 페이지에 연결한다. 이러면 웹 브라우저가 link를 따라 style.css 파일을 다운받고 html 코드에 적용해준다.

```html
<link rel="stylesheet" href="style.css" />
```

