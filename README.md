# baekjoon-algorithm-study

# 📌 스터디 규칙

- 스터디는 온라인으로 1시간 진행한다. 단, 카메라를 켜고 진행한다.
- 10분 아이스 브레이킹 및 각 스터디원별 담당 문제에 대한 풀이법 공유
- 각 스터디원은 풀이법 공유시 이번 주에 정리 및 알게된 알고리즘이 있다면 추가적인 설명
- 매주 달라지는 PR 파트너의 코드에 대해 코드 리뷰

# 📁 3기 Repository 폴더 구조

> week17/BOJ_20300/섬의 개수_홍지훈.py

기존 1~2기와 폴더 구조 및 파일명 규칙이 동일합니다. 단, 매번 폴더 및 파일을 생성하는 과정이 귀찮았던 부분을 자동화하는 파일을 생성했습니다.

해당 자동화 파일은 scripts/create.sh 파일을 말하며 하단에 사용법을 정리해두었습니다.

# 😀 3기 브랜치 생성

## 파일 및 폴더 생성 - create.sh

alias 를 설정해두어서 아래와 같은 명령어를 입력시, 이번주차에 본인에게 해당하는 모든 폴더 및 파일을 생성해줍니다.

```
create {본인이름} {확장자} // 만약 파이썬을 사용한다면 확장자를 붙이지 않아도 상관없고 그 외의 언어를 사용시 js / cpp 등을 붙여주세요.
ex) create 홍지훈
create 홍지훈 cpp
create 홍지훈 js
```

만약 alias 가 먹히지 않았다면 프로젝트 루트 디렉토리에서 ./scripts/create.sh {본인이름} {확장자} 를 해주시면 됩니다.
혹은 루트 디렉토리에서 source bash.bashrc 를 터미널에 입력하신 뒤엔 alias 가 동작합니다. 

```
ex) ./scripts/create.sh 홍지훈
```

위의 명령어 실행시 결과 👉

`확장자명 입력하지 않을 경우`

![Feb-12-2024 21-31-37](https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/b6cd5189-6b74-4559-8ca8-fa1981394e74)

`확장자명 입력할 경우`

![확장자](https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/e65487d9-67a5-4a5b-9651-bfc64a9e6d69)

> 단, alias 는 루트 디렉토리에서만 동작합니다.

## 브랜치

`기존 브랜치명`

```
BOJ_2546_홍지훈
```

`신규 브랜치명`

```
문제이름_홍지훈
```

> 브랜치명을 조금이라도 짧게 줄이고자 문제이름_본인이름 형식으로 바꿀 것을 건의합니다.

# 🤝 3기 PR 규칙

## PR 커밋메세지 단축

PR 메세지가 좀 길고 반복적으로 나오는 부분이 있어 짧게 줄이는 것을 건의합니다.

`기존방식`

```
[BOJ] 17836_공주님을 구해라! / 골드5 / 115분 / X
```

`신규방식`

```
공주님을 구해라! / 골드5 / 115분 / X
```

플랫폼, 문제번호 등은 폴더명 및 파일명에 드러나는 부분이니 이를 생략하고 `문제이름` / `문제난이도` / `걸린시간` / `소요시간` 만 커밋메세지에 반영해보는 것을 건의합니다.

+) 추가로 풀지 못했던 기존의 코드도 지우지 말고 같이 PR 로 올려주시면 좋을 것 같습니다. 

## PR 템플릿 변경

`기존 템플릿`

```md
### 📖 풀이한 문제

- 백준 {문제번호}-{문제이름}

### ⭐️ 문제에서 주로 사용한 알고리즘

### 대략적인 코드 설명
```

`신규 템플릿`

```md
### ⭐️ 문제에서 주로 사용한 알고리즘

### 대략적인 코드 설명

### 코드리뷰시 요청사항
```

> 문제 번호 및 문제이름은 PR TITLE 에 나타나 있으니 생략합니다.
> 코드리뷰 대상자가 랜덤으로 생성되니 해당 리뷰어에게 리뷰를 요청했으면 좋을 것 같은 사항을 PR 에 기입합니다. 이때 코드도 같이 적으면 코드리뷰시 더 용이할 것 같습니다.

# 3기에서의 변경점 정리

1. 폴더 구조 동일. 단, 자동화 script 추가로 create {본인이름} {확장자} 형식의 명령어를 통해 이번주차에 생성해야 하는 모든 폴더 및 파일 생성가능
2. 커밋 메세지 간소화. -> 커밋 메세지엔 `문제난이도` / `걸린시간` / `소요시간` 만 입력
3. PR 템플릿 변경

---

# 기존 1~2 기 규칙들

<details>

<summary>기존 규칙들</summary>

# 🙆‍♂️ 참여 방법

1. 이 저장소를 `clone` 한다.
2. 생성된 저장소에 해당 주차에 맞게 `BOJ_문제번호` 로 폴더를 생성한다.
3. 생성된 폴더에 자신의 소스코드를 업로드한다. ex) `문제이름_자신이름.py / java ...`
4. commit 규칙을 지켜서 커밋한다.
5. 원본 저장소로 `Pull Request` 를 한다.
6. 다른 사람들의 PR 을 보고 자유롭게 코드리뷰를 한다. 되도록이면 다른 멤버들의 코드를 보고 하나 이상씩 피드백을 남겼으면 좋겠습니다만 의견 부탁드립니다 :)

### 참여 방법 안내 - clone

<details>

<summary>클론 방법</summary>

<img width="821" alt="스크린샷 2023-12-09 오후 9 40 55" src="https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/4aa89adf-137b-4838-bb39-36e5e07954bf">

- 해당 주소를 복사후

![스크린샷 2023-12-09 오후 9 42 15](https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/d8f87f6f-1a81-431a-83f5-14fdb28d771c)

- 원하는 로컬 디렉토리에 클론

</details>

### 참여 방법 안내 - 폴더 생성 및 소스코드 업로드

<details>

<summary>폴더 생성</summary>

![스크린샷 2023-12-09 오후 9 44 19](https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/d5fa2500-1363-4bfa-9d2d-f71c3d1868af)

- 주차별 문제로 폴더를 생성하여 해당 폴더 내에 풀이 코드를 업로드한다.
  - ex) `week9/BOJ_18352/특정 거리의 도시 찾기.py`

</details>

# 📁 Repository 폴더 구조

```
week@/플랫폼_문제번호/문제이름_자신이름.ts/ java ...
```

- 예시 : `week1/BOJ_2548/대표자연수_홍지훈.py`

## 플랫폼

| 플랫폼                 | 태그 |
| ---------------------- | ---- |
| 백준                   | BOJ  |
| 프로그래머스           | PSG  |

# ✏️ commit 규칙

- commit 메세지 : [플랫폼] 문제번호_문제이름 / 난이도 / 걸린시간 / 문제풀이성공여부
- merge 가 아니더라도 push 후 PR을 해주셔야 다른 분들이 코드리뷰를 할 수 있습니다!

```
git commit -m "[BOJ] 2548_대표자연수 / 실버3 / 10분 / O "
git commit -m "[PSG] 양궁 대회 / Lv. 2 / 110분 / X "
```

- 코드를 커밋하는 경우가 아닐때 ( readme 수정, 이름 변경, 코드 수정, 주석 추가 및 오타 수정 등 )는 자유롭게 커밋해주세요.

# 🤝 PR 규칙

![스크린샷 2023-12-09 오후 9 49 16](https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/a03a9e3c-6e33-49fd-b7af-f83378f0abdf)

위와 같은 PR 템플릿을 등록해두었습니다. 각 문제별로 풀이를 하셨다면 PR 을 요청해주세요.
만약 해당 문제가 자신이 풀이법을 공유해야 하는 문제라면 PR 을 좀 더 자세히 작성해주세요. 이 PR 을 보며 풀이법을 공유해주시면 됩니다.
나머지 문제의 PR 의 경우엔 비교적 간단하게 작성하셔도 상관없습니다.
PR 같은 경우 본인이 직접 merge 해주시면 되는데 가급적이면 파트너가 코드 리뷰한 뒤에 merge 해주시면 좋아요. 단, 몇일이 걸릴지 모르니 스터디 전엔 모두 merge 해주시고 PR 보내고 하루이틀이 지나도 파트너가 코드리뷰를 달지 않으면 일단 merge 해주세요. 파트너는 자신의 파트너의 PR closed 기록에 코드리뷰를 달아주시면 됩니다.

> merge 전에 한번 Fetch 를 클릭해보세요~! 만약 PR 을 요청한 내 커밋이 가장 최신 main 브랜치로부터 나온 것이 아니라면 rebase 가 필요합니다. fork 툴을 사용한 rebase 방법은 하단에 방법을 설명해두었습니다.
> merge 된 원격 브랜치는 삭제해주세요~ 인원이 많다보니 원격 브랜치가 많아지면 복잡해집니다..

<img width="498" alt="스크린샷 2023-12-09 오후 10 38 38" src="https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/daca4169-da6b-4c82-b5f1-8683d834b465">

<img width="800" alt="스크린샷 2023-12-09 오후 10 44 23" src="https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/2db618cb-3161-486d-9c25-4b3e4297d63a">

### PR 방법

<details>

<summary>풀이법을 공유할 문제의 PR</summary>

![github com_Stendhalsynd_baekjoon-algorithm-study_pull_141](https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/e64c8c33-777d-4d90-ad88-211b57cf3aa1)


- 주차별 문제로 폴더를 생성하여 해당 폴더 내에 풀이 코드를 업로드한다.
  - ex) `week9/BOJ_18352/특정 거리의 도시 찾기.py`

</details>

<details>

<summary>일반적인 문제들의 PR</summary>

<img width="729" alt="스크린샷 2023-12-09 오후 9 52 29" src="https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/f96c7446-2b26-4b07-ac03-1c02d9b05227">

- 주차별 문제로 폴더를 생성하여 해당 폴더 내에 풀이 코드를 업로드한다.
  - ex) `week9/BOJ_18352/특정 거리의 도시 찾기.py`

</details>

### `fork` 프로그램을 통해 PR 및 rebase, 브랜치, 커밋 관리하기 ⭐️

<details>

<summary>PR 후 다음 문제를 풀때 or 다른 스터디원이 커밋 혹은 merge 했을때 - `rebase 하기`</summary>

- git 명령어로 rebase 를 해주셔도 좋고 아니면 window / mac 모두 사용 가능한 GUI git 툴인 `fork` 를 사용하셔도 좋습니다. 설명은 `fork` 를 기준으로 명시해두었습니다.

![스크린샷 2023-12-09 오후 10 08 13](https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/b9930eac-7130-416f-8d40-11d87a4cc3a4)

![스크린샷 2023-12-09 오후 10 09 57](https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/7a98fc8d-de0c-433f-9403-145d788c90a7)

#### fork 사용법 1. 좌측 메뉴바

- Local Changes 는 아직 unstaged 된 변경사항, staged 된 변경사항을 확인할 수 있고 Commit subject 에 커밋할 이름, Description 에 커밋 상세내용, Amend 체크시 이전 커밋과 현재 변경점을 합쳐 새로운 커밋을 생성하지 않아도 기존 커밋에 새로 staged 에 올린 변경점을 반영할 수 있습니다.

![스크린샷 2023-12-09 오후 10 14 08](https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/9f07eac9-2ad8-463c-b00a-b47211b4eb44)

![스크린샷 2023-12-09 오후 10 24 42](https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/c8eb8ba8-5af3-4e8f-bf77-e75e5a94dd3e)

이렇게 Staged 된 변경점이 있으면 해당 파일을 커밋할 수 있게 됩니다.

- All Commits 는 모든 커밋 기록을 볼 수 있습니다. 상단에 Fetch 를 클릭하면 새로고침이 되어서 스터디원들중 코드를 merge 했는지 내 커밋이 어떤 상황인지 한눈에 파악할 수 있어요.

![스크린샷 2023-12-09 오후 10 17 32](https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/b3b5cbc5-dab5-40a2-a808-abd547a7179b)

![스크린샷 2023-12-09 오후 10 18 32](https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/0f52d9ec-ea20-45c6-b99e-711d885a2a8d)

#### fork 사용법 2. 브랜치 생성

![스크린샷 2023-12-09 오후 10 20 03](https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/fc050b2c-05c0-4cb5-8417-73c042f15423)

마우스 우클릭 하시면 New Branch 를 클릭하여 브랜치를 생성할 수 있습니다.

저 주황색 박스가 로컬 브랜치이며 상단에 Push 를 해주시면 원격 저장소에 push 가 되어 왼쪽에 깃허브 아이콘이 나타납니다. 

초록생 박스가 원격 저장소를 나타냅니다.

#### fork 사용법 3. 체크아웃 방법

![스크린샷 2023-12-09 오후 10 22 39](https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/37ab83e3-3d02-42ab-9285-fd61ad9f036f)

![스크린샷 2023-12-09 오후 10 22 52](https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/d7c7304b-da8d-4e86-9c2e-234782d98820)

로컬브랜치가 있거나 아니면 원격 저장소만 있는 곳에 좌클릭으로 더블클릭해주면 주황색 박스 영역에 체크 표시가 뜨게 됩니다. 그러면 해당 브랜치에 체크아웃이 되어있다는 의미입니다.

#### fork 사용법 4. 응용

![스크린샷 2023-12-09 오후 10 25 37](https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/374c8ed7-7737-4632-b1f6-1d844906b18d)

현재 어떤 문제를 풀었고 push 하여 PR 을 요청한 상태입니다.
다음 문제를 풀려면 어떻게 해야할까요?
커밋을 하게된 시점에 새로 branch 를 생성하여 다음 문제를 풀기 시작해주세요.

![스크린샷 2023-12-09 오후 10 27 55](https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/c235f6d3-7421-43df-af56-c89e3e9f5c03)

![스크린샷 2023-12-09 오후 10 28 08](https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/ad03383c-79b1-409f-913f-fc486ac047e3)

![스크린샷 2023-12-09 오후 10 28 23](https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/fb828368-1341-442f-beff-9b684f453c0e)

브랜치는 해당 경로를 통해 삭제해줄 수 있습니다.

![스크린샷 2023-12-09 오후 10 28 48](https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/7085f11d-1506-40a5-8c98-9d170936029e)

이번엔 내가 몇일 전에 PR 을 요청했는데 다른 스터디원들이 커밋을 했거나 merge 가 된 상황입니다. 이때는 바로 merge 를 하는 것이 아니고 `rebase` 를 해주세요. `rebase` 는 내 base 를 가장 최근 `main` 브랜치 위로 이동시켜줄 수 있도록 합니다. 

![스크린샷 2023-12-09 오후 10 30 06](https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/fcc1ba05-985b-4533-b5c1-f415deb5dae1)

먼저 rebase 하고싶은 내 커밋의 로컬 브랜치에 더블클릭하여 체크아웃해줍니다.

![스크린샷 2023-12-09 오후 10 31 42](https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/86efc24f-6708-498a-8e5b-eca4bdc113ca)

그리고 rebase 를 하고 싶은 목적지에 우클릭을 하면 interactively rebase ... 라는 것을 클릭합니다.

![스크린샷 2023-12-09 오후 10 32 22](https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/9743f438-4f0b-43b2-89f1-b95be209ea4f)

rebase 는 로컬 브랜치만 이동시킵니다. 따라서 초록색 영역의 원격 브랜치도 내 로컬 브랜치에 따라오도록 하려면 상단의 push 를 해줘야 합니다.

![스크린샷 2023-12-09 오후 10 34 31](https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/469c48f0-d3fb-44b1-b5e4-b73df0c0cf56)

아마 변경점이 있는데 저 Force push 체크를 하지 않으면 오류가 뜰 수도 있어요.

![스크린샷 2023-12-09 오후 10 34 50](https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/e633428c-5776-43a0-8586-ec0931edfb01)

그러면 아래와 같이 커밋을 깔끔하게 rebase 해줄 수 있습니다. 이 상태에서 merge 를 해주시면 됩니다.

![스크린샷 2023-12-09 오후 10 35 36](https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/a524cd7c-3bf1-4cd9-8807-8acc41eb7770)

squash 는 다음과 같은 상황에 사용합니다.

<img width="529" alt="스크린샷 2023-12-09 오후 10 39 35" src="https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/98fa81cf-65af-45de-9e69-1b49cf24b754">

불필요하게 커밋이 두번 나온 상황입니다. 이걸 하나로 합쳐줄때 squash 를 사용합니다.

합치고 싶은 커밋에 우클릭을 하면 아래와 같이 squash 를 할 수 있습니다.

<img width="651" alt="스크린샷 2023-12-09 오후 10 40 08" src="https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/4b7c60de-e0c8-4ffb-96af-ecb0b65e8967">

<img width="937" alt="스크린샷 2023-12-09 오후 10 40 54" src="https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/4c7b5372-300e-4259-8994-3d69c746fd9d">

</details>

### ✅ 코드리뷰 규칙 

- 매주 사다리타기로 각 멤버별 파트너를 선정합니다. 그 주엔 해당 파트너의 PR 만큼은 꼭 코드리뷰할 수 있도록 노력해주세요~!!
- PR 에서 코드 리뷰를 한다.
- 전체 코드 흐름 파악한 뒤, 이 분이 어떻게 풀었을까 이해한 후 의견 제시
  - 잘했다고 생각하는 부분
  - 이렇게 하면 더 좋을 것 같다고 생각하는 부분
  - 왜 이렇게 풀었는지 궁금한 부분
  - 또 다른 풀이 방법 제시
- 코드 일부분에 코드 리뷰를 해도 되고 전체 코드 및 or PR 밑에 코멘트 작성으로 리뷰를 해도 됩니다.

`파트너체계`

<img width="888" alt="스크린샷 2023-12-09 오후 10 04 50" src="https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/d87fba58-7d59-4fe0-bd11-c93d00be70bd">


# 😀 브랜치 생성

- 문제별로 브랜치를 만들어 각 문제별 PR 을 요청해주세요.
- ex) 플랫폼_문제이름(문제번호)_본인이름 -> BOJ_10164_홍지훈 / PSG_양궁대회_홍지훈
- 백준은 중간에 문제번호를, PSG 는 문제번호가 없으니 문제이름을 붙여주세요.

<details>

<summary>브랜치 관리</summary>

<img width="393" alt="스크린샷 2023-12-09 오후 9 55 24" src="https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/d5b54848-43d5-4abb-bb1b-72e9aa17142c">
<img width="162" alt="스크린샷 2023-12-09 오후 9 57 03" src="https://github.com/Stendhalsynd/baekjoon-algorithm-study/assets/96957774/b62fb5ea-a5f2-428e-963e-2dd7c432543d">


> 브랜치명으로 `PSG_양궁대회_홍지훈` 를 생성한 모습.

</details>


</details>

# ⭐️ 백준 알고리즘 스터디 1기 멤버 
>  `2023.10.09 ~ 2023.12.03` 

| <a href="https://github.com/jojaegu2"><img src="https://avatars.githubusercontent.com/u/65579171?v=4" width="150px"/></a> | <a href="https://github.com/JeongEunBae"><img src="https://avatars.githubusercontent.com/u/59482764?v=4" width="150px"/></a> | <a href="https://github.com/Stendhalsynd"><img src="https://velog.velcdn.com/images/qmflf556/post/19704a5b-0640-4675-b149-abb432c38cd2/image.png" width="150px"/></a> | <a href="https://github.com/96Hong2"><img src="https://avatars.githubusercontent.com/u/62095603?v=4" width="150px"/></a> | <a href="https://avatars.githubusercontent.com/u/62095603?v=4"><img src="https://avatars.githubusercontent.com/u/96766683?v=4" width="150px"/></a> | <a href="https://github.com/vichye-1"><img src="https://avatars.githubusercontent.com/u/66904886?v=4" width="150px"/></a> |
| --- | --- | --- | --- | --- | --- |
| 조재은 | 배정은 | 홍지훈 | 은홍 | 이동혁 | 양승혜 |

# 📅 3기 일정표 ( 매주 7문제 )

|                     | 1                                                   | 2                                            | 3                                                        | 4                                                     | 5                                                   | 6                                                 | 7                                                   |
| ------------------- | --------------------------------------------------- | -------------------------------------------- | -------------------------------------------------------- | ----------------------------------------------------- | --------------------------------------------------- | ------------------------------------------------- | --------------------------------------------------- |
| 17주차 (2.13~2.18)  | [로프](https://www.acmicpc.net/problem/2217) | [주유소](https://www.acmicpc.net/problem/13305) | [뒤집기 2](https://www.acmicpc.net/problem/1455) | [강의실 배정](https://www.acmicpc.net/problem/11000) | [우체국](https://www.acmicpc.net/problem/2141) | [택배](https://www.acmicpc.net/problem/8980) | [생략](생략) |
| 18주차 (2.19~2.25)  | [2xn 타일링 2](https://www.acmicpc.net/problem/11727) | [1,2,3 더하기 5](https://www.acmicpc.net/problem/15990) | [카드 구매하기](https://www.acmicpc.net/problem/11052) | [합분해](https://www.acmicpc.net/problem/2225) | [가장 긴 바이토닉 부분 수열](https://www.acmicpc.net/problem/11054) | [파일 합치기](https://www.acmicpc.net/problem/11066) | [플레이리스트](https://www.acmicpc.net/problem/12872) |
| 19주차 (2.26~3.3)  | [두 스티커](https://www.acmicpc.net/problem/16937) | [테트리스](https://www.acmicpc.net/problem/3019) | [캠프 준비](https://www.acmicpc.net/problem/16938) | [배열 돌리기 4](https://www.acmicpc.net/problem/17406) | [NxM 보드 완주하기](https://www.acmicpc.net/problem/9944) | [괄호 추가하기](https://www.acmicpc.net/problem/16637) | [괄호 변환](https://school.programmers.co.kr/learn/courses/30/lessons/60058) |
| 20주차 (3.4~3.10)  | [늑대와 양](https://www.acmicpc.net/problem/16956) | [아기 상어 2](https://www.acmicpc.net/problem/17086) | [스타트링크](https://www.acmicpc.net/problem/5014) | [물통](https://www.acmicpc.net/problem/2251) | [연구소2](https://www.acmicpc.net/problem/17141) | [연구소3](https://www.acmicpc.net/problem/17142) | [문자열 압축](https://school.programmers.co.kr/learn/courses/30/lessons/60057) |

# 📅 2기 일정표 ( 매주 7문제 )

|                     | 1                                                   | 2                                            | 3                                                        | 4                                                     | 5                                                   | 6                                                 | 7                                                   |
| ------------------- | --------------------------------------------------- | -------------------------------------------- | -------------------------------------------------------- | ----------------------------------------------------- | --------------------------------------------------- | ------------------------------------------------- | --------------------------------------------------- |
| 9주차 (12.11~12.17)  | [특정 거리의 도시 찾기](https://www.acmicpc.net/problem/18352) | [경로 찾기](https://www.acmicpc.net/problem/11403) | [친구](https://www.acmicpc.net/problem/1058) | [지름길](https://www.acmicpc.net/problem/1446)   | [Small World Network](https://www.acmicpc.net/problem/18243) | [k진수에서 소수 개수 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/92335)   | [숨바꼭질](https://www.acmicpc.net/problem/13549) |
| 10주차 (12.18~12.24)  | [DNA](https://www.acmicpc.net/problem/1969) | [숫자 야구](https://www.acmicpc.net/problem/2503) | [도영이가 만든 맛있는 음식](https://www.acmicpc.net/problem/2961) | [오목](https://www.acmicpc.net/problem/2615) | [링크와 스타트](https://www.acmicpc.net/problem/15661)   | [테트로미노](https://www.acmicpc.net/problem/14500)  | [행렬 테두리 회전하기](https://school.programmers.co.kr/learn/courses/30/lessons/77485) |
| 11주차 (12.25~12.31)  | [등수 구하기](https://www.acmicpc.net/problem/1205) | [한 줄로 서기](https://www.acmicpc.net/problem/1138) | [비슷한 단어](https://www.acmicpc.net/problem/2607) | [단어 맞추기](https://www.acmicpc.net/problem/9081) | [배열 돌리기 3](https://www.acmicpc.net/problem/16935)   | [치즈](https://www.acmicpc.net/problem/2636)  | [순위 검색](https://school.programmers.co.kr/learn/courses/30/lessons/72412) |
| 12주차 (1.1~1.7)  | [돌 게임](https://www.acmicpc.net/problem/9655) | [1로 만들기](https://www.acmicpc.net/problem/1463) | [가장 큰 증가하는 부분 수열](https://www.acmicpc.net/problem/11055) | [점프](https://www.acmicpc.net/problem/1890) | [LCS](https://www.acmicpc.net/problem/9251) | [함께 블록 쌓기](https://www.acmicpc.net/problem/18427)  | [메뉴 리뉴얼](https://school.programmers.co.kr/learn/courses/30/lessons/72411) |
| 13주차 (1.8~1.14)  | [트럭](https://www.acmicpc.net/problem/13335) | [요세푸스 문제](https://www.acmicpc.net/problem/1158) | [킹](https://www.acmicpc.net/problem/1063) | [마법사 상어와 비바라기](https://www.acmicpc.net/problem/21610) | [마법사 상어와 파이어볼](https://www.acmicpc.net/problem/20056) | [마법사 상어와 블리자드](https://www.acmicpc.net/problem/21611)  | [도넛과 막대 그래프](https://school.programmers.co.kr/learn/courses/30/lessons/258711) |
| 14주차 (1.15~1.21)  | [동방 프로젝트 (Small)](https://www.acmicpc.net/problem/14594) | [거북이](https://www.acmicpc.net/problem/8911) | [지구 온난화](https://www.acmicpc.net/problem/5212) | [후보 추천하기](https://www.acmicpc.net/problem/1713) | [인구 이동](https://www.acmicpc.net/problem/16234) | [상어 중학교](https://www.acmicpc.net/problem/21609) | [수식 최대화](https://school.programmers.co.kr/learn/courses/30/lessons/67257) |
| 15주차 (1.22~1.28)  | [유기농 배추](https://www.acmicpc.net/problem/1012) | [쉬운 최단거리](https://www.acmicpc.net/problem/14940) | [봄버맨](https://www.acmicpc.net/problem/16918) | [단지번호붙이기](https://www.acmicpc.net/problem/2667) | [연구소](https://www.acmicpc.net/problem/14502) | [벽 부수고 이동하기](https://www.acmicpc.net/problem/2206) | [원 이동하기 1](https://www.acmicpc.net/problem/22946) |
| 16주차 (1.29~2.4)  | [섬의 개수](https://www.acmicpc.net/problem/4963) | [섬의 개수](https://www.acmicpc.net/problem/4963) | [현수막](https://www.acmicpc.net/problem/14716) | [공주님을 구해라!](https://www.acmicpc.net/problem/17836) | [일루미네이션](https://www.acmicpc.net/problem/5547) | [로봇](https://www.acmicpc.net/problem/1726) | [모래성](https://www.acmicpc.net/problem/10711) |

# 📅 1기 일정표 ( 매주 7문제 )

|                     | 1                                                   | 2                                            | 3                                                        | 4                                                     | 5                                                   | 6                                                 | 7                                                   |
| ------------------- | --------------------------------------------------- | -------------------------------------------- | -------------------------------------------------------- | ----------------------------------------------------- | --------------------------------------------------- | ------------------------------------------------- | --------------------------------------------------- |
| 1주차 (10.9~10.15)  | [대표 자연수](https://www.acmicpc.net/problem/2548) | [ATM](https://www.acmicpc.net/problem/11399) | [블랙 프라이데이](https://www.acmicpc.net/problem/18114) | [단어 나누기](https://www.acmicpc.net/problem/1251)   | [회의실 배정](https://www.acmicpc.net/problem/1931) | [두 용액](https://www.acmicpc.net/problem/2470)   | [수리공 항승](https://www.acmicpc.net/problem/1449) |
| 2주차 (10.16~10.22) | [스택](https://www.acmicpc.net/problem/10828)       | [괄호](https://www.acmicpc.net/problem/9012) | [프린터 큐](https://www.acmicpc.net/problem/1966)        | [풍선 터뜨리기](https://www.acmicpc.net/problem/2346) | [쇠막대기](https://www.acmicpc.net/problem/10799)   | [괄호 제거](https://www.acmicpc.net/problem/2800) | [괄호의 값](https://www.acmicpc.net/problem/2504)   |
| 3주차 (10.23~10.29) | [기적의 매매법](https://www.acmicpc.net/problem/20546)       | [지뢰 찾기](https://www.acmicpc.net/problem/4396) | [달팽이](https://www.acmicpc.net/problem/1913)        | [달력](https://www.acmicpc.net/problem/20207) | [기차가 어둠을 헤치고 은하수를](https://www.acmicpc.net/problem/15787)   | [배열 돌리기 1](https://www.acmicpc.net/problem/16926) | [ZOAC](https://www.acmicpc.net/problem/16719)   |
| 4주차 (10.30~11.5) | [빙고](https://www.acmicpc.net/problem/2578)       | [ZOAC 3](https://www.acmicpc.net/problem/20436) | [상어 초등학교](https://www.acmicpc.net/problem/21608)        | [오리](https://www.acmicpc.net/problem/12933) | [오목](https://www.acmicpc.net/problem/2615)   | [원상 복구](https://www.acmicpc.net/problem/22858) | [빗물](https://www.acmicpc.net/problem/14719)   |
| 5주차 (11.6~11.12) | [바이러스](https://www.acmicpc.net/problem/2606)       | [DFS와 BFS](https://www.acmicpc.net/problem/1260) | [트리의 부모 찾기](https://www.acmicpc.net/problem/11725)        | [효율적인 해킹](https://www.acmicpc.net/problem/1325) | [미로 탐색](https://www.acmicpc.net/problem/2178)   | [토마토](https://www.acmicpc.net/problem/7576) | [택배 배달과 수거하기](https://school.programmers.co.kr/learn/courses/30/lessons/150369)   |
| 6주차 (11.13~11.19) | [스위치 켜고 끄기](https://www.acmicpc.net/problem/1244)       | [별 찍기 - 19](https://www.acmicpc.net/problem/10994) | [배열 돌리기](https://www.acmicpc.net/problem/17276)        | [단어 뒤집기 2](https://www.acmicpc.net/problem/17413) | [홀수 홀릭 호석](https://www.acmicpc.net/problem/20164)   | [사탕 게임](https://www.acmicpc.net/problem/3085) | [택배 배달과 수거하기](https://school.programmers.co.kr/learn/courses/30/lessons/150369)   |
| 7주차 (11.20~11.26) | [다리 놓기](https://www.acmicpc.net/problem/1010)       | [설탕 배달](https://www.acmicpc.net/problem/2839) | [Four Squares](https://www.acmicpc.net/problem/17626)        | [가장 긴 증가하는 부분 수열](https://www.acmicpc.net/problem/11053) | [스티커](https://www.acmicpc.net/problem/9465)   | [퇴사 2](https://www.acmicpc.net/problem/15486) | [두 큐 합 같게 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/118667)   |
| 8주차 (11.27~12.3) | [파스칼 삼각형](https://www.acmicpc.net/problem/15489)       | [격자상의 경로](https://www.acmicpc.net/problem/10164) | [과일 서리](https://www.acmicpc.net/problem/17213)        | [단어 맞추기](https://www.acmicpc.net/problem/9081) | [암호](https://www.acmicpc.net/problem/1394)   | [주차 요금 계산](https://school.programmers.co.kr/learn/courses/30/lessons/92341) | [양궁 대회](https://school.programmers.co.kr/learn/courses/30/lessons/92342)   |

# 📚 블로깅 및 노션 정리

|          | 블로그 / 노션 | 알고리즘                    | 작성자   |
| -------- | ------------- | --------------------------- | -------- |
| 1  | [js sort 특징](https://velog.io/@qmflf556/11399.-ATM)  | `정렬` | 홍지훈 |
| 2  | [브루트 포스 (Brute Force, 완전 탐색)](https://velog.io/@jeongeunbae/Algorithms-브루트-포스-Brute-Force-완전-탐색-mllrvvmx) | `브루트 포스 (완전 탐색)` | 배정은 |
| 3 | [python 문법 for algorithm](https://velog.io/@qmflf556/%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%A5%BC-%EC%9C%84%ED%95%9C-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%AC%B8%EB%B2%95) | `python 문법` | 홍지훈 |
| 4 | [그리디 알고리즘 및 자료형별 시간복잡도](https://velog.io/@qmflf556/%EA%B7%B8%EB%A6%AC%EB%94%94-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%8B%9C%EA%B0%84-%EB%B3%B5%EC%9E%A1%EB%8F%84%EB%B3%84-%EB%A9%94%EC%86%8C%EB%93%9C-%EB%B6%84%EB%A5%98) | `greedt algorithm`, `time complexity` | 홍지훈 |
| 5 | [fork 툴을 활용한 rebase 방법](https://velog.io/@qmflf556/fork-%ED%88%B4-%EC%82%AC%EC%9A%A9%EB%B2%95) | `fork`, `rebase` | 홍지훈 |
| 6 | [matrix 3가지 풀이 - transpose, reverse, rotate](https://velog.io/@qmflf556/algorithm-matrix-transpose-reverse-rotate) | `matrix`, `transpose`, `reverse`, `rotate` | 홍지훈 |
| 7 | [Floyd's algorithm](https://velog.io/@qmflf556/Floyd-algorithm) | `likedlist`, `cycle` | 홍지훈 |
| 8 | [Linked List](https://velog.io/@qmflf556/%EC%97%B0%EA%B2%B0%EB%A6%AC%EC%8A%A4%ED%8A%B8) | `likedlist` | 홍지훈 |
| 9 | [비트마스킹 알고리즘](https://velog.io/@qmflf556/%EB%B9%84%ED%8A%B8%EB%A7%88%EC%8A%A4%ED%82%B9-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98) | `비트마스킹` | 홍지훈 |
| 10 | [배열돌리기](https://velog.io/@qmflf556/16926-%EB%B0%B0%EC%97%B4-%EB%8F%8C%EB%A6%AC%EA%B8%B0) | `matrix`, `구현`, `rotate` | 홍지훈 |
| 11 | [입력타입 정리](https://velog.io/@qmflf556/%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%9E%85%EB%A0%A5-%ED%83%80%EC%9E%85-%EC%A0%95%EB%A6%AC) | `input` | 홍지훈 |
| 12 | [트리](https://velog.io/@qmflf556/%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%ED%8A%B8%EB%A6%AC) | `tree`, `traversal` | 홍지훈 |
| 13 | [bfs & dfs](https://velog.io/@qmflf556/DFS-BFS) | `bfs`, `dfs` | 홍지훈 |
| 14 | [최단경로](https://velog.io/@qmflf556/%EC%B5%9C%EB%8B%A8-%EA%B2%BD%EB%A1%9C-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98) | `다익스트라`, `플로이드 워셜` | 홍지훈 |
| 15 | [우선순위 큐](https://velog.io/@qmflf556/%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84-%ED%81%90) | `우선순위큐` | 홍지훈 |
| 16 | [비트마스킹 알고리즘2](https://velog.io/@qmflf556/%EB%B9%84%ED%8A%B8%EB%A7%88%EC%8A%A4%ED%82%B9-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-2) | `비트마스킹` | 홍지훈 |


# 🤗 참고 레퍼런스

- [알고리즘 및 코딩 테스트 문제 풀이 챌린지 100](https://github.com/ellynhan/challenge100-codingtest-study)
- [알고리즘 및 코딩 테스트 문제 풀이](https://github.com/Seongho0503/Algo_Study)
- [코딩 테스트 기출 문제 풀이 및 업로드](https://github.com/CodeTest-StudyGroup/Code-Test-Study)
- [알고리즘 스터디1](https://github.com/b1urrrr/Algorithm-Study)
- [알고리즘 스터디2](https://github.com/CodeSquad-2023-BE-Study/Algorithm-Study)
- [초심자를 위한 기술면접 가이드](https://github.com/JaeYeopHan/Interview_Question_for_Beginner)
