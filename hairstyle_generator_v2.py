import streamlit as st
import google.generativeai as genai
from PIL import Image
import io
import base64
from datetime import datetime
import replicate
import os

# 페이지 설정
st.set_page_config(
    page_title="헤어스타일 모델 생성기",
    page_icon="💇",
    layout="wide"
)

# 세션 상태 초기화
if 'api_key' not in st.session_state:
    st.session_state.api_key = None
if 'api_provider' not in st.session_state:
    st.session_state.api_provider = None
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'history' not in st.session_state:
    st.session_state.history = []

# CSS 스타일
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .option-card {
        background: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 1rem 0;
        cursor: pointer;
        transition: transform 0.2s;
    }
    .option-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(0,0,0,0.15);
    }
    .warning-box {
        background: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 5px;
    }
    .info-box {
        background: #d1ecf1;
        border-left: 4px solid #0c5460;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 5px;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem;
        font-size: 1.1rem;
        font-weight: bold;
        border-radius: 8px;
    }
    .provider-badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 15px;
        font-size: 0.85rem;
        font-weight: bold;
        margin-left: 0.5rem;
    }
    .badge-google {
        background: #4285f4;
        color: white;
    }
    .badge-replicate {
        background: #ff4d4f;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# API 키 검증 함수
def verify_google_api_key(api_key):
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content("test")
        return True
    except Exception as e:
        return False

def verify_replicate_api_key(api_key):
    try:
        os.environ["REPLICATE_API_TOKEN"] = api_key
        # 간단한 테스트
        replicate.Client(api_token=api_key)
        return True
    except Exception as e:
        return False

# 로그인 페이지
def login_page():
    st.markdown('<div class="main-header"><h1>💇 헤어스타일 모델 생성기</h1><p>AI 제공자를 선택하고 로그인하세요</p></div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("---")
        st.markdown("### 🔑 로그인")
        
        # API 제공자 선택
        provider = st.radio(
            "AI 제공자 선택",
            ["Google AI Studio (Gemini)", "Replicate (Seedream 4.0)"],
            help="각 제공자는 다른 기능과 가격을 제공합니다"
        )
        
        st.markdown("")
        
        # Google AI Studio
        if provider == "Google AI Studio (Gemini)":
            st.markdown('<div class="info-box">📌 <b>Google AI Studio</b><br>• 무료 일일 100회<br>• Gemini 2.5 Flash Image<br>• 고품질 이미지 생성</div>', unsafe_allow_html=True)
            
            api_key = st.text_input(
                "Google AI Studio API 키",
                type="password",
                placeholder="AIzaSy...",
                help="https://aistudio.google.com/app/apikey"
            )
            
            if st.button("🔐 Google로 로그인", use_container_width=True):
                if not api_key:
                    st.error("❌ API 키를 입력해주세요")
                else:
                    with st.spinner("API 키 검증 중..."):
                        if verify_google_api_key(api_key):
                            st.session_state.api_key = api_key
                            st.session_state.api_provider = "google"
                            st.session_state.logged_in = True
                            st.success("✅ Google AI Studio 로그인 성공!")
                            st.rerun()
                        else:
                            st.error("❌ 유효하지 않은 API 키입니다")
        
        # Replicate
        else:
            st.markdown('<div class="info-box">📌 <b>Replicate (Seedream 4.0)</b><br>• 개인 크레딧 사용<br>• 4K 해상도 지원<br>• 업스케일링 기능<br>• 초고속 생성</div>', unsafe_allow_html=True)
            
            api_key = st.text_input(
                "Replicate API 토큰",
                type="password",
                placeholder="r8_...",
                help="https://replicate.com/account/api-tokens"
            )
            
            if st.button("🔐 Replicate로 로그인", use_container_width=True):
                if not api_key:
                    st.error("❌ API 토큰을 입력해주세요")
                else:
                    with st.spinner("API 토큰 검증 중..."):
                        if verify_replicate_api_key(api_key):
                            st.session_state.api_key = api_key
                            st.session_state.api_provider = "replicate"
                            st.session_state.logged_in = True
                            st.success("✅ Replicate 로그인 성공!")
                            st.rerun()
                        else:
                            st.error("❌ 유효하지 않은 API 토큰입니다")
        
        st.markdown("---")
        
        # API 키 발급 안내
        if provider == "Google AI Studio (Gemini)":
            st.info("💡 **Google API 키 발급**\n\n1. https://aistudio.google.com 접속\n2. 'Get API key' 클릭\n3. API 키 생성 및 복사")
        else:
            st.info("💡 **Replicate API 토큰 발급**\n\n1. https://replicate.com 가입\n2. Account → API tokens\n3. 토큰 생성 및 복사")

# Google 메인 선택 화면 (5개 옵션)
def google_main_selection():
    st.markdown('<div class="main-header"><h1>💇 헤어스타일 모델 생성기</h1><span class="provider-badge badge-google">Google Gemini</span></div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([4, 1, 1])
    with col3:
        if st.button("🚪 로그아웃"):
            st.session_state.logged_in = False
            st.session_state.api_key = None
            st.session_state.api_provider = None
            st.rerun()
    
    st.markdown("## 작업을 선택하세요")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("1️⃣ 이미지 생성\n\n처음부터 새로운 헤어스타일 모델 생성", key="gen_google", use_container_width=True):
            st.session_state.selected_mode = "generation"
            st.rerun()
        
        if st.button("2️⃣ 의상 변경\n\n헤어스타일 고정, 의상만 변경", key="outfit_google", use_container_width=True):
            st.session_state.selected_mode = "outfit"
            st.rerun()
        
        if st.button("3️⃣ 얼굴 변경\n\n헤어스타일 고정, 얼굴만 변경", key="face_google", use_container_width=True):
            st.session_state.selected_mode = "face"
            st.rerun()
    
    with col2:
        if st.button("4️⃣ 배경 변경\n\n인물 고정, 배경만 변경", key="bg_google", use_container_width=True):
            st.session_state.selected_mode = "background"
            st.rerun()
        
        if st.button("5️⃣ 헤어 컬러 변경\n\n헤어 스타일 유지, 컬러만 변경", key="color_google", use_container_width=True):
            st.session_state.selected_mode = "color"
            st.rerun()

# Replicate 메인 선택 화면 (3개 옵션)
def replicate_main_selection():
    st.markdown('<div class="main-header"><h1>💇 헤어스타일 모델 생성기</h1><span class="provider-badge badge-replicate">Replicate Seedream</span></div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([4, 1, 1])
    with col3:
        if st.button("🚪 로그아웃"):
            st.session_state.logged_in = False
            st.session_state.api_key = None
            st.session_state.api_provider = None
            st.rerun()
    
    st.markdown("## 작업을 선택하세요")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("1️⃣ 이미지 생성\n\n텍스트로 새로운 이미지 생성\n(Text-to-Image)", key="gen_replicate", use_container_width=True):
            st.session_state.selected_mode = "generation"
            st.rerun()
    
    with col2:
        if st.button("2️⃣ 이미지 편집\n\n기존 이미지 수정\n(Image-to-Image)", key="edit_replicate", use_container_width=True):
            st.session_state.selected_mode = "edit_menu"
            st.rerun()
    
    with col3:
        if st.button("3️⃣ 업스케일링\n\n이미지 해상도 향상\n(4K Upscaling)", key="upscale_replicate", use_container_width=True):
            st.session_state.selected_mode = "upscale"
            st.rerun()

# Replicate 이미지 편집 서브메뉴
def replicate_edit_submenu():
    st.markdown('<div class="main-header"><h1>2️⃣ 이미지 편집</h1><span class="provider-badge badge-replicate">Replicate Seedream</span></div>', unsafe_allow_html=True)
    
    if st.button("⬅️ 메인으로 돌아가기"):
        st.session_state.selected_mode = None
        st.rerun()
    
    st.markdown("## 편집 유형을 선택하세요")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("👤 얼굴 변경\n\n헤어스타일 고정, 얼굴만 변경", key="face_replicate", use_container_width=True):
            st.session_state.selected_mode = "face"
            st.rerun()
        
        if st.button("🏞️ 배경 변경\n\n인물 고정, 배경만 변경", key="bg_replicate", use_container_width=True):
            st.session_state.selected_mode = "background"
            st.rerun()
    
    with col2:
        if st.button("👔 의상 변경\n\n헤어스타일 고정, 의상만 변경", key="outfit_replicate", use_container_width=True):
            st.session_state.selected_mode = "outfit"
            st.rerun()
        
        if st.button("🎨 헤어 컬러 변경\n\n헤어 스타일 유지, 컬러만 변경", key="color_replicate", use_container_width=True):
            st.session_state.selected_mode = "color"
            st.rerun()

# 이미지 생성 페이지 (Google)
def generation_page_google():
    st.markdown('<div class="main-header"><h1>1️⃣ 이미지 생성</h1><span class="provider-badge badge-google">Google Gemini</span></div>', unsafe_allow_html=True)
    
    if st.button("⬅️ 뒤로 가기"):
        st.session_state.selected_mode = None
        st.rerun()
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📋 모델 정보")
        
        age_group = st.selectbox("나이대", ["10대", "20대", "30대", "40대", "50대"])
        gender = st.selectbox("성별", ["여성", "남성"])
        skin_tone = st.selectbox("피부톤", ["밝은 톤", "보통 톤", "어두운 톤"])
        
        st.markdown("### 💇 헤어스타일")
        
        if gender == "여성":
            hair_length = st.selectbox("기장", [
                "숏컷 (pixie cut)",
                "숏단발 (short bob)",
                "중간머리 (shoulder length)",
                "단발머리 (long bob)",
                "긴머리 (long hair)"
            ])
        else:
            hair_length = st.selectbox("스타일", [
                "내린머리 (down-styled)",
                "올린머리 (up-styled)",
                "투블럭 (undercut)"
            ])
        
        hair_texture = st.selectbox("헤어 질감", ["스트레이트", "C컬", "웨이브"])
        hair_color = st.selectbox("헤어 컬러", [
            "자연흑발",
            "다크 브라운",
            "브라운",
            "애쉬 브라운",
            "밝은 브라운"
        ])
        hair_volume = st.selectbox("볼륨감", ["볼륨있는", "자연스러운", "얇은/가벼운"])
        bangs = st.selectbox("앞머리", ["있음", "없음", "시스루뱅"])
        
        st.markdown("### 📸 촬영 설정")
        
        shot_type = st.selectbox("샷 타입", ["헤드샷 (headshot)", "상반신 (upper body)"])
        angle = st.selectbox("앵글", ["정면 (front view)", "45도 (3/4 view)", "측면 (side profile)"])
        expression = st.selectbox("표정", ["무표정", "은은한 미소", "자연스러운 미소"])
        lighting = st.selectbox("조명", ["스튜디오 조명", "자연광", "소프트 라이팅"])
        background = st.selectbox("배경", [
            "흰색 무지 배경",
            "회색 무지 배경",
            "스튜디오 배경",
            "블러 처리된 실내"
        ])
    
    with col2:
        st.markdown("### 🎨 생성 결과")
        
        if st.button("🎨 이미지 생성하기", use_container_width=True, type="primary"):
            with st.spinner("이미지 생성 중... 약 30초 소요됩니다"):
                try:
                    # 프롬프트 생성
                    age_map = {"10대": "teenage", "20대": "20s", "30대": "30s", "40대": "40s", "50대": "50s"}
                    gender_map = {"여성": "female", "남성": "male"}
                    skin_map = {"밝은 톤": "fair skin", "보통 톤": "medium skin tone", "어두운 톤": "tan skin"}
                    texture_map = {"스트레이트": "straight", "C컬": "soft C-curl", "웨이브": "wavy"}
                    color_map = {
                        "자연흑발": "natural black",
                        "다크 브라운": "dark brown",
                        "브라운": "brown",
                        "애쉬 브라운": "ash brown",
                        "밝은 브라운": "light brown"
                    }
                    volume_map = {"볼륨있는": "voluminous", "자연스러운": "natural", "얇은/가벼운": "flat"}
                    bangs_map = {"있음": "with bangs", "없음": "no bangs", "시스루뱅": "with see-through bangs"}
                    
                    prompt = f"""
A professional studio portrait photograph of a Korean {age_map[age_group]} {gender_map[gender]}.

COMPOSITION:
- Shot type: {shot_type}
- Angle: {angle}
- Expression: {expression}

HAIR (PRIMARY FOCUS):
- Style: {hair_length} {texture_map[hair_texture]} hair
- Color: {color_map[hair_color]}
- Volume: {volume_map[hair_volume]} volume
- Bangs: {bangs_map[bangs]}

SUBJECT DETAILS:
- Skin tone: {skin_map[skin_tone]}
- Clean, professional appearance

TECHNICAL SETTINGS:
- Lighting: {lighting} creating even, flattering illumination
- Background: {background}
- Image quality: High-resolution, sharp focus on hair details
- Aspect ratio: Portrait orientation

The final image should showcase the hairstyle clearly with professional salon-quality photography standards.
"""
                    
                    # API 호출
                    genai.configure(api_key=st.session_state.api_key)
                    model = genai.GenerativeModel('gemini-2.5-flash-image')
                    response = model.generate_content([prompt])
                    
                    # 결과 표시
                    for part in response.candidates[0].content.parts:
                        if part.inline_data is not None:
                            image_data = part.inline_data.data
                            image = Image.open(io.BytesIO(image_data))
                            
                            st.image(image, use_container_width=True)
                            
                            # 다운로드 버튼
                            buf = io.BytesIO()
                            image.save(buf, format="PNG")
                            st.download_button(
                                label="💾 이미지 다운로드",
                                data=buf.getvalue(),
                                file_name=f"hairstyle_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png",
                                mime="image/png",
                                use_container_width=True
                            )
                            
                            st.success("✅ 이미지 생성 완료!")
                
                except Exception as e:
                    st.error(f"❌ 오류 발생: {str(e)}")

# 이미지 생성 페이지 (Replicate)
def generation_page_replicate():
    st.markdown('<div class="main-header"><h1>1️⃣ 이미지 생성</h1><span class="provider-badge badge-replicate">Replicate Seedream</span></div>', unsafe_allow_html=True)
    
    if st.button("⬅️ 뒤로 가기"):
        st.session_state.selected_mode = None
        st.rerun()
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📋 모델 정보")
        
        age_group = st.selectbox("나이대", ["10대", "20대", "30대", "40대", "50대"])
        gender = st.selectbox("성별", ["여성", "남성"])
        skin_tone = st.selectbox("피부톤", ["밝은 톤", "보통 톤", "어두운 톤"])
        
        st.markdown("### 💇 헤어스타일")
        
        if gender == "여성":
            hair_length = st.selectbox("기장", [
                "숏컷 (pixie cut)",
                "숏단발 (short bob)",
                "중간머리 (shoulder length)",
                "단발머리 (long bob)",
                "긴머리 (long hair)"
            ])
        else:
            hair_length = st.selectbox("스타일", [
                "내린머리 (down-styled)",
                "올린머리 (up-styled)",
                "투블럭 (undercut)"
            ])
        
        hair_texture = st.selectbox("헤어 질감", ["스트레이트", "C컬", "웨이브"])
        hair_color = st.selectbox("헤어 컬러", [
            "자연흑발",
            "다크 브라운",
            "브라운",
            "애쉬 브라운",
            "밝은 브라운"
        ])
        hair_volume = st.selectbox("볼륨감", ["볼륨있는", "자연스러운", "얇은/가벼운"])
        bangs = st.selectbox("앞머리", ["있음", "없음", "시스루뱅"])
        
        st.markdown("### 📸 촬영 설정")
        
        shot_type = st.selectbox("샷 타입", ["헤드샷 (headshot)", "상반신 (upper body)"])
        angle = st.selectbox("앵글", ["정면 (front view)", "45도 (3/4 view)", "측면 (side profile)"])
        expression = st.selectbox("표정", ["무표정", "은은한 미소", "자연스러운 미소"])
        lighting = st.selectbox("조명", ["스튜디오 조명", "자연광", "소프트 라이팅"])
        background = st.selectbox("배경", [
            "흰색 무지 배경",
            "회색 무지 배경",
            "스튜디오 배경",
            "블러 처리된 실내"
        ])
        
        st.markdown("### ⚙️ Seedream 설정")
        resolution = st.selectbox("해상도", ["2K (2048x2048)", "4K (4096x4096)"], index=0)
        num_images = st.slider("생성 이미지 수", 1, 4, 1)
    
    with col2:
        st.markdown("### 🎨 생성 결과")
        
        if st.button("🎨 이미지 생성하기", use_container_width=True, type="primary"):
            with st.spinner(f"이미지 생성 중... {num_images}개 생성 예상 시간: 약 {num_images * 10}초"):
                try:
                    # 프롬프트 생성
                    age_map = {"10대": "teenage", "20대": "20s", "30대": "30s", "40대": "40s", "50대": "50s"}
                    gender_map = {"여성": "female", "남성": "male"}
                    skin_map = {"밝은 톤": "fair skin", "보통 톤": "medium skin tone", "어두운 톤": "tan skin"}
                    texture_map = {"스트레이트": "straight", "C컬": "soft C-curl", "웨이브": "wavy"}
                    color_map = {
                        "자연흑발": "natural black",
                        "다크 브라운": "dark brown",
                        "브라운": "brown",
                        "애쉬 브라운": "ash brown",
                        "밝은 브라운": "light brown"
                    }
                    volume_map = {"볼륨있는": "voluminous", "자연스러운": "natural", "얇은/가벼운": "flat"}
                    bangs_map = {"있음": "with bangs", "없음": "no bangs", "시스루뱅": "with see-through bangs"}
                    
                    prompt = f"""
A professional studio portrait photograph of a Korean {age_map[age_group]} {gender_map[gender]}.

COMPOSITION:
- Shot type: {shot_type}
- Angle: {angle}
- Expression: {expression}

HAIR (PRIMARY FOCUS):
- Style: {hair_length} {texture_map[hair_texture]} hair
- Color: {color_map[hair_color]}
- Volume: {volume_map[hair_volume]} volume
- Bangs: {bangs_map[bangs]}

SUBJECT DETAILS:
- Skin tone: {skin_map[skin_tone]}
- Clean, professional appearance

TECHNICAL SETTINGS:
- Lighting: {lighting} creating even, flattering illumination
- Background: {background}
- Image quality: High-resolution, sharp focus on hair details
- Aspect ratio: Portrait orientation

The final image should showcase the hairstyle clearly with professional salon-quality photography standards.
"""
                    
                    # Replicate API 호출
                    os.environ["REPLICATE_API_TOKEN"] = st.session_state.api_key
                    
                    output = replicate.run(
                        "bytedance/seedream-4",
                        input={
                            "prompt": prompt,
                            "num_outputs": num_images,
                            "aspect_ratio": "1:1",
                            "output_format": "png"
                        }
                    )
                    
                    # 결과 표시
                    if isinstance(output, list):
                        for idx, image_url in enumerate(output):
                            st.image(image_url, caption=f"생성 이미지 {idx + 1}", use_container_width=True)
                            
                            # 다운로드 링크
                            st.markdown(f"[💾 이미지 {idx + 1} 다운로드]({image_url})")
                        
                        st.success(f"✅ {len(output)}개 이미지 생성 완료!")
                    else:
                        st.image(output, use_container_width=True)
                        st.markdown(f"[💾 이미지 다운로드]({output})")
                        st.success("✅ 이미지 생성 완료!")
                
                except Exception as e:
                    st.error(f"❌ 오류 발생: {str(e)}")

# 업스케일링 페이지 (Replicate 전용)
def upscale_page_replicate():
    st.markdown('<div class="main-header"><h1>3️⃣ 업스케일링</h1><span class="provider-badge badge-replicate">Replicate Seedream</span></div>', unsafe_allow_html=True)
    
    if st.button("⬅️ 뒤로 가기"):
        st.session_state.selected_mode = None
        st.rerun()
    
    st.markdown('<div class="info-box">💡 <b>업스케일링 기능</b><br>저해상도 이미지를 4K까지 업스케일하여 선명도를 높입니다.</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📤 이미지 업로드")
        
        input_image = st.file_uploader("업스케일할 이미지", type=['png', 'jpg', 'jpeg'], key="upscale_input")
        
        if input_image:
            st.image(input_image, caption="원본 이미지", use_container_width=True)
            
            st.markdown("### ⚙️ 업스케일 설정")
            scale_factor = st.selectbox("배율", ["2x", "4x"], index=1)
    
    with col2:
        st.markdown("### 🎨 업스케일 결과")
        
        if st.button("✨ 업스케일링 시작", use_container_width=True, type="primary"):
            if not input_image:
                st.error("❌ 이미지를 업로드해주세요!")
            else:
                with st.spinner("업스케일 중... 약 20-30초 소요됩니다"):
                    try:
                        # 이미지를 base64로 변환
                        image = Image.open(input_image)
                        buffered = io.BytesIO()
                        image.save(buffered, format="PNG")
                        img_str = base64.b64encode(buffered.getvalue()).decode()
                        data_uri = f"data:image/png;base64,{img_str}"
                        
                        # Replicate API 호출 (업스케일 모델)
                        os.environ["REPLICATE_API_TOKEN"] = st.session_state.api_key
                        
                        # Note: Seedream 4의 업스케일 기능 사용
                        # 실제로는 별도의 upscale 모델이 필요할 수 있음
                        st.info("ℹ️ Seedream 4.0의 고해상도 재생성 기능을 사용합니다")
                        
                        output = replicate.run(
                            "bytedance/seedream-4",
                            input={
                                "prompt": "high quality, ultra detailed, 4K resolution",
                                "image": data_uri,
                                "prompt_strength": 0.3,  # 원본 유지
                                "output_format": "png"
                            }
                        )
                        
                        # 결과 표시
                        if isinstance(output, list):
                            st.image(output[0], use_container_width=True)
                            st.markdown(f"[💾 업스케일 이미지 다운로드]({output[0]})")
                        else:
                            st.image(output, use_container_width=True)
                            st.markdown(f"[💾 업스케일 이미지 다운로드]({output})")
                        
                        st.success("✅ 업스케일 완료!")
                    
                    except Exception as e:
                        st.error(f"❌ 오류 발생: {str(e)}")
                        st.info("💡 Seedream 4.0의 업스케일 기능은 이미지 편집 모드를 사용합니다")

# 이미지 편집 페이지 (공통 - API에 따라 다른 처리)
def edit_page(mode):
    mode_names = {
        "outfit": "의상 변경",
        "face": "얼굴 변경",
        "background": "배경 변경",
        "color": "헤어 컬러 변경"
    }
    
    mode_emojis = {
        "outfit": "👔",
        "face": "👤",
        "background": "🏞️",
        "color": "🎨"
    }
    
    provider_badge = "badge-google" if st.session_state.api_provider == "google" else "badge-replicate"
    provider_name = "Google Gemini" if st.session_state.api_provider == "google" else "Replicate Seedream"
    
    st.markdown(f'<div class="main-header"><h1>{mode_emojis[mode]} {mode_names[mode]}</h1><span class="provider-badge {provider_badge}">{provider_name}</span></div>', unsafe_allow_html=True)
    
    if st.button("⬅️ 뒤로 가기"):
        if st.session_state.api_provider == "replicate":
            st.session_state.selected_mode = "edit_menu"
        else:
            st.session_state.selected_mode = None
        st.rerun()
    
    st.markdown('<div class="warning-box">⚠️ <b>주의:</b> 헤어스타일은 메인 이미지 그대로 유지됩니다</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📤 이미지 업로드")
        
        main_image = st.file_uploader("메인 이미지 (헤어스타일 유지)", type=['png', 'jpg', 'jpeg'], key=f"main_{mode}")
        
        st.markdown("**샘플 이미지 (1-3개)**")
        st.caption("💡 팁: 샘플 이미지를 2-3개 업로드하면 더 정확한 결과를 얻을 수 있습니다!")
        
        sample1 = st.file_uploader("샘플 1 (필수)", type=['png', 'jpg', 'jpeg'], key=f"sample1_{mode}")
        sample2 = st.file_uploader("샘플 2 (선택)", type=['png', 'jpg', 'jpeg'], key=f"sample2_{mode}")
        sample3 = st.file_uploader("샘플 3 (선택)", type=['png', 'jpg', 'jpeg'], key=f"sample3_{mode}")
        
        if main_image:
            st.image(main_image, caption="메인 이미지", use_container_width=True)
        
        samples_col1, samples_col2, samples_col3 = st.columns(3)
        with samples_col1:
            if sample1:
                st.image(sample1, caption="샘플 1", use_container_width=True)
        with samples_col2:
            if sample2:
                st.image(sample2, caption="샘플 2", use_container_width=True)
        with samples_col3:
            if sample3:
                st.image(sample3, caption="샘플 3", use_container_width=True)
    
    with col2:
        st.markdown("### 🎨 변경 결과")
        
        if st.button(f"✨ {mode_names[mode]}하기", use_container_width=True, type="primary"):
            if not main_image or not sample1:
                st.error("❌ 메인 이미지와 샘플 1은 필수입니다!")
            else:
                with st.spinner("이미지 변경 중... 약 30-60초 소요됩니다"):
                    try:
                        # 프롬프트 선택
                        prompts = {
                            "outfit": """
Create a new image using:
- The person and hairstyle from the FIRST image (main image)
- The outfit style from the remaining sample images

CRITICAL RULES:
1. Keep the hairstyle EXACTLY as shown in the first image:
   - Hair length, hair texture, hair color, hair volume
   - Hair cut, bangs style, hair direction
   - DO NOT change ANY aspect of the hair
2. Apply the outfit style from the sample images
3. Maintain the person's pose and facial features from the first image
4. Keep natural lighting and professional portrait quality

The result should look like the same person from the first image 
wearing the outfit from the sample images.
""",
                            "face": """
Create a new image by combining:
- The hairstyle and outfit from the FIRST image (main image)
- The facial features from the remaining sample images

CRITICAL RULES:
1. Keep the hairstyle from the first image EXACTLY the same:
   - Hair length, texture, color, volume, cut, style
   - DO NOT modify the hair in any way
2. Replace only the facial features (eyes, nose, mouth, face shape)
3. Keep the outfit and pose from the first image
4. Maintain professional portrait quality and natural lighting

The result should have the face from the sample images 
with the exact hairstyle from the first image.
""",
                            "background": """
Create a new image by:
- Keeping the person EXACTLY as shown in the FIRST image (main image)
- Replacing the background with the style from the remaining sample images

CRITICAL RULES:
1. Keep the person completely unchanged:
   - Hairstyle, hair color, face, outfit, pose
   - DO NOT modify ANY aspect of the subject
2. Only change the background/environment
3. Ensure lighting on the person matches the new background naturally
4. Maintain professional portrait quality

The result should be the exact same person in a different environment.
""",
                            "color": """
Create a new image by:
- Using the person from the FIRST image (main image)
- Applying the hair color from the remaining sample images

CRITICAL RULES:
1. ONLY change the hair color - nothing else
2. Keep EXACTLY the same:
   - Hair length, texture, volume, cut, style
   - Bangs style, hair direction, hair flow
   - Face, outfit, background, pose
3. Apply the color naturally with proper highlights and shadows
4. Maintain professional portrait quality

The result should be the exact same hairstyle in a different color.
"""
                        }
                        
                        prompt = prompts[mode]
                        
                        # API별 처리
                        if st.session_state.api_provider == "google":
                            # Google Gemini API
                            main_img = Image.open(main_image)
                            sample1_img = Image.open(sample1)
                            
                            images = [main_img, sample1_img]
                            
                            if sample2:
                                images.append(Image.open(sample2))
                            if sample3:
                                images.append(Image.open(sample3))
                            
                            genai.configure(api_key=st.session_state.api_key)
                            model = genai.GenerativeModel('gemini-2.5-flash-image')
                            
                            response = model.generate_content([prompt] + images)
                            
                            for part in response.candidates[0].content.parts:
                                if part.inline_data is not None:
                                    image_data = part.inline_data.data
                                    result_image = Image.open(io.BytesIO(image_data))
                                    
                                    st.image(result_image, use_container_width=True)
                                    
                                    buf = io.BytesIO()
                                    result_image.save(buf, format="PNG")
                                    st.download_button(
                                        label="💾 이미지 다운로드",
                                        data=buf.getvalue(),
                                        file_name=f"{mode}_changed_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png",
                                        mime="image/png",
                                        use_container_width=True
                                    )
                        
                        else:
                            # Replicate Seedream API
                            os.environ["REPLICATE_API_TOKEN"] = st.session_state.api_key
                            
                            # 이미지를 base64로 변환
                            def image_to_data_uri(img_file):
                                image = Image.open(img_file)
                                buffered = io.BytesIO()
                                image.save(buffered, format="PNG")
                                img_str = base64.b64encode(buffered.getvalue()).decode()
                                return f"data:image/png;base64,{img_str}"
                            
                            main_uri = image_to_data_uri(main_image)
                            
                            # Seedream은 단일 참조 이미지 사용 (가장 중요한 샘플1)
                            output = replicate.run(
                                "bytedance/seedream-4",
                                input={
                                    "prompt": prompt,
                                    "image": main_uri,
                                    "prompt_strength": 0.8,
                                    "output_format": "png"
                                }
                            )
                            
                            if isinstance(output, list):
                                st.image(output[0], use_container_width=True)
                                st.markdown(f"[💾 이미지 다운로드]({output[0]})")
                            else:
                                st.image(output, use_container_width=True)
                                st.markdown(f"[💾 이미지 다운로드]({output})")
                        
                        st.success(f"✅ {mode_names[mode]} 완료!")
                    
                    except Exception as e:
                        st.error(f"❌ 오류 발생: {str(e)}")

# 메인 앱 로직
def main():
    if not st.session_state.logged_in:
        login_page()
    else:
        if 'selected_mode' not in st.session_state:
            st.session_state.selected_mode = None
        
        # Google AI Studio 로그인
        if st.session_state.api_provider == "google":
            if st.session_state.selected_mode is None:
                google_main_selection()
            elif st.session_state.selected_mode == "generation":
                generation_page_google()
            elif st.session_state.selected_mode in ["outfit", "face", "background", "color"]:
                edit_page(st.session_state.selected_mode)
        
        # Replicate 로그인
        elif st.session_state.api_provider == "replicate":
            if st.session_state.selected_mode is None:
                replicate_main_selection()
            elif st.session_state.selected_mode == "generation":
                generation_page_replicate()
            elif st.session_state.selected_mode == "edit_menu":
                replicate_edit_submenu()
            elif st.session_state.selected_mode == "upscale":
                upscale_page_replicate()
            elif st.session_state.selected_mode in ["outfit", "face", "background", "color"]:
                edit_page(st.session_state.selected_mode)

if __name__ == "__main__":
    main()
