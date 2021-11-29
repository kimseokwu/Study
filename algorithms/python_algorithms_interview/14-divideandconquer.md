# 분할 정복

- 분할 정복은 다중 분기 재귀를 기반으로 하는 알고리즘 디자인 패러다임을 말한다.
- 분할 정복은 직접 해결할 수 있을 정도로 간단한 문제가 될 때까지 문제를 재귀적으로 쪼개나간 다음, 그 하위 문제의 결과들을 조합하여 원래 문제의 결과로 만들어 낸다.

__분할정복 수도 코드__

```
function F(x):
	if F(x)가 간단 then:
		return F(x)를 계산한 값
	
	else:
		x를 x1, x2로 분할
		F(x1)과 F(x2)를 호출
		return F(x1), F(x2)로 F(x)를 구한 값
```



### 과반수 엘리먼트

- 과반수를 차지하는 절반을 초과하는 엘리먼트를 출력하라

> __예제__
>
> - 입력: [3, 2, 3]
> - 출력: 3



__풀이 1. 다이나믹 프로그래밍__

- 한 번 카운트를 계산한 값은 저장해서 재활용한다.

```python
def solution(nums):
    counts = collections.defaultdict(int)
    for num in nums:
        if counts[num] == 0:
            counts[num] = nums.count(num)
        
        if counts[num] > len(nums) // 2:
            return num
```



__풀이 2. 분할 정복__

- 쪼갠 후 과반수 후보군에 해당하는 엘리먼트만 리턴하면서 계속 위로 올려주면 최종적으로 정답이 남게 된다.

```python
def solution(nums):
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]
    
    half = len(nums) // 2
    a = solution(nums[:half])
    a = solution(nums[half:])
    
    return [b, a][nums.count(a) > half]
```



__풀이 3. 파이썬다운 방식__

- 정렬하여 가운데를 지정하면 반드시 과반수 이상인 엘리먼트일 것이다.

```python
def solution(nums):
    return sorted(nums)[len(nums) // 2]
```





### 괄호를 삽입하는 여러가지 방법

- 숫자와 연산자를 입력받아 가능한 모든 조합의 결과를 출력하라

> __예제__
>
> - 입력: "2-1-1"
> - 출력: [0, 2]



__풀이 1. 분할 정복을 이용한 다양한 조합__

- *, -, + 연산자가 등장할 때 좌/우 분할을 하고 각각 계산 결과를 리턴한다.
- 연산자를 기준으로 재귀로 left, right로 계속 분할하고 분할된 값은 compute()  함수로 계산한 결과를 extend()로 확장한다.

```python
def solution(input):
    def compute(left, right, op):
        result = []
        
        for l in left:
            for r in right:
                result.append(eval(str(l) + op + str(r)))
        return result
    
    if input.isdigit():
        return [int(input)]
    
    results = []
    for index, value in enumerate(input):
        if value in '-+*':
            left = solution(input[:index])
            right = solution(input[input + 1:])
            
            results.extend(compute(left, right, value))
    
    return results
```

