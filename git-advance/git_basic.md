# git 01

## ※ WARNING
1. **현재 위치를 잘 확인한다.**
2. **Repo 안에서 repo (master)를 만들지 않는다. (Master 떠있으면 `git init` X)**
   > 리포지토리 안에 리포리지토리 만들 지 x (git init을 한 곳 안에 하위 폴더를 만들고 그 하위 폴더에서 git init하지 않는다!)
3. **Home(`~`)에서 init 하지 않는다.**
4. **git을 잘 쓸줄 모르면(브런치 개념이 없으면) github에서 직접 수정하지 않는다.**
   
---
## 기초 

Git의 Repository 구조는 크게 세 가지로 구성되어 있다.

```
작업폴더(Working directory) > 인덱스(Staging Area) > 저장소(Head -Repository)
```

우리가 작업하는 폴더를 `작업트리(Working directory)`라고 부르며 commit을 실행하기 전에 작업트리와 저장소 사이에 존재하는 가상의 준비 영역(Staging Area)을 `인덱스(Index)`라고 함

저장소에 commit하기 위헤서 먼저 추가(Untracked files) 및 변경(Modified files) 하고자 하는 파일을 먼저 `인덱스에 기록(Stage)`하고 이후 스테이징된 목록만 최종적으로 commit 명령어에 의해 저장소에 공개하게 됨 

.gitignore 파일 생성 시 https://www.toptal.com/developers/gitignore 사이트를 이용하면 편하게 생성할 수 있음. 사용법은 windows, python, Django 같은 단어들을 개별적으로 검색해서 추가하고 생성버튼을 누르면 됨 

Git의 '커밋' 작업은 '작업트리'에 있는 변경 내용을 저장소에 바로 기록하는 것이 아닌 그 사이 공간인 '인덱스'에 파일 상태를 기록(Stage-스테이징이라고 표현하기도 함)하게 되어 있음. 따라서 저장소에 변경 사항을 기록하기 위해서는, 기록하고자 하는 모든 변경사항들이 '인덱스'에 존재해야 함. 

ex. 10개의 파일을 수정했으나 그 중 7개만 저장소에 공개하고 싶을 때, 그 일부 파일만을 선택하는 작업이 바로 '인덱스 등록' 또는 '스테이징(Stage)'라고 표현하는 작업인 것 

이렇게 인덱스란 가상 공간이 중간에 있는 덕분에 작업 트리 안에 있는 커밋이 필요 없는 파일들을 커밋에 포함하지 않을 수 있고, 파일에서 내가 원하는 일부 변경 사항만 인덱스에 등록해 커밋 가능 (backlog, 작업트리와 인덱스)


### 쉬운 설명
영화 촬영에 비유하자면? 

1. 분장실 (작업트리, working directory)
2. 스테이지 (Stage, 인덱스)
3. 커밋들 (commits)

이때, 1 → 2로 가는 명령이 add이고, 2 → 3으로 가는 명령이 commit이고 뒤로 가는 명령 (reset, pull)도 존재한다. 

---

## git 사용 중 추천 사항
1. 커밋 메세지는 짧지만 내용을 담을 것 
2. 모든 Repo(프로젝트)는 READEME.md, .gitignore 파일을 만들 것! 
   
---
## git 시스템 관련 
## 프로젝트 초기화 진행

### 계정 세팅

```sh
# (계정당 1회) 서명이 등록되지 않았다면, 계정용 서명 등록
$ git config --global user.name '내이름'
$ git config --global user.email 'github에서@쓸메일주소'
# 서명이 정상적으로 등록되었는지 확인
$ cat ~/.gitconfig  
```

### config
git의 config 설정을 확인한다. 빠져나오고 싶지만 프롬프트 `$`가 나타나지 않는 경우 `Q`를 누르면 빠져나올 수 있다.


| 옵션   | 설명                               | 예시                                                 |
| ------ | ---------------------------------- | ---------------------------------------------------- |
| --list | config 리스트를 출력한다.          | `$ git config --list`                                |
| --list | config에 이름을 등록한다.          | `$ git config --global user.name 'name'`             |
| --list | config에 이메일을 등록한다.        | `$ git config --global user.email 'email@gmail.com'` |
| --list | config에 등록된 이름을 출력한다.   | `$ git config --user.name`                           |
| --list | config에 등록된 이메일을 출력한다. | `$ git config --user.email`                          |


### status
현재 git의 상태를 나타낸다. 현재 스테이징 / 커밋된 파일이 나타나 push가 필요한 파일을 알 수 있다. 
```
$ git status
```

### log
커밋 히스토리를 조회한다. config 확인과 마찬가지로 빠져나오고 싶으면 `Q`를 누른다.
```
$ git log
$ git log --oneline
$ git log --oneline --graph # 깃 commit 로그를 자세히 출력한다. (그래프 포함)
```

## 로컬 저장소 업데이트 

#### 로컬 저장소(Repository) 생성
현재 디렉토리를 로컬 저장소로 만든다. (.git 폴더 생성)
```
$ git init
``` 
> Giit을 사용할 때 보통 이미 생성해 놓은 Git 원격 저장소를 git clone 명령어를 통해 내려받기 하는 경우가 많고, 직접 Git 저장소를 생성하더라도 프로젝트 초기에 딱 한 번만 사용하기 때문에 생소하게 느껴질 수도 있는 명령어 

### 로컬 저장소 url 변경

GitHub repository 이름을 변경한 경우 다음과 같이 변경된 url을 로컬 저장소에 적용해줌 
```
$ git remote set-url origin <url>
```

### 로컬 저장소 해제
```
$ rm -rf .git 
``` 

### add 
특정 파일을 stage에 올림 
```
$ git add a.txt
$ git add .
```

### 스테이징된 파일 되돌리기 
`git rm --cached <file>...` 명령을 사용하여 스테이징된 파일을 되돌린다. 
(커밋하고 싶지 않은 파일이 실수로 올라갔을 경우 사용)
```
$ git rm --cached a.txt
```

### commit
스테이징된 파일을 최종 확정 (커밋은 신중히! 올라가면 안되는 내용이 포함된 폴더 혹은 파일이 올라가진 않았을 지? ex. api secret key, 저작권 침해 우려가 있는 파일 등)
```
$ git commit -m a.txt '변경 메시지'
$ git commit -a -m a.txt '변경 메시지' # add와 commit을 한번에 한다. 
```
* commit 메시지 수정 
```
$ git commit --amend -m "new commit message"
```

### reset (커밋 취소-git 실수 되돌리기)
스테이징된 파일을 되돌린다.
* reset 옵셥 
    - --soft : index 보존(add한 상태, staged 상태), 워킹 디렉터리의 파일 보존(즉, 모두 보존)
    ```
    $ git reset --soft 30ccdae58f4d86s
    ```
    - --mixed : index 취소(add하기 전 상태, unstagged 상태), 워킹 디렉터리의 파일 보존(기본 옵션)
    ```
    $ git reset --mixed 30ccdae58f4d86s
    ```
    - --hard : index 취소(add하기 전 상태), 워킹 디렉터리의 파일 삭제(즉 모두, 취소)
    ```
    $ git reset --hard 30ccdae58f4d86s
    ```

* reset HEAD~ 
- HEAD란 현재 내가 위치해 있는 커밋을 가리키는 식별자 
- HEAD 뒤에 숫자를 넣으면 마지막 n개의 commit 취소 가능 
```
# 특정 파일의 add만 취소하고, 파일명을 적지 않으면 add된 파일 전체를 unstaged 상태로 되돌림
$ git reset HEAD <filename>
# git log에서 지금까지 수행된 각 commit의 HEAD 번호와 고유한 id를 확인
$ git log 
# HEAD가 가리켰던 commit 기록을 모두 보여주는 명령어 
$ git reflog
# 마지막 n개의 commit을 취소
$ git reset <option> HEAD~1
```

### restor 
특정 커밋으로 되돌리거나 unstaging함 
```
$ git restore a.txt
```

### 파일 삭제 
1. 원격 저장소와 로컬 저장소에 있는 파일 모두 삭제 
```
$ git rm <filename>
```
2. 원격 저장소에 있는 파일만 삭제하고, 로컬 저장소의 파일은 삭제 x 
```
$ git rm --cached <filename>
```

### 파일/폴더 이름 변경 및 이동 
* oldname과 newname에 파일명 혹은 폴더명을 넣어 이름을 변경하거나 path를 넣어 이동 가능 
```
$ git mv <oldname> <newname>
```

---
### 프로젝트 생성부터 push까지

```sh
# 프로젝트 폴더 생성
$ mkdir new_project

# 프로젝트 폴더로 이동
$ cd new_project

# README 파일 & .gitignore 생성
$ touch README.md .gitignore

# gitignore.io 에 접속하여 필요한 내용 복-붙

# 폴더를 리포로 초기화
$ git init

# README & .gitignore 파일 add(tracking)
$ git add .

# commit
$ git commit -m 'first commit'

# github에서 원격 저장소 직접 생성

# 생성한 원격 저장소 등록  (origin 은 별명)
$ git remote add origin <URL>

# 등록된 저장소 확인
$ git remote -v

# 지금까지의 commit들 모아서 push
$ git push origin master
```
---

###  명령어 총정리

1. 리포 초기화 시점에 1회 입력

```sh
$ git init 
```

2. 작업 후 스테이징

```sh
# 특정 파일만 add 할 때
$ git add <filename>
# 현재 폴더 전체를 add 할 때
$ git add .
```

3. 커밋 진행

```sh
# 메시지는 짧고 정확하게
$ git commit -m 'MESSAGE'
```


4. 모니터링 명령어

```sh
# 현재 Working Dir 과 Stage 상황 확인 (주기적으로 확인하자!)
$ git status

# commit 로그 
$ git log     
# commit 로그 짧게
$ git log --oneline
```

5. github 에 원격 저장소 생성하기 (github site에서 `New Repository`)
  
6. 원격 저장소(remote repo) 추가하기

```sh
$ git remote add origin <URL>
```

7. 원격 저장소 확인하기

```sh
$ git remote -v
```

8. 원격 저장소에 지금까지의 commit 들 PUSH 하기

```sh
$ git push origin master
```

9. 새로운 컴퓨터에서 기존 원격 저장소 복제하기
```sh
$ git clone <URL>
```

10. 원격 저장소의 내용 받아오기
```sh
$ git pull origin master
```

|상황|명령어|
|--|--|
|집에서 새로운 프로젝트 시작|`$ mkdir project`|
|프로젝트 폴더로 이동|`$ cd project`|
|리포 초기화|`$ git init`|
|README, .gitignore 생성|`$ touch README.md .gitignore`|
|파일 스테이징|`$ git add .`|
|커밋|`$ git commit -m 'first commit'`|
|원격저장소 생성|github 사이트에서 진행|
|원격 저장소 등록|`$ git remote add origin <URL>`|
|원격 저장소 PUSH|`$ git push origin master`|
|다른 컴퓨터에서 원격저장소 복제|`$ git clone <URL>`|
|작업|`add`, `commit`|
|귀가 직전|`$ git push origin master`|
|집 도착 이후|`$ git pull origin master`|
|작업|`add`, `commit`|
|작업 종료|`$ git push origin master`|
|다른 컴퓨터에서 반복|`$ git pull origin master`|
