## 카카오맵 API를 활용한 시간 안내 웹 서비스 

----

### Description 

여기저기 다 가보고 싶은 나. 하지만 시간은 한정되어 있다. 
돌아다니는 것을 좋아하는 나는 가보고 싶은 곳을 가려면 얼마나 시간이 걸리는지 궁금했다. 

과연 나는 오늘 원하는 곳을 다 갈 수 있을까? 

출발지, 경유지, 도착지 입력하면 경로와 걸리는 시간을 안내해준다. 

-----
### Code 구성

```
< PROJECT ROOT >
   
   |-- db_moodel             # DB 연결, 사용자 정보 저장
        |-- mysql.py
        |-- mongodb.py
   |-- map_control           # 세션 및 쿠키 관리
        |-- session_mgmt.py
        |-- user_mgmt.py
   |-- map_view              # 라우팅 경로 지정 
        map.py
   |-- static 
   |-- templates              # 웹 화면 구성
   |     |-- index.html
   |     |-- login.html
   |     |-- map.html  
   |     |-- map_in.html
   |-- map_app.py            # flask 실행파일 

```
----
### Tools 
- 언어 : Python
- Web framework : Flask 
- DB : MySQL
- 배포 : Heroku 

------
### 개발 내용 
Flask를 활용하여 MVC 패턴으로  화면구성과 백엔드 설계

1. 사용자 등록 후 목적지를 검색 할 수 있게 했다.  
2. 검색어 입력 후 지도위에 마커가 표시된다.

**앞으로 구현될 기능**

1. 지도 위 목적지 라인으로 연결 
2. 사용자가 검색한 목적지 검색기록에 표시
3. 목적지 도착 시간 계산 
4. 시간이 안될 경우 다른 방문지 추천

-----
### 서비스 화면 
<img src = "https://user-images.githubusercontent.com/64198864/169943147-409c812c-f7e5-48de-b8f8-6b0770026a2d.png" width="500" height="300" >

----
### 회고 
* 웹 서비스에 대한 이해
   - 서버와 클라이언트, API, http method, CRUD, 디자인패턴  
* 처음 프론트엔드를 구현하고 나서 백엔드와의 연결에서 문제가 있었다. 
   - 어떤 변수에 어떤 값을 넣어야 할지 생각했고 플라스크의 작동 원리를 찾아보고 어느정도 해결이 되었다. 
   - 이후 mysql에 사용자 정보(아이디, 비밀번호)를 넣는 데 많은 시간이 걸렸다. 

