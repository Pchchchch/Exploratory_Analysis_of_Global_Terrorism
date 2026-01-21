###[Cousera course] IBM: Data Science_capstone project using GTD data

# 🌍 Exploratory Analysis of Global Terrorism
# 🌍 글로벌 테러 발생에 대한 탐색적 분석

---

## 📌 프로젝트 개요  
## 📌 Project Overview

본 프로젝트는 Global Terrorism Database(GTD)를 활용하여 전 세계 테러 발생의
시간적 추세와 공간적 분포를 탐색적으로 분석하는 것을 목표로 한다.  
연도별 테러 발생 변화, 지역별 분포 특성, 공격 유형 및 표적 유형을 분석하고,
분석 결과를 시각화 및 인터랙티브 도구를 통해 직관적으로 전달하고자 하였다.

EDA, SQL 기반 집계 분석, 지도 시각화, 분류 모델, 그리고 대시보드를 포함한
데이터 분석의 전 과정을 단계적으로 수행하였다.

This project aims to explore temporal trends and spatial distributions of global terrorist incidents
using the Global Terrorism Database (GTD).  
It analyzes yearly trends, regional distributions, and incident characteristics,
and presents analytical results through visualizations and interactive tools.

The project follows an end-to-end data analysis workflow, including exploratory analysis,
SQL-based aggregation, geographic visualization, classification modeling,
and an interactive dashboard.

---

## 📊 주요 시각화 결과  
## 📊 Key Visualizations

아래 시각화는 본 프로젝트의 핵심 분석 결과를 요약하여 보여준다.

- 📈 연도별 테러 발생 추이  
- 🌍 지역별 테러 발생 분포  
- 🗺 전 세계 테러 발생 위치 지도 (Folium)  
- 🎛 지역 선택이 가능한 인터랙티브 대시보드 (Dash)

The following visualizations summarize the core analytical outcomes of the project,
including temporal trends, spatial patterns, and interactive exploration of terrorism data.

![Yearly Trend](assets/yearly_trend.png)  
![Region Distribution](assets/region_distribution.png)  
![Folium Map](assets/folium_map.png)  
![Dash Dashboard](assets/dash_dashboard.png)

---

## 🗂 데이터 설명  
## 🗂 Data Description

- 📚 데이터 출처: Global Terrorism Database (GTD)  
- 📅 분석 기간: 2000–2021  
- 🧾 분석 단위: 개별 테러 사건(Event-level data)

GTD는 전 세계 테러 사건에 대한 상세 정보를 제공하는 공개 데이터베이스로,
사건 발생 시점, 위치, 공격 유형, 표적 유형, 인명 피해 정보 등을 포함한다.

- 📚 Data source: Global Terrorism Database (GTD)  
- 📅 Time period: 2000–2021  
- 🧾 Unit of analysis: Individual terrorism incidents  

The GTD provides detailed information on terrorist events worldwide,
including temporal, geographic, and incident-level characteristics.

---

## 🛠 분석 방법  
## 🛠 Methodology

본 프로젝트에서는 다음과 같은 분석 방법을 적용하였다.

- 🔍 탐색적 데이터 분석(EDA)을 통한 기본 분포 및 추세 파악  
- 🗃 SQLite를 활용한 SQL 기반 집계 분석  
- 🗺 Folium을 이용한 테러 발생 위치 지도 시각화  
- 📉 로지스틱 회귀를 활용한 고위험 테러 사건 분류  
- 📊 Plotly Dash를 활용한 인터랙티브 대시보드 구현  

The following analytical methods were applied:

- 🔍 Exploratory Data Analysis (EDA) to identify basic patterns and trends  
- 🗃 SQL-based aggregation using SQLite  
- 🗺 Geographic visualization of incidents using Folium  
- 📉 Binary classification of high-risk incidents using Logistic Regression  
- 📊 Development of an interactive dashboard using Plotly Dash  

---

## 📁 프로젝트 구조  
## 📁 Project Structure

```text
├─ 01_GTD_EDA.ipynb              # 탐색적 데이터 분석
├─ 02_GTD_SQL.ipynb              # SQL 기반 집계 분석
├─ 03_GTD_Folium_Map.ipynb       # 지도 시각화
├─ 04_GTD_Classification.ipynb   # 고위험 사건 분류 모델
├─ 05_GTD_Dash.py                # 인터랙티브 대시보드
├─ assets/                       # 시각화 이미지
│   ├─ yearly_trend.png
│   ├─ region_distribution.png
│   ├─ folium_map.png
│   └─ dash_dashboard.png
└─ README.md

---

### 🔍 Key Insights 섹션 (구조화 버전)

```markdown
## 🔍 주요 인사이트  
## 🔍 Key Insights

### 🇰🇷 주요 분석 결과
1. 테러 발생은 특정 시기와 지역에 집중되는 경향을 보인다.  
2. 일부 지역은 장기간 높은 테러 발생 빈도를 지속적으로 유지한다.  
3. 공격 유형과 표적 유형은 인명 피해 규모와 통계적으로 연관성을 보인다.  

### 🇺🇸 Key Findings
1. Terrorist incidents are highly concentrated in specific regions and periods.  
2. Some regions consistently experience higher frequencies of attacks over time.  
3. Attack and target characteristics are associated with higher casualty risks.  
## 🚀 향후 확장 방향  
## 🚀 Future Work

### 🇰🇷 확장 가능성
향후 연구에서는 거버넌스 지표, 경제 변수, 사회적 불안정성 지표 등을 추가하여  
테러 발생의 구조적 요인을 보다 심층적으로 분석할 수 있다.  
또한, 보다 정교한 머신러닝 모델을 적용하여 예측 성능을 개선할 수 있다.

### 🇺🇸 Future Extensions
Future work may incorporate governance indicators, economic variables,  
and social instability measures to further investigate the structural drivers of terrorism.  
More advanced machine learning models could also be applied to improve predictive performance.

## ⚠️ 데이터 이용 안내  
## ⚠️ Data Availability

Global Terrorism Database(GTD) 원본 데이터는 라이선스 제한으로 인해  
본 저장소에 포함되어 있지 않다.

The raw Global Terrorism Database (GTD) data is not included in this repository  
due to licensing restrictions.

