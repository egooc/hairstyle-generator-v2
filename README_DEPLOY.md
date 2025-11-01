# 💇 헤어스타일 모델 생성기 - 배포 가이드

## 🚀 Streamlit Cloud 배포 (3분 완성)

---

## 📋 **준비물**
- ✅ GitHub 계정
- ✅ Streamlit Cloud 계정 (GitHub으로 로그인)
- ✅ 이 프로젝트 파일들

---

## 📂 **Step 1: GitHub 저장소 생성**

### 1-1. GitHub 새 저장소 만들기
1. https://github.com/new 접속
2. Repository name: `hairstyle-generator` (원하는 이름)
3. Public 선택
4. "Create repository" 클릭

### 1-2. 로컬에서 Git 초기화
```bash
cd /home/user

# Git 초기화
git init

# 파일 추가
git add hairstyle_generator_v2.py
git add requirements_v2.txt
git add README.md
git add .streamlit/

# 커밋
git commit -m "Initial commit: Dual API hairstyle generator"

# GitHub 연결 (자신의 저장소 URL로 변경)
git remote add origin https://github.com/YOUR_USERNAME/hairstyle-generator.git

# 푸시
git branch -M main
git push -u origin main
```

---

## 🌐 **Step 2: Streamlit Cloud 배포**

### 2-1. Streamlit Cloud 접속
1. https://streamlit.io/cloud 접속
2. "Sign in with GitHub" 클릭
3. GitHub 계정 연동

### 2-2. 새 앱 배포
1. **"New app"** 버튼 클릭
2. 다음 정보 입력:
   - **Repository**: `YOUR_USERNAME/hairstyle-generator`
   - **Branch**: `main`
   - **Main file path**: `hairstyle_generator_v2.py`
3. **"Deploy!"** 클릭

### 2-3. 배포 완료 대기
- 약 2-3분 소요
- 자동으로 패키지 설치 및 앱 실행
- 완료 시 URL 생성: `https://your-app.streamlit.app`

---

## 🔗 **Step 3: 노션에 임베딩**

### 3-1. Streamlit 앱 URL 복사
```
https://your-app-name.streamlit.app
```

### 3-2. 노션에서 임베딩
1. 노션 페이지 열기
2. `/embed` 타이핑
3. Streamlit 앱 URL 붙여넣기
4. Enter!

### 3-3. 전체 페이지로 만들기
```
/full page → Embed 선택 → URL 입력
```

---

## 🌍 **Step 4: 웹사이트에 임베딩**

### 4-1. 기본 iframe 코드
```html
<iframe 
  src="https://your-app-name.streamlit.app" 
  width="100%" 
  height="800px" 
  frameborder="0"
  style="border: none; border-radius: 10px;">
</iframe>
```

### 4-2. 반응형 iframe (추천)
```html
<div style="position: relative; padding-bottom: 75%; height: 0; overflow: hidden;">
  <iframe 
    src="https://your-app-name.streamlit.app" 
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;"
    allow="camera; microphone">
  </iframe>
</div>
```

### 4-3. 전체 화면 버튼
```html
<a href="https://your-app-name.streamlit.app" target="_blank" style="text-decoration: none;">
  <button style="
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    padding: 15px 30px;
    font-size: 18px;
    border-radius: 8px;
    cursor: pointer;
    font-weight: bold;
  ">
    💇 헤어스타일 생성기 열기
  </button>
</a>
```

---

## 🎨 **Step 5: 커스터마이징**

### 5-1. 커스텀 도메인 연결 (선택)
Streamlit Cloud 무료 플랜은 기본 도메인만 제공
- 유료 플랜: 커스텀 도메인 가능
- 또는: Cloudflare로 리디렉션 설정

### 5-2. 앱 설정 변경
Streamlit Cloud 대시보드에서:
1. 앱 선택
2. ⚙️ Settings 클릭
3. 다음 변경 가능:
   - 앱 이름
   - URL slug
   - 환경변수 (API 키 저장용)

---

## 🔐 **보안 설정 (중요)**

### API 키를 환경변수로 저장 (선택사항)

**Streamlit Cloud에서:**
1. 앱 Settings → Secrets
2. 다음 형식으로 저장:
```toml
# .streamlit/secrets.toml
GOOGLE_API_KEY = "your-google-api-key"
REPLICATE_API_TOKEN = "your-replicate-token"
```

**코드에서 사용:**
```python
import streamlit as st

# secrets에서 불러오기
default_google_key = st.secrets.get("GOOGLE_API_KEY", "")
default_replicate_key = st.secrets.get("REPLICATE_API_TOKEN", "")
```

---

## 📊 **배포 후 관리**

### 대시보드 확인
- **URL**: https://share.streamlit.io
- **Analytics**: 방문자 수, 사용량 확인
- **Logs**: 에러 로그 확인
- **Reboot**: 앱 재시작

### 코드 업데이트
```bash
# 코드 수정 후
git add .
git commit -m "Update feature"
git push

# Streamlit Cloud가 자동으로 재배포!
```

---

## 🎯 **최종 체크리스트**

- [ ] GitHub 저장소 생성
- [ ] 파일 푸시 완료
- [ ] Streamlit Cloud 배포 완료
- [ ] 앱 URL 확인: `https://_____.streamlit.app`
- [ ] 노션/웹사이트에 임베딩
- [ ] 모바일에서 테스트
- [ ] API 키 테스트 (Google & Replicate)

---

## 💡 **팁**

### 배포 속도 높이기
```toml
# .streamlit/config.toml
[server]
maxUploadSize = 10
```

### 캐싱으로 속도 향상
```python
@st.cache_data
def load_model():
    # 모델 로딩
    pass
```

### 에러 처리
- Logs에서 실시간 에러 확인
- 필요시 Reboot

---

## 🆘 **문제 해결**

### 1. "Module not found" 에러
→ `requirements_v2.txt`에 패키지 추가

### 2. 앱이 로드되지 않음
→ Streamlit Cloud 대시보드에서 Logs 확인

### 3. API 키 오류
→ 사용자가 직접 입력하는 방식이므로 문제없음

### 4. iframe이 표시되지 않음
→ 브라우저 CORS 정책 확인
→ `.streamlit/config.toml`에서 `enableCORS = true` 설정

---

## 📱 **모바일 최적화 확인**

1. 스마트폰으로 URL 접속
2. 세로/가로 모드 테스트
3. 이미지 업로드 테스트
4. 버튼 클릭 반응 확인

---

## 🎉 **완료!**

이제 다음 URL들을 공유하세요:
- **직접 접속**: `https://your-app.streamlit.app`
- **노션 임베딩**: 노션 페이지 URL
- **웹사이트**: 임베딩된 페이지 URL

---

## 📞 **지원**

문제 발생 시:
1. Streamlit Community: https://discuss.streamlit.io
2. GitHub Issues: 저장소에 이슈 등록
3. Streamlit Docs: https://docs.streamlit.io

---

**배포 성공을 기원합니다! 🚀**
