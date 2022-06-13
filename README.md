## 카카오맵 API를 활용한 시간 안내 웹 서비스 

----

### Description 

여행시 이동 경로의 시간을 알려주는게 있으면 효율적으로 계획을 세울 수 있을 것 같았다. 
돌아다니는 것을 좋아하는 나는 가보고 싶은 곳을 가려면 얼마나 시간이 걸리는지 궁금했다. 

과연 나는 오늘 원하는 곳을 다 갈 수 있을까? 

출발지, 경유지, 도착지 입력하면 경로와 걸리는 시간을 안내해준다. 

----
### 개발 내용 
Flask를 활용하여 웹 화면과 백엔드 설계

1. 사용자 등록 후 목적지를 검색 할 수 있게 했다.  
2. 검색어 입력 후 지도위에 마커가 표시된다.

**앞으로 구현될 기능**

1. 지도 위 목적지 라인으로 연결 
2. 사용자가 검색한 목적지 검색기록에 표시
3. 목적지 도착 시간 계산 
4. 시간이 안될 경우 다른 방문지 추천

-----
### stack 
- 언어 : Python
- Web framework : Flask 
- DB : MySQL 
- 배포 : Heroku 

-----
### Code 구성

```
< PROJECT ROOT >
   
.
└── flask_app/
    ├── db_model/                # DB 연결
    │   ├── mysql.py  
    │   └── monggodb.py
    │
    ├── map_control/             # DB에 데이터 삽입
    │   ├── session_mgmt.py      # 세션 관리 
    │   └── user_mgmt.py         # 사용자 정보 관리
    │
    ├── map_view/                # 라우팅 경로 정의 
    │   └── map.py
    │
    ├── static/                  # 부트스트랩 관련 파일
    │   ├── brand
    │   ├── dist
    │   └── blog.css
    │
    ├── templates/               # 템플릿 폴더
    │   ├── map_A.html           # 웹 화면
    │   └── map_B.html
    └── map_app.py               # flask 앱 실행 파일 

```

-----
### 서비스  
:point_right: [서비스 화면 바로가기](https://on-the-road.herokuapp.com/)

<img src = "https://user-images.githubusercontent.com/64198864/171449910-81459e78-2ea0-4238-a29a-3f990e77cff1.png" width="500" height="300" >


