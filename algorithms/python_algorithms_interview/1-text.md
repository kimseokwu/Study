# 문자열 조작

문자열 조작이란 문자열을 변경하거나 분리하는 등의 여러 과정을 말한다. 대부분의 언어에서는 문자열을 조작하기 위한 다양한 기능들을 기본적으로 제공하고 있기 때문에, 굳이 제약을 두지 않는 한 언어에서 제공하는 기본 기능들을 잘 활용하는 편이 좋다.



### 유효한 펠린드롬

- 주어진 문자열이 펠린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.

> __예제__
>
> - 입력: "A man, a plan, a canal: Panama"
> - 출력: true



- 펠린 드롬이란?: 앞뒤가 똑같은 단어나 문장으로 뒤집어도 같은 말이 되는 단어 또는 문장을 팰린드롬(palindrome)이라고 한다.



__풀이 1. 리스트로 변환__

```python
def solution(s):
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    
    return True
```



__풀이 2. 데크 자료형을 이용한 최적화__

```python
def solution(s):
    strs: Deque = collections.deque()
    
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
            
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
        
    return True
```



- 리스트의 pop(0)이 O(n)인데 비해 데크의 popleft()는 O(1)이기 때문에 성능차이가 크다.



__풀이 3. 슬라이싱 사용__

```python
def solution(s):
    s = s.lower()
    # 정규식으로 불필요한 문자 제거
    s = re.sub('[a-z0-9]', '', s)

    return s[::-1] == s
```

- 파이썬은 문자열을 배열이나 리스트 처럼 자유롭게 슬라이싱할 수 있는 기능을 제공하며, [::-1]을 이용하면 뒤집을 수 있다. 내부적으로 C보다 빠르게 구현되어 있어 훨씬 더 좋은 속도를 기대할 수 있다.

  

  __문자열 슬라이싱__

- 문자열 슬라이싱은 위치를 지정하면 해당 위치의 배열 포인터를 얻게 되며 이를 통해 연결된 객체를 찾아 실제 값을 찾아내는데, 이 과정은 매우 빠르게 진행되므로 문자열을 조작할 때는 항상 슬라이싱을 우선으로 사용하는 편이 속도 개선에 유리하다. 문자열을 별도로 리스트로 매핑하는 등의 처리는 데이터 구조를 다루는 입장에서는 좋은 방법이지만, 별도 자료형으로 매핑하는 과정에서 상당한 연산 비용이 필요하므로 전체적인 속도에서는 오히려 손해를 볼 수 있다.



### 문자열 뒤집기

- 문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며 리턴 없이 리스트 내부를 직접 조작하라.

> __예제__
>
> - 입력: ["h", "e", "l", "l", "o"]
> - 출력: ["o", "e", "l", "l", "h"]



__풀이 1. 투 포인터를 이용한 스왑__

- 투포인터는 단어 그대로 2개의 포인터를 이용해 범위를 조정해가며 풀이하는 방식을 말한다. 문제에서 리턴 없이 리스트 내부를 직접 조작하라는 제약사항이 있으므로 다음과 같이 s 내부를 스왑하는 형태로 풀이하면 된다.

```python
def solution(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[rigth] = s[right], s[left]
        left += 1
        right -= 1
```



__풀이 2. 파이썬다운 방식__

- 파이썬의 기본 기능 reverse를 이용하면 한 줄로 쉽게 풀이할 수 있다.

```python
def solution(s):
    s.reverse()
```



### 로그파일 재정렬

- 로그를 재정렬하라. 기준은 다음과 같다.
  1. 로그의 가장 앞 부분은 식별자다
  2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다
  3. 식별자는 순서에 영향을 끼치지 않지만 문자가 동일할 경우 식별자 순으로 한다.
  4. 숫자로그는 입력순서대로 한다.

> __예제__
>
> 입력:  logs = ['dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dig', 'let3 art zero']
>
> 출력: ['let1 art can', 'let3 art zero', 'let2 own kit dig', 'dig1 8 1 5 1', 'dig2 3 6' ]



__풀이 1. 람다와 + 연산자를 사용__

- 문자로 구성된 로그가 숫자 로그보다 이전에 오며 숫자 로그는 입력순서대로 둔다. 그렇다면 문자와 숫자를 구분하고, 숫자는 나중에 그대로 이어 붙인다.

- isdigit()을 이용하여 숫자 여부를 판별해 구분한다.

```python
def solution(logs):
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigt():
            digits.append(log)
        else:
            letters.append(log)
            
    # 2개의 키를 람다 표현식으로 정렬
    letter.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits
```



### 가장 흔한 단어

- 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며 구두점 또한 무시한다.

> __예제__
>
> - 입력: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit", banned = ['hit']
> - 출력: "ball"



__풀이 1. 리스트 컴프레헨션__

- 입력값에는 대소문자가 섞여 있으며 쉼표 등 구두점이 존재한다. 따라서 데이터클렌징이라 부르는 입력값에 대한 전처리 작업이 필요하다. 정규식을 섞어 처리한다.

- defautldict(int)를 사용해 int값이 기본으로 부여되게 해서 단어의 갯수를 센다. max()함수에 key를 지정해 argmax를 간접적으로 추출한다.
- 혹은 collections의 Counter 모듈을 이용해 most_common으로 추출한다.

```python
def solution(paragraph, banned):
    words = [word for word in re.sub('[^\w]', ' ', paragraph).lower().split() if word not in banned]
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]
```



### 그룹 애너그램

- 문자열 배열을 받아 애너그램 단위로 그룹핑하라.

> __예제__
>
> - 입력: ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
> - 출력: [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']]
> - 애너그램이란?: 일종의 언어유희로 문자을 재배열하여 다른 뜻을 가진 단어로 바꾸는 것을 말한다.



__풀이 1. 정렬하여 딕셔너리 추가__

- 애너그램을 판단하는 가장 간단한 방법은 정렬하여 비교하는 것이다. sorted()는 문자열도 잘 정렬하며 여기서 출력된 리스트를 join()으로 다시 합쳐 이 값을 키로 하는 딕셔너리를 구성한다.

```python
def solution(strs):
    anagrams = collections.defauldict(list)
    
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
        
    return list(anagrams.values())
```



__여러가지 정렬 방법__

- 파이썬은 정렬 함수를 기본으로 제공한다. 파이썬에서 시작된 고성능 정렬 알고리즘은 팀소트이다. 
- sorted()는 문자열과 리스트를 잘 정렬하며 리스트 자료형은 sort() 메소드를 함께 제공한다. 이를 제자리 정렬이라고 부르는데, 일반적으로 제자리 정렬 알고리즘은 입력을 출력으로 덮어 쓰기 때문에 별도의 추가 공간이 필요하지 않으며 리턴값이 없다. 따라서 정렬 결과를 별도로 리턴하는 sorted()와 다르므로 주의가 필요하다.
- sorted는 key= 옵션을 지정해 정렬을 위한 키 또는 함수를 별도로 지정할 수 있다.
- 팀소트는 실제 데이터는 대부분 어느정도 이미 정렬되어 있을 것이다라고 가정하고 실제 데이터에서 고성능을 낼 수 있도록 설계한 알고리즘이다.
- 팀소트 알고리즘은 시간복잡도가 평균 O(n log n)이다.



### 가장 긴 팰린드롬 부분 문자열

- 가장 긴 팰린드롬 부분 문자열을 출력하라.

> __예제__
>
> - 입력: "babad"
> - 출력: "bab"



__풀이 1. 중앙을 중심으로 확장하는 풀이__

- 컴퓨터과학의 오랜 문제중에 최장 공통 부분 문자열이라는 문제가 있다. 여러개의 입력 문자열이 있을 때 서로 공통된 가장 긴 부분 문자열을 찾는 문제로, 다이나믹 프로그래밍으로 풀 수 있는 전형적인 문제다. 이 문제 또한 다이나믹 프로그래밍으로 풀 수 있지만 직관적으로 이해가 어렵고 일반적인 예상과 달리 실행속도가 늦다.
- 팰린드롬 판별만 하면 된다는 점에 착안해서, 매칭이 될 때 중앙을 중심으로 점점 확장해 나가면서 가장 긴 팰린드롬을 판별하는 알고리즘을 구현해보자.

```python
def solution(s):
    # 팰린드롬 판별 및 투포인터 확장
    def expand(left, right):
        while left >= 0, and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    # 해당 사항이 없을 때 빠르게 리턴
    if len(s) < s or s == s[::-1]:
        return s
    
    result = ''
    # 슬라이딩 윈도우 우측으로 이동
    for i in range(len(s) - 1):
        result = max(result, 
                    expand(i, i + 1),
                    expand(i, i + 2),
                    key=len)
```



__유니코드와 UTF-8__

초기에 문자를 표현하던 대표적은 방식은 ASCII 인코딩 방식으로 1바이트에 모든 문자를 표현했다. 게다가 1은 체크섬으로 제외하여 7비트, 즉 128글자로 문자를 표현햇다. 그러다 보니 한글이나 한자 같은 문자는 2개 이상의 특수문자를 합쳐서 표현하곤 했는데, 이런 방식으론 표현하지 못했다. 이런 문제를 해결하기 위해 2~4 바이트 공간에 여유있게 문자를 할당하고자 등장한 방식이 유니코드다.

그러나 유니코드 자체는 메모리 낭비가 심해서 이를 가변 길이 문자 인코딩 방식으로 효율적으로 인코딩하는 대표적인 방식이 UTF-8이다.

만약 모든 문자를 4바이트로 표현한다면 python은 24바이트의 메모리를 차지하게 될 것이다. 영문자는 각 문자당 1바이트로 충분한데 3바이트씩 낭비가 되고 있다. UTF-8은 첫 바이트의 맨 앞비트를 확인해서 0이면 1바이트, 10이면 특정 문자의 중간 바이트,  110이면 2바이트, 1110이면 3바이트, 11110이면 4바이트라는 식으로 문자 바이트의 길이를 인식할 수 있다. 약 100만자 정도를 표현할 수 있게 됐다.