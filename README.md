# 💇 헤어스타일 모델 생성기

AI 기반 헤어스타일 모델 생성 및 편집 도구

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app.streamlit.app)

## 🌟 주요 기능

### 🤖 듀얼 AI 엔진 지원
- **Google AI Studio (Gemini 2.5 Flash Image)**
  - 무료 일일 100회 생성
  - 멀티 이미지 참조 (최대 3개)
  - 고품질 자연어 프롬프트 이해

- **Replicate (Seedream 4.0)**
  - 4K 해상도 지원
  - 초고속 생성 (10-20초)
  - 배치 생성 (1-4개 동시)
  - 업스케일링 기능

### 📸 이미지 생성
- 한국인 모델 전문
- 나이대, 성별, 헤어스타일 세부 설정
- 촬영 설정 커스터마이징 (앵글, 조명, 배경)

### ✂️ 이미지 편집 (헤어스타일 고정)
- **의상 변경**: 헤어스타일 유지하며 의상만 교체
- **얼굴 변경**: 헤어스타일 유지하며 얼굴만 교체
- **배경 변경**: 인물 고정, 배경만 교체
- **헤어 컬러 변경**: 헤어 스타일 유지, 컬러만 변경

### 🔧 고급 기능 (Replicate 전용)
- **4K 업스케일링**: 저해상도 → 4K
- **배치 생성**: 한 번에 여러 변형 생성
- **고해상도**: 2K ~ 4K 선택

---

## 🚀 빠른 시작

### 1. 온라인 사용 (추천)
👉 **[웹 앱 바로 사용하기](https://your-app.streamlit.app)**

### 2. 로컬 실행
```bash
# 저장소 클론
git clone https://github.com/YOUR_USERNAME/hairstyle-generator.git
cd hairstyle-generator

# 패키지 설치
pip install -r requirements_v2.txt

# 앱 실행
streamlit run hairstyle_generator_v2.py
```

---

## 🔑 API 키 발급

### Google AI Studio
1. https://aistudio.google.com 접속
2. "Get API key" 클릭
3. API 키 생성 및 복사

### Replicate
1. https://replicate.com 가입
2. Account → API tokens
3. 토큰 생성 및 복사

---

## 📖 사용 방법

### Step 1: 로그인
- AI 제공자 선택 (Google / Replicate)
- API 키 입력

### Step 2: 작업 선택
**Google 로그인 시:**
- 이미지 생성
- 의상/얼굴/배경/헤어 컬러 변경

**Replicate 로그인 시:**
- 이미지 생성 (2K/4K)
- 이미지 편집 → 4가지 하위 옵션
- 업스케일링

### Step 3: 이미지 생성/편집
- 옵션 선택 또는 이미지 업로드
- 생성 버튼 클릭
- 결과 확인 및 다운로드

---

## 💡 사용 팁

### 더 나은 결과를 위해
1. **샘플 이미지 2-3개 업로드**: 더 정확한 스타일 반영
2. **고품질 이미지 사용**: 선명한 결과물
3. **유사한 각도**: 자연스러운 합성

### 헤어스타일 일관성
- 메인 이미지의 헤어스타일이 정확히 보존됩니다
- 여러 번 수정해도 헤어스타일 유지
- 다양한 의상/배경 테스트 가능

---

## 🌐 웹사이트 임베딩

### 노션
```
/embed → Streamlit 앱 URL 입력
```

### HTML
```html
<iframe 
  src="https://your-app.streamlit.app" 
  width="100%" 
  height="800px" 
  frameborder="0">
</iframe>
```

자세한 내용: [배포 가이드](README_DEPLOY.md)

---

## 📊 기술 스택

- **Frontend**: Streamlit
- **AI Models**: 
  - Google Gemini 2.5 Flash Image
  - Bytedance Seedream 4.0
- **Image Processing**: Pillow
- **APIs**: 
  - google-generativeai
  - replicate

---

## 📁 프로젝트 구조

```
hairstyle-generator/
├── hairstyle_generator_v2.py  # 메인 애플리케이션
├── requirements_v2.txt         # Python 패키지
├── .streamlit/
│   └── config.toml            # Streamlit 설정
├── README.md                  # 프로젝트 설명
├── README_DEPLOY.md           # 배포 가이드
└── .gitignore                 # Git 제외 파일
```

---

## 🎯 활용 사례

- 💇 헤어살롱 포트폴리오 제작
- 🎨 헤어스타일 시뮬레이션
- 👔 가상 의상 피팅
- 🏞️ 프로필 사진 배경 교체
- 🌈 헤어 컬러 시뮬레이션

---

## 💰 비용

### Google AI Studio
- 무료: 일일 100회
- 유료: $0.002/image

### Replicate Seedream
- Text-to-Image: $0.02/image
- Image-to-Image: $0.02/image
- Upscaling: $0.015/image

---

## 🔒 보안

- API 키는 사용자 기기에만 저장
- 서버에 API 키 전송 안 함
- 모든 처리는 클라이언트 사이드

---

## 📝 라이센스

MIT License - 개인 및 상업적 용도 자유롭게 사용 가능

---

## 🤝 기여

이슈 제보 및 PR 환영합니다!

1. Fork the Project
2. Create your Feature Branch
3. Commit your Changes
4. Push to the Branch
5. Open a Pull Request

---

## 📧 문의

- GitHub Issues
- Email: your-email@example.com

---

## 🙏 감사

- Google AI Studio Team
- Replicate Team
- Streamlit Community

---

**Made with ❤️ for Hair Stylists**

[![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/hairstyle-generator?style=social)](https://github.com/YOUR_USERNAME/hairstyle-generator)
[![GitHub forks](https://img.shields.io/github/forks/YOUR_USERNAME/hairstyle-generator?style=social)](https://github.com/YOUR_USERNAME/hairstyle-generator/fork)
