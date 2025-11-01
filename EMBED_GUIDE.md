# 🌐 임베딩 가이드

여러 플랫폼에서 앱을 임베딩하는 방법

---

## 📝 **노션 (Notion)**

### 방법 1: Embed 블록
```
1. 노션 페이지 열기
2. /embed 타이핑
3. Streamlit 앱 URL 입력
4. Enter!
```

### 방법 2: 전체 페이지
```
1. 새 페이지 생성
2. /full page 타이핑
3. Embed 선택
4. URL 입력
```

### 💡 팁
- 노션 데이터베이스에서도 사용 가능
- 페이지 폭: 기본 / 전체 폭 선택 가능

---

## 🏠 **우피사이트 (Woofy/Website)**

### 기본 iframe
```html
<div class="hairstyle-generator">
  <iframe 
    src="https://your-app.streamlit.app" 
    width="100%" 
    height="800px" 
    frameborder="0"
    style="border: none; border-radius: 10px;">
  </iframe>
</div>
```

### 반응형 iframe (모바일 최적화)
```html
<div style="
  position: relative; 
  padding-bottom: 75%; 
  height: 0; 
  overflow: hidden;
  max-width: 100%;
">
  <iframe 
    src="https://your-app.streamlit.app" 
    style="
      position: absolute; 
      top: 0; 
      left: 0; 
      width: 100%; 
      height: 100%; 
      border: none;
    "
    allow="camera; microphone; clipboard-write">
  </iframe>
</div>
```

### 전체 화면 버튼
```html
<div style="text-align: center; padding: 20px;">
  <a href="https://your-app.streamlit.app" 
     target="_blank" 
     style="text-decoration: none;">
    <button style="
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      border: none;
      padding: 15px 40px;
      font-size: 18px;
      border-radius: 8px;
      cursor: pointer;
      font-weight: bold;
      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
      transition: transform 0.2s;
    "
    onmouseover="this.style.transform='translateY(-2px)'"
    onmouseout="this.style.transform='translateY(0)'">
      💇 헤어스타일 생성기 열기
    </button>
  </a>
</div>
```

### 팝업 모달
```html
<button onclick="openGenerator()">헤어스타일 생성기</button>

<div id="generatorModal" style="
  display: none;
  position: fixed;
  z-index: 9999;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0,0,0,0.8);
">
  <div style="
    position: relative;
    margin: 2% auto;
    width: 90%;
    height: 90%;
    background: white;
    border-radius: 10px;
  ">
    <span onclick="closeGenerator()" style="
      position: absolute;
      right: 20px;
      top: 10px;
      font-size: 35px;
      cursor: pointer;
      z-index: 10000;
    ">&times;</span>
    
    <iframe 
      src="https://your-app.streamlit.app" 
      style="width: 100%; height: 100%; border: none; border-radius: 10px;">
    </iframe>
  </div>
</div>

<script>
function openGenerator() {
  document.getElementById('generatorModal').style.display = 'block';
}
function closeGenerator() {
  document.getElementById('generatorModal').style.display = 'none';
}
</script>
```

---

## 📱 **WordPress**

### Gutenberg 편집기
```
1. + 버튼 클릭
2. "Custom HTML" 블록 선택
3. iframe 코드 붙여넣기
```

### Classic 편집기
```
1. "텍스트" 탭 클릭
2. iframe 코드 붙여넣기
```

### 숏코드 (테마에 추가)
```php
// functions.php에 추가
function hairstyle_generator_shortcode() {
    return '<iframe src="https://your-app.streamlit.app" width="100%" height="800px" frameborder="0"></iframe>';
}
add_shortcode('hairstyle_generator', 'hairstyle_generator_shortcode');

// 사용: [hairstyle_generator]
```

---

## 🎨 **Wix**

```
1. + 버튼 → 내장 → HTML iframe
2. 코드 입력:
```
```html
<iframe src="https://your-app.streamlit.app" width="100%" height="800"></iframe>
```
```
3. 크기 조정 및 배치
```

---

## 🛒 **Shopify**

```
1. 온라인 스토어 → 페이지 → 페이지 추가
2. HTML 편집 모드 (<>)
3. iframe 코드 붙여넣기
```

---

## 📄 **Google Sites**

```
1. 삽입 → 임베드
2. URL 입력: https://your-app.streamlit.app
3. 삽입 클릭
```

---

## 💬 **Slack**

### 채널에 공유
```
/remind #channel 매일 9시 https://your-app.streamlit.app
```

### 앱 추가 (고급)
```
1. Slack App 생성
2. Slash Command 추가
3. Streamlit URL 연결
```

---

## 📧 **이메일 (HTML)**

```html
<a href="https://your-app.streamlit.app" 
   style="
     display: inline-block;
     background: #667eea;
     color: white;
     padding: 12px 30px;
     text-decoration: none;
     border-radius: 5px;
     font-weight: bold;
   ">
  헤어스타일 생성기 사용하기 →
</a>
```

---

## 🎯 **QR 코드 생성**

### 1. QR 코드 생성 사이트
- https://www.qr-code-generator.com
- Streamlit URL 입력
- 다운로드

### 2. 사용처
- 포스터
- 명함
- 전단지
- 매장 안내판

---

## 📱 **모바일 앱 (WebView)**

### React Native
```javascript
import { WebView } from 'react-native-webview';

<WebView 
  source={{ uri: 'https://your-app.streamlit.app' }}
  style={{ flex: 1 }}
/>
```

### Flutter
```dart
import 'package:webview_flutter/webview_flutter.dart';

WebView(
  initialUrl: 'https://your-app.streamlit.app',
  javascriptMode: JavascriptMode.unrestricted,
)
```

---

## 🔗 **단축 URL**

### Bitly
```
1. https://bitly.com
2. Streamlit URL 입력
3. 커스텀 URL 생성: bit.ly/hairstyle-gen
```

---

## 💡 **임베딩 최적화 팁**

### 1. 로딩 속도
```html
<!-- 지연 로딩 -->
<iframe 
  src="https://your-app.streamlit.app"
  loading="lazy">
</iframe>
```

### 2. 모바일 반응형
```css
@media (max-width: 768px) {
  iframe {
    height: 600px !important;
  }
}
```

### 3. 스크롤 제어
```html
<iframe 
  src="https://your-app.streamlit.app"
  scrolling="auto">
</iframe>
```

---

## ⚠️ **주의사항**

### CORS 에러 해결
이미 `.streamlit/config.toml`에 설정됨:
```toml
[server]
enableCORS = true
enableXsrfProtection = false
```

### iframe 차단 해결
일부 사이트는 iframe 차단:
- → 새 탭 열기 버튼 사용
- → 링크로 안내

---

## 🎨 **스타일 커스터마이징**

### 그림자 효과
```css
iframe {
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
  border-radius: 15px;
}
```

### 애니메이션
```css
iframe {
  transition: transform 0.3s;
}
iframe:hover {
  transform: scale(1.02);
}
```

---

## 📊 **Analytics 추가**

### Google Analytics
Streamlit Cloud 대시보드에서 자동 제공

### 커스텀 트래킹
```javascript
<script>
  // 사용자가 앱을 열 때
  gtag('event', 'hairstyle_generator_open', {
    'event_category': 'engagement',
    'event_label': 'generator_usage'
  });
</script>
```

---

## 🆘 **문제 해결**

### iframe이 표시되지 않음
1. URL 확인
2. CORS 설정 확인
3. 브라우저 콘솔 에러 확인

### 모바일에서 작동 안함
1. 반응형 iframe 코드 사용
2. viewport 메타 태그 확인

### 느린 로딩
1. 지연 로딩 사용
2. 버튼 클릭 시 로드

---

**선택한 플랫폼에 맞는 코드를 복사해서 사용하세요! 🚀**
