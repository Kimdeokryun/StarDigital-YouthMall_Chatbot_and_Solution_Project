# StarDigital-YouthMall_Chatbot_and_Solution_Project
스타디지털육성프로그램 프로젝트 - 천안 청년몰의 공실 문제 해결 및 아이템 홍보를 위한 챗봇 및 솔루션

## 프로젝트 개요

천안 청년몰의 공실 안내와 아이템 홍보에 대한 문제점을 온라인 정보의 부재 및 천안 청년몰의 홍보를 위한 추가 인력 구성의 어려움으로 파악하였습니다. 
챗봇과의 채팅을 위한 페이지를 구성하고 기존 천안 청년몰의 홈페이지의 카피페이지에 연동하여 공실 정보 및 청년몰의 온라인 홍보를 통해 문제를 해결하고 기존 판매중인 상품의 리뷰 분석을 통해 상품 개선 및 확장의 판단에 어시스트를 위해 텍스트 기반 긍부정도 분석 AI를 통해 솔루션을 제공합니다.

## 개발 사항
Flask, MySQL, AWS Lex를 이용한 챗봇 기능 및 api 구현

AWS 서비스를 이용하여 서버, DB, 챗봇 구현

챗봇의 답변 형태의 제한을 극복하고자 정보의 삽입 및 수정의 용이성을 위한 DB 설계

아이템의 리뷰 분석을 위한 네이버 스마트 스토어 리뷰 크롤링

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


## 프로젝트 설명

### 프로세스
![image](https://github.com/Kimdeokryun/StarDigital-YouthMall_Chatbot_and_Solution_Project/assets/96904134/99b63d0b-d539-46b5-8e74-d1e4be765600)

### WBS
![image](https://github.com/Kimdeokryun/StarDigital-YouthMall_Chatbot_and_Solution_Project/assets/96904134/e75ca6d1-e944-4c94-a7ec-8b1de09def9b)

### ERD
![image](https://github.com/Kimdeokryun/StarDigital-YouthMall_Chatbot_and_Solution_Project/assets/96904134/592a1787-ce0d-41f7-ac03-e640a886b7ed)

### 챗봇 플로우 유도 간략도

![챗봇 플로우 유도](https://github.com/Kimdeokryun/StarDigital-YouthMall_Chatbot_and_Solution_Project/assets/96904134/7a9e40b2-d588-4763-ae92-a572dd2e2d93)

### 기존 홈페이지 카피 페이지 제작 및 연동
기존 홈페이지에 새로운 서비스를 연동하여 접근성을 높이고자 하였습니다.
![image](https://github.com/Kimdeokryun/StarDigital-YouthMall_Chatbot_and_Solution_Project/assets/96904134/4d215ac0-4fd5-49ac-bc37-8e84c1ca5cf1)

### 메인 챗봇 페이지
챗봇의 한정된 텍스트 기반 발화를 개선하고자 AWS Lex는 의도를 파악하기 위한 용도로 사용하고 DB를 구축하여, 버튼형, 이미지형 발화 기능도 추가하였습니다.
![image](https://github.com/Kimdeokryun/StarDigital-YouthMall_Chatbot_and_Solution_Project/assets/96904134/a59ffbb0-3b8f-4b4f-873c-3fe52809d27d)


### 리뷰 분석 대시보드 페이지
네이버 스마트 스토어, 아이디어스, 쿠팡의 쇼핑몰 주소 입력을 통해 리뷰를 크롤링하고 해당 리뷰를 분석하여 보여주는 예시 페이지 입니다.
![image](https://github.com/Kimdeokryun/StarDigital-YouthMall_Chatbot_and_Solution_Project/assets/96904134/623d246d-6819-4399-b20a-134e04affde6)
