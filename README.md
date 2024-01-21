# CCSCD_v0.1
Court case search chatbot for Discord
법원 판례 검색 디스코드 챗봇

--------
## 데이터 출처 : AI-Hub
https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=580

## 사용 라이브러리 (설치할것)
 - discord.py
 - pandas
 - sentence_transformers
 - sklearn.metrics.pairwise
 - json

## 작동방법
 - pandas, SentenceTransformer, sklearn 패키지, json 라이브러리 설치
 - 디스코드 개발자 페이지에서 봇 토큰 생성 후 코드에 입력 후 코드 실행
 
## 작동원리
1981년 ~ 2021년까지의 민사, 행정, 형사 재판의 판례에서 기록되어 있는 사건의 내용과 사용자가 작성하는 사건의 자연어를 모두 벡터화 시키고 두 개의 벡터를 코사인 유사도 계산을 이용하여 5470개의 판례 중 코사인 유사도가 가장 높은 판례를 찾아 보내주는 원리입니다.
