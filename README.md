# 원재와 함께하는 스터디
> 김동현 김승주 정규식

## Table of Contents (Optional)

> If your `README` has a lot of info, section headers might be nice.

- [Pre-setting](#pre-setting)
- [GIt](#git)

---

## Pre-setting

- [Python](https://www.python.org/downloads/)
- [PyCharm](https://www.jetbrains.com/ko-kr/pycharm/download/)
- [Git Bash](https://gitforwindows.org/)

---

## Git

- 만든이 : [리누스 토발즈](https://ko.wikipedia.org/wiki/%EB%A6%AC%EB%88%84%EC%8A%A4_%ED%86%A0%EB%A5%B4%EB%B0%9C%EC%8A%A4)

(리눅스와 Git을 만든사람으로 유명, 퍼블릭 클라우드 워크로드의 90%, 세계 스마트폰의 82%, 임베디드 기기의 62%, 슈퍼 컴퓨터 시장의 99%가 리눅스로 작동한다)

- 깃(Git)은 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율하기 위한 분산 버전 관리 시스템이다.
소프트웨어 개발에서 소스 코드 관리에 주로 사용되지만 어떠한 집합의 파일의 변경사항을 지속적으로 추적하기 위해 사용될 수 있다.

### Overview

![image](https://camo.githubusercontent.com/5339022528f65f8db050a6326e123f404cbf4275/68747470733a2f2f64316a6e783962613873366a39722e636c6f756466726f6e742e6e65742f626c6f672f77702d636f6e74656e742f75706c6f6164732f323031362f31312f4769742d417263686974656368747572652d4769742d5475746f7269616c2d45647572656b612d322d373638783732302e706e67)

### Git Branch

![](https://i.stack.imgur.com/F00b8.png)

- Git은 여러 Branch를 운영하며 안정적인 개발을 할 수 있게 해줍니다.

---

### 사용법

#### 1. Clone

- Github 혹은 remote Git Repository를 내 Local로 복사해오는 작업을 말한다.

##### Sample
![](https://user-images.githubusercontent.com/18394695/73465276-7e028700-43c3-11ea-8f80-192fad7b800d.png)

---

#### 2. git add

- 현재 내 작업 분량을 Staging Area(녹색)로 이동하는 작업을 말한다

##### Sample
![](https://user-images.githubusercontent.com/18394695/73465434-bdc96e80-43c3-11ea-9d07-763be11f1d93.png)

---

#### 3. git commit

- 현재 내 Staging Area(녹색)에 저장된 변경분을 하나의 commit으로 만드는 작업을 말한다(한 시점을 긋는다)

##### Sample
![](https://user-images.githubusercontent.com/18394695/73465588-ec474980-43c3-11ea-823d-e10840b7e4d2.png)

---

#### 4. git push

- 내 Local에 작업한 commit들을 Remote 저장소(origin 또는 Cloud 또는 Github)에 업로드하는 작업을 말한다.

##### Sample
![](https://user-images.githubusercontent.com/18394695/73465680-10a32600-43c4-11ea-8775-ede438e8b0b9.png)

---

#### 번외1. Branch 바꾸기 (git checkout)

- 현재 Branch에서 다른 Branch로 갈아타는 작업을 말한다

##### Sample
![](https://user-images.githubusercontent.com/18394695/73466511-4eed1500-43c5-11ea-9d11-3891857eeba6.png)

---

#### 번외2. git pull

- 내 Local에서 마지막에 pull 한 시점부터 현재 Remote에 업로드된 commit의 변경량 만큼을 가져오는 작업을 말한다.
- 번외1을 진행했다면 그냥 git pull만 해도 된다.

##### Sample
![](https://user-images.githubusercontent.com/18394695/73466755-a8edda80-43c5-11ea-8d69-72cd53115ea9.png)

---
