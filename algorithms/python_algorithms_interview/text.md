- 문자열 조작이란 문자열을 변경하거나 분리하는 등의 여러 과정을 말한다.

# 유효한 펠린드롬
주어진 문자열이 펠린드롬인지 확인하라, 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.

* 펠린드롬 : 앞뒤가 똑같은 단어나 문장

입력 : “A man, a plan, a canal : Panama”
출력 : true


## <풀이 1> 리스트로 변환

```python
strs = []
for char in s:
    if char.isalnum(): # isalnum() : 영문자, 숫자 여부를 판별하는 함수
        strs.append(char.lower())

while len(strs) >.1:
    if strs.pop(0) != strs.pop():
        return False
    return True
```

## <풀이 2> 데크 자료형을 이용한 최적화

```python
def isPallindrome(self, s:str) -> bool:
    strs : Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True
```

- pop(0)이 O(n)인데 비해 popleft()는 O(1)이기 때문이다.


## <풀이 3> 슬라이싱 사용

```python
def isPallindrom(self, s: str) -> bool:
    s = s.lower()
    s = re.sub(‘[^a-z0-9]’, ‘’, s)

    return s == s[::-1] #슬라이싱
```

*풀이 속도: 풀이 1 > 풀이 2 > 풀이 3

- 파이썬의 문자 슬라이싱은 내부적으로 매우 빠르게 동작한다. 문자열을 조작할 때는 항상 슬라이싱을 우선으로 사용하는 편이 속도 개선에 유리하다.

# 로그 파일 재정렬

로그를 재정렬하라. 기준은 다음과 같다.
1. 로그의 가장 앞 부분은 식별자다.
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
3. 식별자는 순서에 영향을 끼치지 않지만 문자가 동일할 경우 식별자 순으로 한다.
4. 숫자 로그는 입력 순서대로 한다.

## <풀이> 람다 표현식과 + 연산자 활용

```python
def rearrange_logs(logs):
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    #선순위 문자열, 후순위 식별자로 정렬
    return letters + digits
```

# 가장 흔한 단어

금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다.

입력: paragraph = “Bob hit a ball, the hit BALL flew far after it was hit”
banned = [“hit”]

출력: ball

## <풀이 1> 리스트 컴프리헨션, counter 객체 사용

```python
def mostCommonWord(paragraph, banned):
    word = [word for word in re.sub(r’[^\w]’, ‘ ‘, paragraph).lower().split() if word not in banned]
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]
```

- \w : 단어문자를 뜻하는 정규식


# 그룹 애너그램

문자열 배열을 받아 애너그램 단위로 그룹핑하라

입력 : ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
출력 : [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

## <풀이> 정렬하여 딕셔너리에 추가

- 애너그램을 판단하는 가장 간단한 방법은 정렬하여 비교하는 것이다. 애너그램 관계인 단어들을 정렬하면 서로 같은 값을 갖게 되기 때문이다.

```python
def groupAnagrams(strs):
    import collections
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())
```

- sorted()는 정렬된 리스트를 리턴하고 .sort()는 제자리 정렬로 입력을 출력으로 덮어 쓰고 리턴값이 없다.
- alist = blist.sort()는 잘못된 구문
- 파이썬의 sorted()는 팀소트를 사용한다.

# 가장 긴 펠린드롬 부분 문자열

가장 긴 펠린드롬 부분 문자열을 출력하라.

입력: “babad”
출력: “bab”

입력: “cbbd”
출력: “bb”

## <풀이 1> 중앙을 중심으로 확장하는 풀이

```python
def longest(s):
    # 펠린드롬 판별 및 투 포인터 확장
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]

    # 해당 사항이 없을 때 빠르게 리턴
    if len(s) < 2 or s == s[::-1]:
        return (s)

    result = ''

    # 슬라이딩 윈도우 우측으로 이동
    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 2), expand(i, i + 1), key=len)

    return result
```
