# StarDigital-YouthMall_Chatbot_and_Solution_Project
스타디지털육성프로그램 프로젝트 - 천안 청년몰의 공실 문제 해결 및 아이템 홍보를 위한 챗봇 및 솔루션

## 프로젝트 개요

이 프로젝트는 천안 청년몰의 공실 문제를 해결하고 아이템 홍보를 위한 챗봇 및 솔루션을 개발하는 것을 목표로 합니다. 

## 주요 기능

### 공실 문제 해결, 아이템 홍보
- 챗봇을 활용
- 천안 청년몰의 공실 정보, 모집 정보를 제공
- 청년상인분들의 상품을 홍보
- 관련 정보를 텍스트, 버튼, 이미지으로 제공 


### 솔루션
- 감성 분석 모델을 활용
- 링크를 통한 상품별 리뷰 크롤링
- 리뷰 긍부정도 분석
- 주요 키워드 분석
- 리뷰 트렌드 분석
- 리뷰 요약
- 시각정보

## 사용 기술 및 도구

- 언어: Python
- 웹 프론트엔드: HTML, CSS, JavaScript
- 프레임워크: Flask
- 데이터베이스: MySQL, AWS RDS
- 챗봇 기능: AWS Lex

## 챗봇 기능 커스텀 확장
- AWS Lex의 답변 제공 형태는 텍스트형으로 한계
- Lex 의도 및 응답 설정 부분은 수정의 어려움과 복잡함이 존재
- Lex의 응답 설정 부분을 넘버링형태로 부여
- 넘버링 정보를 DB의 key값과 연계하여 답변을 DB에서 제공
- DB 데이터 입력 및 수정은 엑셀파일 업로드 자동화 
- 버튼 기능을 통한 사용자의 챗봇 사용 플로우 유도

<br>
<br>
<br>

### 카피페이지 구성
![카피페이지](https://github.com/Kimdeokryun/StarDigital-YouthMall_Chatbot_and_Solution_Project/assets/96904134/f20494cc-10f0-46ba-8543-a3949f4fe6a6)
![카피페이지2](https://github.com/Kimdeokryun/StarDigital-YouthMall_Chatbot_and_Solution_Project/assets/96904134/992a2569-6032-4429-906c-b9e42357a48f)


### 챗봇 페이지
![챗봇페이지](https://github.com/Kimdeokryun/StarDigital-YouthMall_Chatbot_and_Solution_Project/assets/96904134/83495bc3-6535-434a-92f0-b7dd56ce1052)
![챗봇페이지2](https://github.com/Kimdeokryun/StarDigital-YouthMall_Chatbot_and_Solution_Project/assets/96904134/84e4da8e-306c-4533-8561-13790d132a51)
![챗봇페이지3](https://github.com/Kimdeokryun/StarDigital-YouthMall_Chatbot_and_Solution_Project/assets/96904134/b8717355-8aaa-4832-a39f-3c95b6faff27)


### 리뷰 분석 페이지
![리뷰 분석 페이지](https://github.com/Kimdeokryun/StarDigital-YouthMall_Chatbot_and_Solution_Project/assets/96904134/979a884b-71a1-4a34-b0e1-778f1a342bc9)
![리뷰 분석 페이지2](https://github.com/Kimdeokryun/StarDigital-YouthMall_Chatbot_and_Solution_Project/assets/96904134/25b024e3-7e13-477f-a5c7-f67ff6bbf42c)
![리뷰 분석 페이지3](https://github.com/Kimdeokryun/StarDigital-YouthMall_Chatbot_and_Solution_Project/assets/96904134/f3278fbf-dd20-4646-827a-48734a819eca)



### 챗봇 플로우 유도 간략도

![챗봇 플로우 유도](https://github.com/Kimdeokryun/StarDigital-YouthMall_Chatbot_and_Solution_Project/assets/96904134/7a9e40b2-d588-4763-ae92-a572dd2e2d93)

### DB 구성

![드림하이](https://github.com/Kimdeokryun/StarDigital-YouthMall_Chatbot_and_Solution_Project/assets/96904134/3b8ee398-5891-49d7-bfe4-817a2d735901)
