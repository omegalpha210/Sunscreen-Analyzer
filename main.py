# main.py
import streamlit as st
import re
from ingredients_data import UV_FILTERS, PORE_CLOGGERS, FOLLICULITIS_TRIGGERS

# 모바일에서도 화면이 꽉 차지 않도록 넓이를 최적화 (centered 활용 시 모바일에 완벽 적응)
st.set_page_config(page_title="Sunscreen Analyzer", page_icon="☀️", layout="centered")

# --- UI 텍스트 언어팩 ---
UI = {
    "kr": {
        "title": "☀️ 선크림 전성분 상세 분석기",
        "placeholder": "여기에 전성분 텍스트를 붙여넣기 하세요...",
        "btn_sample_kr": "예시: 라운드랩 (한국어)",
        "btn_sample_en": "예시: 라로슈포제 (영어)",
        "btn_analyze": "정밀 분석 시작",
        "warn_empty": "분석할 텍스트를 입력해주세요.",
        "inorg_title": "🧱 무기자차 (Physical)",
        "org_title": "🧪 유기자차 (Chemical)",
        "clog_title": "🚫 모공 막힘 (Comedogenic)",
        "folli_title": "🦠 모낭염 주의 (Fungal Acne)",
        "range": "차단",
        "comedo_score": "코메도제닉 지수",
        "tag_new": "✨ 신형",
        "tag_old": "🕰️ 구형",
        "reef_warn": "🪸 해양생태계 파괴 성분 (하와이 금지)",
        "mixed_title": "💜 혼합자차 (무기+유기)",
        "mixed_desc": "발림성이 좋고 백탁이 적으며, 바르자마자 차단 효과를 내는 밸런스형 선크림입니다.",
        "phys_title": "🧱 100% 무기자차 (물리적 차단)",
        "phys_desc": "자외선을 튕겨냅니다. 민감성 피부에 좋지만 백탁 현상이 있을 수 있습니다.",
        "chem_title": "🧪 100% 유기자차 (화학적 차단)",
        "chem_desc": "자외선을 흡수해 열로 배출합니다. 발림성이 뛰어나지만 사람에 따라 눈시림이 있을 수 있습니다.",
        "none_title": "❓ 자외선 차단 성분 미검출",
        "none_desc": "선크림 성분을 찾을 수 없습니다.",
        "share_title": "📤 결과 공유하기 (복사하기)",
        "empty": "검출 없음"
    },
    "en": {
        "title": "☀️ Sunscreen Ingredient Analyzer",
        "placeholder": "Paste your ingredient list here...",
        "btn_sample_kr": "Sample: Korean",
        "btn_sample_en": "Sample: English",
        "btn_analyze": "Analyze Ingredients",
        "warn_empty": "Please enter ingredients to analyze.",
        "inorg_title": "🧱 Physical Filters",
        "org_title": "🧪 Chemical Filters",
        "clog_title": "🚫 Pore Clogging",
        "folli_title": "🦠 Fungal Acne Triggers",
        "range": "Range",
        "comedo_score": "Comedogenic Rating",
        "tag_new": "✨ New Gen",
        "tag_old": "🕰️ Old Gen",
        "reef_warn": "🪸 Reef Harmful (Banned in Hawaii)",
        "mixed_title": "💜 Hybrid Sunscreen (Physical + Chemical)",
        "mixed_desc": "Offers great blendability with immediate protection. A well-balanced choice.",
        "phys_title": "🧱 100% Physical (Mineral) Sunscreen",
        "phys_desc": "Reflects UV rays. Great for sensitive skin but may leave a white cast.",
        "chem_title": "🧪 100% Chemical Sunscreen",
        "chem_desc": "Absorbs UV rays. No white cast and cosmetically elegant, but may cause eye stinging.",
        "none_title": "❓ No UV Filters Found",
        "none_desc": "We couldn't find any sunscreen filters in the text.",
        "share_title": "📤 Share Results (Copy Text)",
        "empty": "None found"
    }
}

# CSS (모바일 반응형을 고려한 디자인)
st.markdown("""
    <style>
    .main { background-color: #FAF8F5; }
    .result-card { background-color: #FFFFFF; padding: 15px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); margin-bottom: 12px; border-left: 6px solid #D6C3B3; }
    .inorganic-card { border-left-color: #4A90E2; }
    .organic-card { border-left-color: #43A047; }
    .clogger-card { border-left-color: #FBC02D; }
    .folliculitis-card { border-left-color: #E53935; }
    .card-title { font-size: 15px; font-weight: 700; color: #111; margin-bottom: 5px; line-height: 1.4; display: flex; align-items: center; flex-wrap: wrap; gap: 6px;}
    .card-info { font-size: 13px; color: #666; line-height: 1.4; margin-top: 4px; }
    .score-tag { color: #D32F2F; font-weight: 700; font-size: 12px; margin-top: 5px; }
    .gen-new { background-color: #E3F2FD; color: #1976D2; font-size: 11px; padding: 2px 6px; border-radius: 4px; font-weight: 800; }
    .gen-old { background-color: #EEEEEE; color: #757575; font-size: 11px; padding: 2px 6px; border-radius: 4px; font-weight: 800; }
    .reef-warning { color: #D32F2F; font-size: 12px; font-weight: 800; margin-top: 5px; display: block; }
    h3 { font-size: 18px; border-bottom: 2px solid #EEE; padding-bottom: 8px; color: #444; margin-top: 20px; }
    </style>
""", unsafe_allow_html=True)

# 1. 언어 선택 토글
lang_choice = st.radio("", ["🇰🇷 한국어", "🇺🇸 English"], horizontal=True)
lang = "kr" if "한국어" in lang_choice else "en"
L = UI[lang]

st.title(L["title"])

# 세션 상태 초기화 (입력창 텍스트 유지를 위해)
if "input_val" not in st.session_state:
    st.session_state.input_val = ""

# 2. 샘플 데이터 버튼 (사용자 편의성 향상)
col_s1, col_s2 = st.columns(2)
if col_s1.button(L["btn_sample_kr"]):
    st.session_state.input_val = "정제수, 다이부틸아디페이트, 프로판다이올, 디에칠아미노하이드록시벤조일헥실벤조에이트, 폴리메틸실세스퀴옥세인, 에칠헥실트리아존, 나이아신아마이드, 메칠렌비스-벤조트리아졸릴테트라메틸부틸페놀, 코코-카프릴레이트/카프레이트, 카프릴릴메티콘, 디에칠헥실부타미도트리아존, 글리세린, 1,2-헥산다이올, 부틸렌글라이콜, 자작나무수액, 소듐하이알루로네이트..."
if col_s2.button(L["btn_sample_en"]):
    st.session_state.input_val = "AQUA / WATER • ALCOHOL DENAT. • DIISOPROPYL SEBACATE • SILICA • ISOPROPYL MYRISTATE • ETHYLHEXYL SALICYLATE • ETHYLHEXYL TRIAZONE • BIS-ETHYLHEXYLOXYPHENOL METHOXYPHENYL TRIAZINE • BUTYL METHOXYDIBENZOYLMETHANE • GLYCERIN • DROMETRIZOLE TRISILOXANE..."

input_text = st.text_area(L["placeholder"], value=st.session_state.input_val, height=150)

def standardize(text):
    if not text: return ""
    text = re.sub(r'[^가-힣a-zA-Z0-9]', '', text).lower()
    subs = {"메칠": "메틸", "에칠": "에틸", "다이": "디", "트라이": "트리", "아이소": "이소"}
    for old, new in subs.items(): text = text.replace(old, new)
    return text

def analyze():
    std_input = standardize(input_text)
    res_inorganic, res_organic, res_cloggers, res_folliculitis = [], [], [], []

    for key, data in UV_FILTERS.items():
        for kw in data['keywords']:
            std_kw = standardize(kw)
            if std_kw in std_input:
                if std_kw == "zincoxide" and "zincoxide" not in std_input: continue
                if std_kw == "zinc" and "zincoxide" not in std_input: continue
                
                item = {
                    "display": f"{data['display'][lang]} ({kw})",
                    "range": data['range'][lang], 
                    "peak": data['peak'],
                    "gen": data['gen'][lang] if data['gen'] else "",
                    "reef_harmful": data.get('reef_harmful', False)
                }
                if data['type'] == 'inorganic': res_inorganic.append(item)
                else: res_organic.append(item)
                break

    for key, info in PORE_CLOGGERS.items():
        for kw in info['keywords']:
            if standardize(kw) in std_input:
                res_cloggers.append({"display": f"{info['display'][lang]} ({kw})", "score": info['score']})
                break

    for key, info in FOLLICULITIS_TRIGGERS.items():
        for kw in info['keywords']:
            if standardize(kw) in std_input:
                res_folliculitis.append({"display": f"{info['display'][lang]} ({kw})", "desc": info['desc'][lang]})
                break
                    
    return res_inorganic, res_organic, res_cloggers, res_folliculitis

if st.button(L["btn_analyze"]):
    if not input_text.strip():
        st.warning(L["warn_empty"])
    else:
        inorg, org, clog, folli = analyze()
        
        # 타입 배너 출력
        if inorg and org:
            st.markdown(f'<div style="padding:15px; border-radius:10px; margin-bottom:20px; background-color:#F3E5F5; border-left:5px solid #9C27B0;"><div style="font-size:18px; font-weight:800; color:#6A1B9A; margin-bottom:5px;">{L["mixed_title"]}</div><div style="font-size:13px; color:#555;">{L["mixed_desc"]}</div></div>', unsafe_allow_html=True)
        elif inorg:
            st.markdown(f'<div style="padding:15px; border-radius:10px; margin-bottom:20px; background-color:#E3F2FD; border-left:5px solid #2196F3;"><div style="font-size:18px; font-weight:800; color:#1565C0; margin-bottom:5px;">{L["phys_title"]}</div><div style="font-size:13px; color:#555;">{L["phys_desc"]}</div></div>', unsafe_allow_html=True)
        elif org:
            st.markdown(f'<div style="padding:15px; border-radius:10px; margin-bottom:20px; background-color:#E8F5E9; border-left:5px solid #4CAF50;"><div style="font-size:18px; font-weight:800; color:#2E7D32; margin-bottom:5px;">{L["chem_title"]}</div><div style="font-size:13px; color:#555;">{L["chem_desc"]}</div></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div style="padding:15px; border-radius:10px; margin-bottom:20px; background-color:#FAFAFA; border-left:5px solid #9E9E9E;"><div style="font-size:18px; font-weight:800; color:#616161; margin-bottom:5px;">{L["none_title"]}</div><div style="font-size:13px; color:#555;">{L["none_desc"]}</div></div>', unsafe_allow_html=True)

        # 3. 레이아웃 모바일 최적화 (모바일에서는 세로로 쌓이고 PC에서는 가로 정렬됨)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"### {L['inorg_title']}")
            for item in inorg: st.markdown(f'<div class="result-card inorganic-card"><div class="card-title">🛡️ {item["display"]}</div><div class="card-info">{L["range"]}: {item["range"]}<br>Peak: {item["peak"]}</div></div>', unsafe_allow_html=True)
            if not inorg: st.info(L["empty"])
            
            st.markdown(f"### {L['clog_title']}")
            for item in clog: st.markdown(f'<div class="result-card clogger-card"><div class="card-title">⚠️ {item["display"]}</div><div class="score-tag">{L["comedo_score"]}: {item["score"]}/5</div></div>', unsafe_allow_html=True)
            if not clog: st.success(L["empty"])

        with col2:
            st.markdown(f"### {L['org_title']}")
            for item in org: 
                gen_html, reef_html = "", ""
                if item["gen"] == "신형" or item["gen"] == "New Gen": gen_html = f'<span class="gen-new">{L["tag_new"]}</span>'
                elif item["gen"] == "구형" or item["gen"] == "Old Gen": gen_html = f'<span class="gen-old">{L["tag_old"]}</span>'
                if item["reef_harmful"]: reef_html = f'<span class="reef-warning">{L["reef_warn"]}</span>'
                
                st.markdown(f'<div class="result-card organic-card"><div class="card-title">🧬 {item["display"]} {gen_html}</div>{reef_html}<div class="card-info">{L["range"]}: {item["range"]}<br>Peak: {item["peak"]}</div></div>', unsafe_allow_html=True)
            if not org: st.info(L["empty"])
            
            st.markdown(f"### {L['folli_title']}")
            for item in folli: st.markdown(f'<div class="result-card folliculitis-card"><div class="card-title">🍄 {item["display"]}</div><div class="card-info">{item["desc"]}</div></div>', unsafe_allow_html=True)
            if not folli: st.success(L["empty"])
            
        # 4. 결과 공유하기 기능 (복사용 텍스트 박스 제공)
        st.markdown("---")
        with st.expander(L["share_title"], expanded=False):
            share_text = f"☀️ Sunscreen Analysis Result\n\n"
            share_text += f"[ {L['inorg_title']} ]\n" + ("\n".join([f"- {i['display']}" for i in inorg]) if inorg else "None") + "\n\n"
            share_text += f"[ {L['org_title']} ]\n" + ("\n".join([f"- {i['display']}" for i in org]) if org else "None") + "\n\n"
            share_text += f"[ {L['clog_title']} ]\n" + ("\n".join([f"- {i['display']} (Score: {i['score']}/5)" for i in clog]) if clog else "None")
            
            st.code(share_text, language="markdown")