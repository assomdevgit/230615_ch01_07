"""
# 리스트 응용

## 리스트 조작하기

### 리스트에 요소 추가하기

리스트의 대표적인 기능이 바로 요소 추가입니다. 다음과 같이 리스트에 요소를 추가하는 메서드는 3가지가 있습니다.

* `append`: 요소 하나를 추가
* `extend`: 리스트를 연결하여 확장
* `insert`: 특정 인덱스에 요소 추가

### 기존 리스트에 요소 하나 추가하기
"""

l = list(range(0, 10, 2))
print(l)
l.append(100)
print(l)
l.extend([200, 1000])
print(l)
l.insert(0, 10) # 인덱스, 값
print(l)

l.append([100, 1000])
print(l)
l.extend([100, 1000])
print(l)

# 물론 빈 리스트에 값을 추가할 수도 있습니다.

"""### 리스트 안에 리스트 추가하기"""

# append는 append(리스트)처럼 리스트를 넣으면 리스트 안에 리스트가 들어갑니다.

"""append는 항상 리스트의 길이가 1씩 증가합니다.

### 리스트 확장하기

그러면 리스트에 요소를 여러 개 추가하려면 어떻게 해야 할까요? append를 여러 번 사용하는 방법도 있지만, 추가할 요소가 많은 경우에는 상당히 번거롭습니다. 이때는 extend를 사용합니다.
"""

# extend(리스트)는 리스트 끝에 다른 리스트를 연결하여 리스트를 확장합니다.

"""extend의 동작을 좀 더 정확하게 이야기하면 extend에 전달된 요소를 반복하면서 각 요소를 리스트 a에 추가하는 것입니다. 따라서 리스트와 리스트를 연결한 모양이 됩니다.

### 리스트의 특정 인덱스에 요소 추가하기

append, extend는 리스트 끝에 요소를 추가합니다. 그러면 원하는 위치에 요소를 추가하는 방법은 없을까요? 이때는 insert를 사용합니다.
"""

# insert(인덱스, 요소)는 리스트의 특정 인덱스에 요소 하나를 추가합니다.

"""insert에서 자주 사용하는 패턴은 다음 2가지입니다.

* `insert(0, 요소)`: 리스트의 맨 처음에 요소를 추가
* `insert(len(리스트), 요소)`: 리스트 끝에 요소를 추가

"""



# insert에 마지막 인덱스보다 큰 값을 지정하면 리스트 끝에 요소 하나를 추가할 수 있습니다.

"""len(리스트)는 마지막 인덱스보다 1이 더 크기 때문에 리스트 끝에 값을 추가할 때 자주 활용합니다. (=append)"""

# 특히 insert는 요소 하나를 추가하므로 insert에 리스트를 넣으면 append처럼 리스트 안에 리스트가 들어갑니다. (중첩 리스트)

# 만약 리스트 중간에 요소 여러 개를 추가하고 싶다면 슬라이스에 요소 할당하기를 활용하면 됩니다.

"""### 리스트에서 요소 삭제하기

이번에는 리스트에서 요소를 삭제하는 방법입니다. 다음과 같이 요소를 삭제하는 메서드는 2가지가 있습니다.

* `pop`: 마지막 요소 또는 특정 인덱스의 요소를 삭제
* `remove`: 특정 값을 찾아서 삭제

### 리스트에서 특정 인덱스의 요소를 삭제하기

pop()은 리스트의 마지막 요소를 삭제한 뒤 삭제한 요소를 반환합니다.
"""

print(f"l : {l}")
l.remove(100)
print(f"l : {l}")
print(l.pop())
print(f"l : {l}")
print(f"l.pop(2) : {l.pop(2)}")
print(f"l : {l}")


"""그러면 원하는 인덱스의 요소를 삭제할 수는 없을까요? 이때는 pop에 인덱스를 지정하면 됩니다."""

# pop(인덱스)는 해당 인덱스의 요소를 삭제한 뒤 삭제한 요소를 반환합니다.



# 사실 pop 대신 del을 사용해도 상관없습니다.

"""### 리스트에서 특정 값을 찾아서 삭제하기

pop이나 del은 인덱스로 요소를 삭제했는데, 리스트에서 원하는 값을 찾아서 삭제하고 싶을 수도 있습니다. 이런 경우에는 remove를 사용합니다.
"""

# remove(값)은 리스트에서 특정 값을 찾아서 삭제합니다.

# 만약 리스트에 같은 값이 여러 개 있을 경우 처음 찾은 값을 삭제합니다.
# while -> value in ... -> 계속 반복.


"""### 리스트에서 특정 값의 인덱스 구하기"""

# index(값)은 리스트에서 특정 값의 인덱스를 구합니다.
# 이때 같은 값이 여러 개일 경우 처음 찾은 인덱스를 구합니다(가장 작은 인덱스).
print(f"l.index(6) : {l.index(6)}")
"""### 특정 값의 개수 구하기"""

# count(값)은 리스트에서 특정 값의 개수를 구합니다.
l2 = [10, 100, 10, 20, 30, 10]
print(f"l2.count(10): {l2.count(10)}")
import random
r = random.choices(range(1, 100), k=10)
print(r)
"""### 리스트의 순서를 뒤집기"""

# reverse()는 리스트에서 요소의 순서를 반대로 뒤집습니다.
print(f"l : {l}")
print(f"l[::-1] : {l[::-1]}")
print(list(reversed(l)))



"""### 리스트의 요소를 정렬하기

sort()는 리스트의 요소을 작은 순서대로 정렬합니다(오름차순).

* `sort()` 또는 `sort(reverse=False)`: 리스트의 값을 작은 순서대로 정렬(오름차순)
* `sort(reverse=True)`: 리스트의 값을 큰 순서대로 정렬(내림차순)
"""
print(f"sorted(r) : {sorted(r)}")
print(r.sort())
print(f"r : {r}")

"""### sort 메서드와 sorted 함수
파이썬은 리스트의 sort 메서드뿐만 아니라 내장 함수 sorted도 제공합니다. sort와 sorted 모두 정렬을 해주는 함수지만, 약간의 차이점이 있습니다. sort는 메서드를 사용한 리스트를 변경하지만, sorted 함수는 정렬된 새 리스트를 생성합니다.
"""





"""### 리스트의 모든 요소를 삭제하기"""

# clear()는 리스트의 모든 요소를 삭제합니다.
print(f"l: {l}")
l.clear()
print(f"l: {l}")
# clear 대신 del a[:]와 같이 시작, 끝 인덱스를 생략하여 리스트의 모든 요소를 삭제할 수도 있습니다.

"""### 리스트를 슬라이스로 조작하기"""

# 리스트는 메서드를 사용하지 않고, 슬라이스로 조작할 수도 있습니다. 다음은 리스트 끝에 값이 한 개 들어있는 리스트를 추가합니다.

"""a[len(a):]는 시작 인덱스를 len(a)로 지정해서 리스트의 마지막 인덱스보다 1이 더 큰 상태입니다. 즉, 그림과 같이 리스트 끝에서부터 시작하겠다는 뜻입니다(이때는 리스트의 범위를 벗어난 인덱스를 사용할 수 있습니다).

그리고 a[len(a):] = [..., ...]과 같이 요소가 여러 개 들어있는 리스트를 할당하면 리스트 a 끝에 다른 리스트를 연결한다는 뜻입니다.
"""



"""### 리스트가 비어 있는지 확인하기

리스트(시퀀스 객체)가 비어 있는지 확인하려면 어떻게 해야 할까요? 방법은 간단합니다. 리스트는 len 함수로 길이를 구할 수 있죠? 이걸 if 조건문으로 판단하면 리스트가 비어 있는지 확인할 수 있습니다.

```
if not len(seq):    # 리스트가 비어 있으면 True
if len(seq):        # 리스트에 요소가 있으면 True
```

하지만 파이썬에서는 이 방법보다 리스트(시퀀스 객체)를 바로 if 조건문으로 판단하는 방법을 권장합니다(PEP 8).
```
if not seq:    # 리스트가 비어 있으면 True
if seq:        # 리스트에 내용이 있으면 True
```

특히 리스트가 비어 있는지 확인하는 방법은 리스트의 마지막 요소에 접근할 때 유용하게 사용할 수 있습니다. 리스트의 마지막 요소에 접근할 때는 인덱스를 -1로 지정하면 되죠?
"""



# 만약 리스트가 비어 있을 경우에는 인덱스를 -1로 지정하면 에러가 발생합니다.

# 이때는 if 조건문을 활용하여 리스트에 요소가 있을 때만 마지막 요소를 가져오면 됩니다.

"""## 리스트의 할당과 복사

이번에는 리스트의 할당과 복사에 대해 알아보겠습니다. 할당과 복사는 비슷한 것 같지만 큰 차이점이 있습니다.
"""



"""b = a와 같이 리스트를 다른 변수에 할당하면 리스트는 두 개가 될 것 같지만 실제로는 리스트가 한 개입니다."""

# a와 b를 is 연산자로 비교해보면 True가 나옵니다. 즉, 변수 이름만 다를 뿐 리스트 a와 b는 같은 객체입니다.

# a와 b는 같으므로 b[2] = 99와 같이 리스트 b의 요소를 변경하면 리스트 a와 b에 모두 반영됩니다.

# 리스트 a와 b를 완전히 두 개로 만들려면 copy 메서드로 모든 요소를 복사해야 합니다.

"""b = a.copy()와 같이 copy를 사용한 뒤 b에 할당해주면 리스트 a의 요소가 모두 b에 복사됩니다."""

# a와 b를 is 연산자로 비교해보면 False가 나옵니다. 즉, 두 리스트는 다른 객체입니다. 그러나 복사된 요소는 모두 같으므로 ==로 비교하면 True가 나옵니다.

# 이제 리스트 a와 b는 별개이므로 한쪽의 값을 변경해도 다른 리스트에 영향을 미치지 않습니다.
# 다음과 같이 리스트 b의 요소를 변경하면 리스트 a는 그대로이고 리스트 b만 바뀝니다.

"""## 반복문으로 리스트의 요소를 모두 출력하기

### for 반복문으로 요소 출력하기

for 반복문은 그냥 in 뒤에 리스트를 지정하면 됩니다.

```
for 변수 in 리스트:
     반복할 코드
```
"""



"""`for i in a:`는 리스트 a에서 요소를 꺼내서 i에 저장하고, 꺼낼 때마다 코드를 반복합니다. 따라서 print로 i를 출력하면 모든 요소를 순서대로 출력할 수 있습니다.


"""

# 물론 in 다음에 리스트를 직접 지정해도 상관 없습니다.

"""### 인덱스와 요소를 함께 출력하기

그럼 for 반복문으로 요소를 출력할 때 인덱스도 함께 출력하려면 어떻게 해야 할까요? 이때는 `enumerate`를 사용합니다.

* `for 인덱스, 요소 in enumerate(리스트)`:
"""



"""`for index, value in enumerate(a):`와 같이 enumerate에 리스트를 넣으면 for 반복문에서 인덱스와 요소를 동시에 꺼내 올 수 있습니다."""

# 인덱스 1부터 출력하기

"""enumerate에 start를 지정해주면 시작 인덱스를 바꿀 수 있습니다.

* `for 인덱스, 요소 in enumerate(리스트, start=숫자):`
"""

# for index, value in enumerate(a, start=1):

"""### while반복문으로 요소 출력하기"""



"""즉, 리스트의 인덱스는 0부터 시작하고 마지막 인덱스는 리스트의 길이보다 1이 작으므로 <를 사용합니다. 만약 i <= len(a)처럼 <=을 사용하면 리스트의 범위를 벗어나게 되므로 주의해야 합니다."""



"""## 리스트(튜플)의 가장 작은 수, 가장 큰 수, 합계 구하기

### 가장 작은 수와 가장 큰 수 구하기

먼저 가장 작은 수와 가장 큰 수는 어떻게 구할까요? 앞에서 반복문을 배웠으니 요소를 모두 반복하면서 숫자를 찾아내 보겠습니다.
"""



"""먼저 리스트 a의 첫 번째 요소 a[0]를 변수 smallest에 저장합니다. 그리고 for로 리스트의 요소를 모두 반복하면서 i가 smallest보다 작으면 smallest에 i를 할당합니다. 즉, 숫자를 계속 비교해서 숫자가 작으면 smallest를 바꾸는 방식입니다."""

# 가장 큰 수는 부등호를 반대로 만들면 되겠죠?

"""리스트의 숫자를 계속 비교해서 숫자가 크면 largest를 바꾸는 방식입니다. 그런데 이렇게 for와 if를 사용해서 가장 작은 수와 가장 큰 수를 찾으려니 좀 번거롭습니다. 다른 방법이 없을까요?

앞에서 리스트를 정렬하는 sort 메서드를 배웠습니다. 리스트를 작은 순서대로 정렬(오름차순)하면 첫 번째 요소가 가장 작은 수입니다. 반대로 큰 순서대로 정렬(내림차순)하면 첫 번째 요소가 가장 큰 수가 되겠죠?
"""


print(f"r : {r}")
print(f"r min(r) : {min(r)}")
print(f"r max(r) : {max(r)}")
print(f"r sum(r) : {sum(r)}")
print(f"r len(r) : {len(r)}")


# 더 간단한 방법이 있습니다. 파이썬에서 제공하는 min, max 함수를 사용하면 됩니다.

"""min은 리스트에서 가장 작은 값을 구하고, max는 가장 큰 값을 구합니다.

### 요소의 합계 구하기
"""

# 이번에는 리스트에서 요소의 합계를 구해보겠습니다. 합계를 구할 때도 반복문을 사용할 수 있겠죠?

"""변수 x에 0을 할당하고, for 반복문으로 리스트의 요소를 모두 반복하면서 요소를 x에 계속 더해주면 됩니다. 이때 x에는 반드시 0을 할당해야 합니다. 그렇지 않으면 없는 변수에 값을 더하게 되므로 에러가 발생합니다. 또한, 0부터 시작해서 숫자를 더해야 제대로 된 합계가 구해지겠죠?

사실 이 방법도 좀 번거롭습니다. 그래서 파이썬에서는 합계를 구하는 sum 함수를 제공합니다.
"""



"""## 리스트 표현식 사용하기

파이썬의 리스트가 특이한 점은 리스트 안에 for 반복문과 if 조건문을 사용할 수 있다는 점입니다. 이렇게 리스트 안에 식, for 반복문, if 조건문 등을 지정하여 리스트를 생성하는 것을 **리스트 컴프리헨션(list comprehension)**이라고 합니다.

리스트 컴프리헨션이라고 하니 언뜻 이해가 잘 안되죠? 책이나 인터넷에서도 리스트 내포, 리스트 내장, 리스트 축약, 리스트 해석 등으로 씁니다. 컴프리헨션은 능력, 이해력, 시험 등의 뜻도 있지만, 어떤 것을 잡아서 담아둔다는 뜻이 있습니다. 즉, 식으로 지정해서 생성된 것을 리스트로 잡아두는 것이 리스트 컴프리헨션입니다. 개념적으로 보면 "리스트 표현식"이라고 할 수 있으니 이 책에서는 간단하게 리스트 표현식이라고 쓰겠습니다.

리스트 표현식은 다음과 같이 리스트 안에 식, for 반복문을 지정합니다. 문법이 다소 복잡해 보이지만 여러 줄의 코드를 한 줄로 줄일 수 있고, 익숙해지면 크게 어렵지 않습니다.

* `[식 for 변수 in 리스트]`
"""


x = [i * 2 for i in range(10)]
print(x)
x = [i ** 2 for i in range(10)]
print(x)


"""리스트 안에 식, for, 변수, in, 리스트 순서로 들어있지만 뒤에서 앞으로 읽으면 간단합니다. 즉, range(10)으로 0부터 9까지 생성하여 변수 i에 숫자를 꺼내고, 최종적으로 i를 이용하여 리스트를 만든다는 뜻입니다."""





"""### 리스트 표현식에서 if 조건문 사용하기

이번에는 리스트 표현식에서 if 조건문을 사용해보겠습니다. 다음과 같이 if 조건문은 for 반복문 뒤에 지정합니다.

* `[식 for 변수 in 리스트 if 조건식]`
"""





"""### for 반복문과 if 조건문을 여러 번 사용하기

리스트 표현식은 for와 if를 여러 번 사용할 수도 있습니다.

* `[식 for 변수1 in 리스트1 if 조건식1     for 변수2 in 리스트2 if 조건식2     ...     for 변수n in 리스트n if 조건식n]`
"""

x = [i * 2 for i in range(10) if i % 2 == 0]
print(x)
x2 = [i ** 2 for i in range(10) if i % 2]
print(x2)



"""## 리스트에 map 사용하기

이번에는 리스트에 map을 사용해보겠습니다. map은 리스트의 요소를 지정된 함수로 처리해주는 함수입니다(map은 원본 리스트를 변경하지 않고 새 리스트를 생성합니다).

* `list(map(함수, 리스트))`
* `tuple(map(함수, 튜플))`

예를 들어 실수가 저장된 리스트가 있을 때 이 리스트의 모든 요소를 정수로 변환하려면 어떻게 해야 할까요? 먼저 for 반복문을 사용해서 변환해보겠습니다.
"""



# 매번 for 반복문으로 반복하면서 요소를 변환하려니 조금 번거롭습니다. 이때는 map을 사용하면 편리합니다.

"""### input().split()과 map

지금까지 input().split()으로 값을 여러 개 입력받고 정수, 실수로 변환할 때도 map을 사용했었죠? 사실 input().split()의 결과가 문자열 리스트라서 map을 사용할 수 있었습니다.

다음과 같이 input().split()을 사용한 뒤에 변수 한 개에 저장해보면 리스트인지 확인할 수 있습니다.
"""



# 이제 map을 사용해서 정수로 변환해봅니다.

"""사실 map이 반환하는 맵 객체는 변수 여러 개에 저장하는 언패킹(unpacking)이 가능합니다. 그래서 a, b = map(int, input().split())처럼 list를 생략한 것입니다"""

"""
# 문자열 응용

지금까지 리스트 사용 방법을 알아보았습니다. 리스트는 요소 여러 개가 연속적으로 이어져 있죠? 마찬가지로 문자열도 문자 여러 개가 연속적으로 이어져 있는 시퀀스 자료형이라 리스트와 비슷한 점이 많습니다.

## 문자열 조작하기

### 문자열 바꾸기

replace('바꿀문자열', '새문자열')은 문자열 안의 문자열을 다른 문자열로 바꿉니다(문자열 자체는 변경하지 않으며 바뀐 결과를 반환합니다). 다음은 문자열 'Hello, world!'에서 'world'를 'Python'으로 바꾼 뒤 결과를 반환합니다.
"""

s = "아메리카노 2샷추가(ice)"
s.replace("2", "3")  # 메소드를 사용하면 -> 새로운 사본. 복사본.
print(f"s : {s}")
print(f"s.replace(\"2\", \"3\") : {s.replace('2', '3')}")
s2 = s.replace("2", "3")
print(f"s2 : {s2}")

"""만약 바뀐 결과를 유지하고 싶다면 문자열이 저장된 변수에 replace를 사용한 뒤 다시 변수에 할당해주면 됩니다."""



"""### 문자열 분리하기

이제 문자열을 분리하는 방법입니다.

split()은 공백을 기준으로 문자열을 분리하여 리스트로 만듭니다. 지금까지 input으로 문자열을 입력받은 뒤 리스트로 만든 메서드가 바로 이 split입니다.
"""

s = "5시 53분의 하늘에서 발견한 너와 나"
s2 = "9와 4분의 3 승강장에서 너를 기다려 (Run Away)"
print(s.split())
print(s2.split("승강장에서"))

"""split('기준문자열')과 같이 기준 문자열을 지정하면 기준 문자열로 문자열을 분리합니다. 즉, 문자열에서 각 단어가 ,(콤마)와 공백으로 구분되어 있을 때 ', '으로 문자열을 분리하면 단어만 리스트로 만듭니다."""



"""### 구분자 문자열과 문자열 리스트 연결하기

문자열을 분리하여 리스트로 만들었으니 다시 연결하는 방법도 있겠죠?

join(리스트)는 구분자 문자열과 문자열 리스트의 요소를 연결하여 문자열로 만듭니다. 다음은 공백 ' '에 join을 사용하여 각 문자열 사이에 공백이 들어가도록 만듭니다..
"""

r = [str(i) for i in range(10)]
print(r)
print(f'"".join(r): {"".join(r)}')
print(f'",".join(r): {",".join(r)}')

# 마이너스 '-'에 join을 사용하면 각 문자열 사이에 마이너스가 들어가겠죠?

"""### 소문자를 대문자로 바꾸기

이번에는 문자열의 문자를 대소문자로 바꾸는 방법입니다.

upper()는 문자열의 문자를 모두 대문자로 바꿉니다. 만약 문자열 안에 대문자가 있다면 그대로 유지됩니다.
"""



"""### 대문자를 소문자로 바꾸기

lower()는 문자열의 문자를 모두 소문자로 바꿉니다. 만약 문자열 안에 소문자가 있다면 그대로 유지됩니다.
"""



"""### 양쪽 공백 삭제하기

strip()은 문자열에서 양쪽에 있는 연속된 모든 공백을 삭제합니다.
"""



"""### 메서드 체이닝

이렇게 문자열 메서드는 처리한 결과를 반환하도록 만들어져 있습니다. 따라서 메서드를 계속 연결해서 호출하는 메서드 체이닝이 가능합니다. 메서드 체이닝은 메서드를 줄줄이 연결한다고 해서 메서드 체이닝(method chaining)이라 부릅니다.

### 문자열 왼쪽에 0 채우기

지금까지 문자열을 정렬하면서 남는 공간에 공백을 채웠죠? 파이썬을 사용하다 보면 문자열 왼쪽에 0을 채워야 할 경우가 생깁니다.

zfill(길이)는 지정된 길이에 맞춰서 문자열의 왼쪽에 0을 채웁니다( zero fill을 의미). 단, 문자열의 길이보다 지정된 길이가 작다면 아무것도 채우지 않습니다. 보통 zfill은 숫자를 일정 자릿수로 맞추고 앞자리는 0으로 채울 때 사용합니다.
"""







"""### 문자열 위치 찾기

이번에는 문자열의 위치를 찾는 방법을 알아보겠습니다.

find('찾을문자열')은 문자열에서 특정 문자열을 찾아서 인덱스를 반환하고, 문자열이 없으면 -1을 반환합니다. find는 왼쪽에서부터 문자열을 찾는데, 같은 문자열이 여러 개일 경우 처음 찾은 문자열의 인덱스를 반환합니다. 여기서는 'pl'이 2개 있지만 왼쪽에서 처음 찾은 'pl'의 인덱스 2를 반환합니다.
"""

print(f"s2 : {s2}")
print(f"s2.find('너') : {s2.find('너')}")



"""### 문자열 개수 세기

count('문자열')은 현재 문자열에서 특정 문자열이 몇 번 나오는지 알아냅니다.
"""

s3 = "짜리짜리짜리짜리몽땅"
print("짜리짜리짜리짜리몽땅")
print("짜리짜리짜리짜리몽땅".count("짜리"))

"""
# 문자열 서식

파이썬에서 문자열 포맷팅을 할 때는 f-string, format 메소드, 서식 지정자를 사용할 수 있습니다.

## f-string

f-string은 파이썬 3.6 이후부터 사용 가능한 문자열 포맷팅 방법 중 하나입니다. f-string을 사용하면 문자열 안에서 변수의 값을 간단하게 삽입할 수 있으며, 이를 통해 가독성과 코드 작성의 편의성이 크게 향상됩니다.
"""
# f"텍스트... {변수명, 리터럴}" : 포맷팅된 문자열 표현

# f{...:.[표시하고싶은자리수]f} : float를 나타냄.



"""
# 딕셔너리 응용

## 딕셔너리 조작하기

### 딕셔너리에서 키의 값 저장하기

update(키=값)은 이름 그대로 딕셔너리에서 키의 값을 수정합니다. 예를 들어 딕셔너리가 x = {'a': 10}이라면 x.update(a=90)과 같이 키에서 작은따옴표 또는 큰따옴표를 빼고 키 이름과 값을 지정합니다.
"""

d = {"name": "투바투"}
d['name'] = "TXT"
print(f"d : {d}")
d.update(name = "HIVE")
print(f"d : {d}")

"""만약 딕셔너리에 키가 없으면 키-값 쌍을 추가합니다. 딕셔너리 x에는 키 'e'가 없으므로 x.update(e=50)을 실행하면 'e': 50을 추가합니다."""



"""update는 키-값 쌍 여러 개를 콤마로 구분해서 넣어주면 값을 한꺼번에 수정할 수 있습니다. 이때도 키가 있으면 해당 키의 값을 수정하고 없으면 키-값 쌍을 추가합니다.

"""



"""update(키=값)은 키가 문자열일 때만 사용할 수 있습니다. 만약 키가 숫자일 경우에는 update(딕셔너리)처럼 딕셔너리를 넣어서 값을 수정할 수 있습니다."""



"""다른 방법으로는 리스트와 튜플을 이용하는 방법도 있습니다. update(리스트), update(튜플)은 리스트와 튜플로 값을 수정합니다. 여기서 리스트는 [[키1, 값1], [키2, 값2]] 형식으로 키와 값을 리스트로 만들고 이 리스트를 다시 리스트 안에 넣어서 키-값 쌍을 나열해줍니다(튜플도 같은 형식)."""



"""### 딕셔너리에서 키-값 쌍 삭제하기

pop(키)는 딕셔너리에서 특정 키-값 쌍을 삭제한 뒤 삭제한 값을 반환합니다.
"""

n = d.pop("name")
print(f"d : {d}")


"""pop(키, 기본값)처럼 기본값을 지정하면 딕셔너리에 키가 있을 때는 해당 키-값 쌍을 삭제한 뒤 삭제한 값을 반환하지만 키가 없을 때는 기본값만 반환합니다."""



"""pop 대신 del로 특정 키-값 쌍을 삭제할 수도 있습니다. 이때는 [ ]에 키를 지정하여 del을 사용합니다."""



"""### 딕셔너리의 모든 키-값 쌍을 삭제하기"""

# clear()는 딕셔너리의 모든 키-값 쌍을 삭제합니다.

"""### 딕셔너리에서 키의 값을 가져오기"""

# get(키)는 딕셔너리에서 특정 키의 값을 가져옵니다.

"""get(키, 기본값)처럼 기본값을 지정하면 딕셔너리에 키가 있을 때는 해당 키의 값을 반환하지만 키가 없을 때는 기본값을 반환합니다."""

print(d.get("name"))
print(d.get("name","UNTITLED"))

"""### 딕셔너리에서 키-값 쌍을 모두 가져오기

딕셔너리는 키와 값을 가져오는 다양한 메서드를 제공합니다.

* items: 키-값 쌍을 모두 가져옴
* keys: 키를 모두 가져옴
* values: 값을 모두 가져옴
"""

# items()는 딕셔너리의 키-값 쌍을 모두 가져옵니다.

# keys()는 키를 모두 가져옵니다.
print(f"d.keys() : {d.keys()}")
# values()는 값을 모두 가져옵니다.
print(f"d.valuses() : {d.values()}")
"""## 반복문으로 딕셔너리의 키-값 쌍을 모두 출력하기"""



"""for i in x:처럼 for 반복문에 딕셔너리를 지정한 뒤에 print로 변수 i를 출력해보면 값은 출력되지 않고 키만 출력됩니다. 그럼 키와 값을 모두 출력하려면 어떻게 해야 할까요?

이때는 for in 뒤에 딕셔너리를 지정하고 items를 사용해야 합니다.

```
for 키, 값 in 딕셔너리.items():
     반복할 코드
```
"""
d = {"name": "투바투"}
for key, value in d.items():
    print(f"key : {key}, value : {value}")


"""`for key, value in x.items():`는 딕셔너리 x에서 키-값 쌍을 꺼내서 키는 key에 값은 value에 저장하고, 꺼낼 때마다 코드를 반복합니다. 따라서 print로 key와 value를 출력하면 키-값 쌍을 모두 출력할 수 있습니다.

### 딕셔너리의 키만 출력하기
"""





"""### 딕셔너리의 값만 출력하기"""



"""## 딕셔너리 안에서 딕셔너리 사용하기

딕셔너리는 값 부분에 다시 딕셔너리가 계속 들어갈 수 있습니다.

* `딕셔너리 = {키1: {키A: 값A}, 키2: {키B: 값B}}`
"""



"""중첩 딕셔너리는 계층형 데이터를 저장할 때 유용합니다.

딕셔너리 안에 들어있는 딕셔너리에 접근하려면 딕셔너리 뒤에 [ ](대괄호)를 단계만큼 붙이고 키를 지정해주면 됩니다.

* `딕셔너리[키][키]`
* `딕셔너리[키][키] = 값`
"""