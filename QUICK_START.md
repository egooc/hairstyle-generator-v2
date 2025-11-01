# ⚡ 3분 안에 배포하기

## 🎯 초간단 배포 가이드

---

## 1️⃣ GitHub 저장소 만들기 (1분)

### 웹에서:
1. https://github.com/new
2. Repository name: `hairstyle-generator`
3. Public ✅
4. **Create repository** 클릭

---

## 2️⃣ 코드 업로드 (1분)

### 터미널에서:
```bash
# 프로젝트 폴더로 이동
cd /home/user

# Git 초기화
git init
git add .
git commit -m "Initial commit"

# GitHub 연결 (자신의 URL로 변경!)
git remote add origin https://github.com/YOUR_USERNAME/hairstyle-generator.git
git branch -M main
git push -u origin main
```

---

## 3️⃣ Streamlit Cloud 배포 (1분)

### 웹에서:
1. https://streamlit.io/cloud
2. **Sign in with GitHub**
3. **New app** 클릭
4. 다음 입력:
   ```
   Repository: YOUR_USERNAME/hairstyle-generator
   Branch: main
   Main file: hairstyle_generator_v2.py
   ```
5. **Deploy!** 클릭

---

## ✅ 완료!

약 2-3분 후:
```
✅ 배포 완료!
🌐 URL: https://your-app.streamlit.app
```

---

## 📱 노션에 임베딩

### 노션에서:
1. `/embed` 타이핑
2. Streamlit URL 붙여넣기
3. Enter!

---

## 🌐 웹사이트에 임베딩

```html
<iframe 
  src="https://your-app.streamlit.app" 
  width="100%" 
  height="800px">
</iframe>
```

---

## 🎉 끝!

이제 URL을 공유하세요!
