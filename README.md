## 초기 세팅
###### 1. git clone or git pull
###### 2. 가상환경 생성하기
###### 3. local_settings.py 집어넣기 (manage.py와 같은 계층)
###### 4. pip install -r requirements.txt

## git flow
###### main
- 실제 운영에 반영되는 브랜치
###### dev
- 실제 배포에 적용되기 전 코드들을 테스트해보는 브랜치
###### feat
- 특정 기능을 개발하는 브랜치

## 작업 방식
###### 0. merge한 사람이 merge 했다고 하면 dev에서 pull 받아서 최신화 하기
###### 1. 한 기능에 대해 이슈 생성
###### 2. dev브랜치에서 feat/이슈번호 브랜치 생성
###### 3. 기능 개발 완료 후 ```[#이슈번호] 커밋 메시지 내용``` 형식으로 commit 및 pull & request 생성하기
###### 4. 팀장 코드 피드백 완료 후 본인이 merge 하기
