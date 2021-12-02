# 정렬



## K 번째 수

- start와 end를 input으로 받아 sorted하고 k번째 수를 인덱싱으로 뽑는다.

```python
def solution(array, commands):
    answer = []
    for command in commands:
        # start, end 저장
        start = command[0] - 1
        end = command[1]
        k = command[2] - 1
        
        # 자른 배열 sorted
        temp = sorted(array[start:end])
        answer.append(temp[k])
    return answer
```





## 가장 큰 수

- 처음엔 정렬로 접근했지만 numbers에 들어오는 숫자의 자릿수가 모두 다를 가능성이 있어서 잘 풀리지 않았다. 예를 들어 3, 30이 들어올경우 330이 맞는 답이지만 단순히 정렬로 풀면 303이 되어버린다.
- 검색을 통해 다른 사람들의 풀이를 참고하니 functools.cmp_to_key 메소드를 쓴 풀이가 눈에 띄었다.
- cmp_to_key는 sorted와 같은 정렬 함수의 key 매개변수에 함수를 전달할 때 사용되는 함수로, 두개의 인수를 받아들이고 첫번째 인수를 기준으로 그들을 비교하여 작으면 음수, 같으면 0, 크면 양수를 반환하는 비교함수여야 한다.

__cmp-to-key 예시__

```python
import functools

def xy_compare(n1, n2):
    if n1[1] > n2[1]:         # y 좌표가 크면
        return 1
    elif n1[1] == n2[1]:      # y 좌표가 같으면
        if n1[0] > n2[0]:     # x 좌표가 크면
            return 1
        elif n1[0] == n2[0]:  # x 좌표가 같으면
            return 0
        else:                 # x 좌표가 작으면
            return -1
    else:                     # y 좌표가 작으면
        return -1

src = [(0, 4), (1, 2), (1, -1), (2, 2), (3, 3)]
result = sorted(src, key=functools.cmp_to_key(xy_compare))
print(result)
```

- cmp_to_key는 정렬을 할 때, 대소관계를 새로 정의할 수 있는 유용한 함수로 꼭 암기해둬야겠다고 생각했다.

```python
# 모범 답안
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer
```



## H-Index

- citations를 내림차순으로 정렬하여 반복문을 돌면서 h번 이상 인용된 논문의 갯수가 몇개 포함되어 있는지 체크할 수 있도록 한다.
- max를 이용해 h를 계속 최댓값으로 업데이트하여 최댓값을 리턴하도록 한다.

```python
def solution(citations):
    # 내림차순 정렬
    citations.sort(reverse=True)
    h = 0 
    
    # 반복문을 돌면서 h값 최대화
    for i in range(len(citations)):
        if citations[i] >= i+1: 
            h = max(h, i+1)
    return h
```

