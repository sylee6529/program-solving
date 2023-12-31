# [Silver II] 골드바흐의 추측 - 9020 

[문제 링크](https://www.acmicpc.net/problem/9020) 

### 의사코드

```
n 입력받음
// n번 입력받는다
for 1 ~ n-1:
  num 입력받음
  for j/2 ~ 2:     // 1은 제외
    if (j는 소수) and (num-j는 소수):	// 차이가 적은 숫자 출력을 위해 거꾸로
       print(j, num-j)
       break           // 숫자를 찾으면 출력하고 더 돌지 않는다


def is_prime_number(a):
    for 2 ~ math.sqrt(a)+1    // 제곱근 포함 주의
      if a % i == 0:   // 숫자와 i 가 나눠지면, false 반환
        return False
    return True
```


### 성능 요약

메모리: 33240 KB, 시간: 160 ms

### 분류

수학, 정수론, 소수 판정, 에라토스테네스의 체

### 제출 일자

2023년 10월 14일 13:21:17

### 문제 설명

<p>1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다. 예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다. 하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.</p>

<p>골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다. 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다. 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.</p>

<p>2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.</p>

### 입력 

 <p>첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고 짝수 n이 주어진다.</p>

### 출력 

 <p>각 테스트 케이스에 대해서 주어진 n의 골드바흐 파티션을 출력한다. 출력하는 소수는 작은 것부터 먼저 출력하며, 공백으로 구분한다.</p>

