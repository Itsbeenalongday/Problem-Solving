# Problem-Solving

코딩테스트 준비 과정 기록 노트

## PS의 기초

**1. 알고리즘을 생각하세요.**

때로는 문제의 세부 사항을 검토하고 해결책이 당신에게 나올 것을 기대하는 것이 유용합니다 (상향식 접근법). 
그러나 다른 알고리즘에 대해서도 생각해 볼 수 있으며 각각의 알고리즘이 당신 앞의 문제에 적용되는지를 질문 할 수 있습니다 (하향식 접근법). 
이러한 방식으로 참조 프레임을 변경하면 종종 즉각적인 통찰력을 얻을 수 있습니다. 

다음은 면접에서 요구하는 문제의 절반 이상을 해결하는 데 도움이되는 알고리즘 기법입니다.
Sorting (plus searching / binary search)
Divide and Conquer
Dynamic Programming / Memoization
Greediness
Recursion
Algorithms associated with a specific data structure (which brings us to our fourth suggestion...)

**2. 데이터 구조를 생각하십시오.**

상위 10 개 데이터 구조가 실제 세계에서 사용되는 모든 데이터 구조의 99 %를 차지한다는 것을 알고 계셨습니까? 
때로는 최적의 솔루션이 블룸 필터 또는 접미어 트리를 필요로하는 문제를 묻습니다. 
하지만 이러한 문제조차도 훨씬 더 일상적인 데이터 구조를 사용하는 최적의 솔루션을 사용하는 경향이 있습니다. 

가장 자주 표시 될 데이터 구조는 다음과 같습니다.
+ Array
+ Stack / Queue
+ HashSet / HashMap / HashTable / Dictionary
+ Tree / Binary tree
+ Heap
+ Graph

**3. 이전에 보았던 관련 문제와 해결 방법에 대해 생각해보십시오.**

여러분에게 제시한 문제는 이전에 보았던 문제이거나 적어도 조금은 유사합니다. 
이러한 솔루션에 대해 생각해보고 문제의 세부 사항에 어떻게 적응할 수 있는지 생각하십시오. 문제가 제기되는 형태로 넘어지지는 마십시오. 
핵심 과제로 넘어 가서 과거에 해결 한 것과 일치하는지 확인하십시오.

**4. 문제를 작은 문제로 분해하여 수정하십시오.**

+ 특별한 경우 또는 문제의 단순화 된 버전을 해결하십시오. 
+ 코너 케이스를 보는 것은 문제의 복잡성과 범위를 제한하는 좋은 방법입니다.
> 코너 케이스

>> 코너 케이스는 여러 가지 변수와 환경의 복합적인 상호작용으로 발생하는 문제다.

예를 들어 fixnum이라는 변수의 값으로 128이 입력되었을 때, 
A 기계에서 테스트했을 때는 정상작동하지만 B 기계에서는 오류가 발생한다면 코너 케이스라고 할 수 있다. 
같은 장치에서라도 시간이나 다른 환경에 따라 오류가 발생하기도 하고 정상작동 하기도 한다면 이것도 코너 케이스다.

특히 멀티코어 프로그래밍에서 만나기 쉬운 오류일 것이다.
문제를 큰 문제의 하위 집합으로 축소하면 작은 부분부터 시작하여 전체 범위까지 작업을 진행할 수 있습니다. 
작은 문제의 구성으로 문제를 보는 것도 도움이 될 수 있습니다.

**5. 되돌아 오는 것을 두려워하지 마십시오.**

특정 접근법이 효과적이지 않다고 느끼면 다른 접근 방식을 시도 할 때가 있습니다. 
물론 너무 쉽게 포기해서는 안됩니다. 그러나 열매를 맺지 않고도 유망한 생각이 들지 않는 접근법에 몇 분을 소비했다면, 백업하고 다른 것을 시도해보십시오. 
저는 덜 접근한 지원자보다 한참 더 많이 나아간 지원자를 많이 보았습니다. 
즉, (모두 평등 한) 다른 사람들이 좀 더 기민한 접근 방식을 포기해야 한다는 것을 의미합니다.


## 문제 해결을 위한 전략적 접근

+ 코딩 테스트의 목적
+ 문제 해결 여부
+ 예외 상황과 경계값 처리
+ 코드 가독성과 중복 제거 여부 등 코드 품질
+ 언어 이해도
+ 효율성

궁극적으로는 문제 해결 능력을 측정하기 위함이며 이는 '어떻게 이 문제를 창의적으로 해결할 것인가'를 측정하기 위함이라고 볼 수 있다.

**접근하기**
문제를 공격적으로 받아들이고 필요한 정보를 추가적으로 요구하여, 해당 문제에 대해 완벽하게 이해하는게 우선이다.
해당 문제를 익숙한 용어로 재정의하거나 문제를 해결하기 위한 정보를 추출한다. 이 과정을 추상화라고 한다.
추상화된 데이터를 기반으로 이 문제를 어떻게 해결할 지 계획을 세운다. 이 때 사용할 알고리즘과 자료구조를 고민한다.
세운 계획에 대해 검증을 해본다. 수도 코드 작성도 해당될 수 있고 문제 출제자에게 의견을 물어볼 수도 있다.
세운 계획으로 문제를 해결해본다. 해결이 안 된다면 앞선 과정을 되짚어본다.

**생각할 때**
비슷한 문제를 생각해본다.
단순한 방법으로 시작하여 점진적으로 개선해나간다.
작은 값을 생각해본다.
그림으로 그려본다.
수식으로 표현해본다.
순서를 강제해본다.
뒤에서부터 생각해본다.

## 문제 풀면서 나온 아이디어, 반성할 점

1. 배열의 최대 최소값을 필요로 하는 문제는 입력받을 때 처리해 버리자

2. 자료구조, 수열을 다루는 문제에서 공통되는 부분이 있다면 그 부분을 묶어서 최대한 반복회수를 줄이자

3. 연산관련 문제에서 1로 만든다거나 등등 줄여나가는 문제에서 배수, 약수를 생각해보자

## Reference

<div align="center">

[![ReadMe Card](https://github-readme-stats.vercel.app/api/pin/?username=matthewsamuel95&repo=ACM-ICPC-Algorithms&theme=radical)](https://github.com/matthewsamuel95/ACM-ICPC-Algorithms.git)
[![ReadMe Card](https://github-readme-stats.vercel.app/api/pin/?username=ndb796&repo=python-for-coding-test&theme=radical)](https://github.com/ndb796/python-for-coding-test.git)
[![ReadMe Card](https://github-readme-stats.vercel.app/api/pin/?username=TheAlgorithms&repo=Python&theme=radical)](https://github.com/TheAlgorithms/Python.git)
[![ReadMe Card](https://github-readme-stats.vercel.app/api/pin/?username=TheAlgorithms&repo=Java&theme=radical)](https://github.com/TheAlgorithms/Java.git)
[![ReadMe Card](https://github-readme-stats.vercel.app/api/pin/?username=TheAlgorithms&repo=C-Plus-Plus&theme=radical)](https://github.com/TheAlgorithms/C-Plus-Plus.git)

</div>