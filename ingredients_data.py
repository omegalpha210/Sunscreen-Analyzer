# ingredients_data.py

# 1. 자외선 차단 성분 (글로벌 24종 및 모든 이명 완벽 포함)
UV_FILTERS = {
    # --- 무기자차 ---
    "Zinc Oxide": {
        "display": {"kr": "징크옥사이드", "en": "Zinc Oxide"},
        "type": "inorganic", "range": {"kr": "UVA + UVB (광범위)", "en": "UVA + UVB (Broad)"}, 
        "peak": "약 370nm", "gen": {"kr": "", "en": ""}, "reef_harmful": False,
        "keywords": ["징크옥사이드", "zinc oxide", "아연화", "zincoxide"]
    },
    "Titanium Dioxide": {
        "display": {"kr": "티타늄디옥사이드", "en": "Titanium Dioxide"},
        "type": "inorganic", "range": {"kr": "UVB + UVA2", "en": "UVB + UVA2"}, 
        "peak": "약 305nm", "gen": {"kr": "", "en": ""}, "reef_harmful": False,
        "keywords": ["티타늄디옥사이드", "titanium dioxide", "이산화티타늄", "titaniumdioxide"]
    },
    
    # --- 유기자차 (신형) ---
    "Tinosorb S": {
        "display": {"kr": "티노소브 S", "en": "Tinosorb S"},
        "type": "organic", "range": {"kr": "UVA + UVB (광범위)", "en": "UVA + UVB (Broad)"}, "peak": "310nm, 343nm",
        "gen": {"kr": "신형", "en": "New Gen"}, "reef_harmful": False,
        "keywords": ["비스에틸헥실옥시페놀메톡시페닐트리아진", "bis-ethylhexyloxyphenol methoxyphenyl triazine", "tinosorb s", "bemt"]
    },
    "Tinosorb M": {
        "display": {"kr": "티노소브 M", "en": "Tinosorb M"},
        "type": "organic", "range": {"kr": "UVA + UVB (혼합)", "en": "UVA + UVB (Mixed)"}, "peak": "305nm, 360nm",
        "gen": {"kr": "신형", "en": "New Gen"}, "reef_harmful": False,
        "keywords": ["메틸렌비스벤조트라이아졸릴테트라메틸부틸페놀", "methylene bis-benzotriazolyl tetramethylbutylphenol", "tinosorb m", "mbbt"]
    },
    "Tinosorb A2B": {
        "display": {"kr": "티노소브 A2B", "en": "Tinosorb A2B"},
        "type": "organic", "range": {"kr": "UVB + UVA2", "en": "UVB + UVA2"}, "peak": "310nm",
        "gen": {"kr": "신형", "en": "New Gen"}, "reef_harmful": False,
        "keywords": ["트리스-비페닐트리아진", "tris-biphenyl triazine", "tinosorb a2b"]
    },
    "Uvinul A Plus": {
        "display": {"kr": "유비눌 A 플러스", "en": "Uvinul A Plus"},
        "type": "organic", "range": {"kr": "UVA1 (장파)", "en": "UVA1 (Long)"}, "peak": "354nm",
        "gen": {"kr": "신형", "en": "New Gen"}, "reef_harmful": False,
        "keywords": ["디에틸아미노하이드록시벤조일헥실벤조에이트", "diethylamino hydroxybenzoyl hexyl benzoate", "uvinul a plus"]
    },
    "Uvinul T 150": {
        "display": {"kr": "유비눌 T 150", "en": "Uvinul T 150"},
        "type": "organic", "range": {"kr": "UVB", "en": "UVB"}, "peak": "314nm",
        "gen": {"kr": "신형", "en": "New Gen"}, "reef_harmful": False,
        "keywords": ["에틸헥실트리아존", "ethylhexyl triazone", "uvinul t 150"]
    },
    "Uvasorb HEB": {
        "display": {"kr": "유바소브 HEB", "en": "Uvasorb HEB"},
        "type": "organic", "range": {"kr": "UVB", "en": "UVB"}, "peak": "311nm",
        "gen": {"kr": "신형", "en": "New Gen"}, "reef_harmful": False,
        "keywords": ["디에틸헥실부타미도트리아존", "diethylhexyl butamido triazone", "uvasorb heb", "이스코트리지놀", "iscotrizinol"]
    },
    "Mexoryl SX": {
        "display": {"kr": "멕소릴 SX", "en": "Mexoryl SX"},
        "type": "organic", "range": {"kr": "UVA2", "en": "UVA2"}, "peak": "344nm",
        "gen": {"kr": "신형", "en": "New Gen"}, "reef_harmful": False,
        "keywords": ["테레프탈릴리덴디캠퍼설포닉애씨드", "terephthalylidene dicamphor sulfonic acid", "mexoryl sx", "에캄슐", "ecamsule"]
    },
    "Mexoryl XL": {
        "display": {"kr": "멕소릴 XL", "en": "Mexoryl XL"},
        "type": "organic", "range": {"kr": "UVB + UVA2", "en": "UVB + UVA2"}, "peak": "303nm, 344nm",
        "gen": {"kr": "신형", "en": "New Gen"}, "reef_harmful": False,
        "keywords": ["드로메트리졸트리실록산", "drometrizole trisiloxane", "mexoryl xl", "실트리졸", "silatrizole"]
    },
    "Mexoryl 400": {
        "display": {"kr": "멕소릴 400", "en": "Mexoryl 400"},
        "type": "organic", "range": {"kr": "UVA1 (초장파)", "en": "UVA1 (Ultra Long)"}, "peak": "385nm",
        "gen": {"kr": "신형", "en": "New Gen"}, "reef_harmful": False,
        "keywords": ["메톡시프로필아미노사이클로헥세닐리덴에톡시에틸사이아노아세테이트", "methoxypropylamino cyclohexenylidene ethoxyethylcyanoacetate", "mexoryl 400"]
    },
    "Triasorb": {
        "display": {"kr": "트리아소브", "en": "Triasorb"},
        "type": "organic", "range": {"kr": "UVA + UVB + Blue Light", "en": "UVA + UVB + Blue Light"}, "peak": "310nm, 350nm, 450nm",
        "gen": {"kr": "신형", "en": "New Gen"}, "reef_harmful": False,
        "keywords": ["페닐렌비스-다이페닐트라이아진", "phenylene bis-diphenyltriazine", "triasorb"]
    },
    "Polysilicone-15": {
        "display": {"kr": "폴리실리콘-15", "en": "Polysilicone-15"},
        "type": "organic", "range": {"kr": "UVB", "en": "UVB"}, "peak": "312nm",
        "gen": {"kr": "신형", "en": "New Gen"}, "reef_harmful": False,
        "keywords": ["폴리실리콘-15", "polysilicone-15", "파솔slx", "parsol slx"]
    },
    "Amiloxate": {
        "display": {"kr": "아밀록세이트", "en": "Amiloxate"},
        "type": "organic", "range": {"kr": "UVB", "en": "UVB"}, "peak": "310nm",
        "gen": {"kr": "신형", "en": "New Gen"}, "reef_harmful": False,
        "keywords": ["이소아밀p-메톡시신나메이트", "isoamyl p-methoxycinnamate", "amiloxate"]
    },
    "Neo Heliopan AP": {
        "display": {"kr": "네오헬리오판 AP", "en": "Neo Heliopan AP"},
        "type": "organic", "range": {"kr": "UVA2", "en": "UVA2"}, "peak": "335nm",
        "gen": {"kr": "신형", "en": "New Gen"}, "reef_harmful": False,
        "keywords": ["디소듐페닐디벤즈이미다졸테트라설포네이트", "bisdisulizole disodium", "neo heliopan ap"]
    },

    # --- 유기자차 (구형) ---
    "Octinoxate": {
        "display": {"kr": "옥티노세이트", "en": "Octinoxate"},
        "type": "organic", "range": {"kr": "UVB", "en": "UVB"}, "peak": "310nm",
        "hormone_harmful": True, # 추가
        "gen": {"kr": "구형", "en": "Old Gen"}, "reef_harmful": True,
        "keywords": ["에틸헥실메톡시신나메이트", "ethylhexyl methoxycinnamate", "옥티노세이트", "octinoxate", "옥틸메톡시신나메이트", "octyl methoxycinnamate"]
    },
    "Octisalate": {
        "display": {"kr": "옥티살레이트", "en": "Octisalate"},
        "type": "organic", "range": {"kr": "UVB", "en": "UVB"}, "peak": "307nm",
        "gen": {"kr": "구형", "en": "Old Gen"}, "reef_harmful": False,
        "keywords": ["에틸헥실살리실레이트", "ethylhexyl salicylate", "옥티살레이트", "octisalate", "옥틸살리실레이트", "octyl salicylate"]
    },
    "Avobenzone": {
        "display": {"kr": "아보벤존", "en": "Avobenzone"},
        "type": "organic", "range": {"kr": "UVA1 (장파)", "en": "UVA1 (Long)"}, "peak": "357nm",
        "hormone_harmful": True, # 추가
        "gen": {"kr": "구형", "en": "Old Gen"}, "reef_harmful": False,
        "keywords": ["부틸메톡시디벤조일메탄", "butyl methoxydibenzoylmethane", "아보벤존", "avobenzone", "parsol 1789"]
    },
    "Oxybenzone": {
        "display": {"kr": "옥시벤존", "en": "Oxybenzone"},
        "type": "organic", "range": {"kr": "UVB + UVA2", "en": "UVB + UVA2"}, "peak": "288nm, 325nm",
        "hormone_harmful": True, # 추가
        "gen": {"kr": "구형", "en": "Old Gen"}, "reef_harmful": True,
        "keywords": ["벤조페논-3", "benzophenone-3", "oxybenzone"]
    },
    "Sulisobenzone": {
        "display": {"kr": "설리소벤존", "en": "Sulisobenzone"},
        "type": "organic", "range": {"kr": "UVB + UVA2", "en": "UVB + UVA2"}, "peak": "285nm, 324nm",
        "gen": {"kr": "구형", "en": "Old Gen"}, "reef_harmful": False,
        "keywords": ["벤조페논-4", "benzophenone-4", "sulisobenzone"]
    },
    "Octocrylene": {
        "display": {"kr": "옥토크릴렌", "en": "Octocrylene"},
        "type": "organic", "range": {"kr": "UVB", "en": "UVB"}, "peak": "303nm",
        "gen": {"kr": "구형", "en": "Old Gen"}, "reef_harmful": False,
        "keywords": ["옥토크릴렌", "octocrylene"]
    },
    "Homosalate": {
        "display": {"kr": "호모살레이트", "en": "Homosalate"},
        "type": "organic", "range": {"kr": "UVB", "en": "UVB"}, "peak": "306nm",
        "hormone_harmful": True, # 추가
        "gen": {"kr": "구형", "en": "Old Gen"}, "reef_harmful": False,
        "keywords": ["호모살레이트", "homosalate"]
    },
    "Ensulizole": {
        "display": {"kr": "엔술리졸", "en": "Ensulizole"},
        "type": "organic", "range": {"kr": "UVB", "en": "UVB"}, "peak": "302nm",
        "gen": {"kr": "구형", "en": "Old Gen"}, "reef_harmful": False,
        "keywords": ["페닐벤즈이미다졸설포닉애씨드", "phenylbenzimidazole sulfonic acid", "ensulizole"]
    },
    "4-MBC": {
        "display": {"kr": "4-MBC", "en": "4-MBC"},
        "type": "organic", "range": {"kr": "UVB", "en": "UVB"}, "peak": "300nm",
        "hormone_harmful": True, # 추가
        "gen": {"kr": "구형", "en": "Old Gen"}, "reef_harmful": False,
        "keywords": ["4-메틸벤질리덴캠퍼", "4-methylbenzylidene camphor", "4-mbc"]
    },
    "Padimate O": {
        "display": {"kr": "파디메이트 O", "en": "Padimate O"},
        "type": "organic", "range": {"kr": "UVB", "en": "UVB"}, "peak": "311nm",
        "gen": {"kr": "구형", "en": "Old Gen"}, "reef_harmful": False,
        "keywords": ["에틸헥실디메틸파바", "ethylhexyl dimethyl paba", "padimate o"]
    }
}

# 2. 모공 막힘 성분 (그대로 유지)
PORE_CLOGGERS = {
    "Lauric Acid": {"display": {"kr": "라우릭애씨드", "en": "Lauric Acid"}, "score": 4, "keywords": ["라우릭애씨드", "lauric acid"]},
    "Myristic Acid": {"display": {"kr": "미리스틱애씨드", "en": "Myristic Acid"}, "score": 3, "keywords": ["미리스틱애씨드", "myristic acid"]},
    "Palmitic Acid": {"display": {"kr": "팔미틱애씨드", "en": "Palmitic Acid"}, "score": 2, "keywords": ["팔미틱애씨드", "palmitic acid"]},
    "Stearic Acid": {"display": {"kr": "스테아릭애씨드", "en": "Stearic Acid"}, "score": 3, "keywords": ["스테아릭애씨드", "stearic acid"]},
    "Isopropyl Myristate": {"display": {"kr": "이소프로필미리스테이트", "en": "Isopropyl Myristate"}, "score": 5, "keywords": ["이소프로필미리스테이트", "아이소프로필미리스테이트", "isopropyl myristate"]},
    "Isopropyl Palmitate": {"display": {"kr": "이소프로필팔미테이트", "en": "Isopropyl Palmitate"}, "score": 4, "keywords": ["이소프로필팔미테이트", "아이소프로필팔미테이트", "isopropyl palmitate"]},
    "Ethylhexyl Palmitate": {"display": {"kr": "에틸헥실팔미테이트", "en": "Ethylhexyl Palmitate"}, "score": 4, "keywords": ["에틸헥실팔미테이트", "ethylhexyl palmitate"]},
    "Laureth-4": {"display": {"kr": "라우레스-4", "en": "Laureth-4"}, "score": 5, "keywords": ["라우레스-4", "laureth-4"]},
    "Coconut Oil": {"display": {"kr": "코코넛야자오일", "en": "Coconut Oil"}, "score": 4, "keywords": ["코코넛야자오일", "코코넛오일", "coconut oil"]},
    "Shea Butter": {"display": {"kr": "시어버터", "en": "Shea Butter"}, "score": 2, "keywords": ["시어버터", "shea butter"]},
    "Cetearyl Alcohol": {"display": {"kr": "세테아릴알코올", "en": "Cetearyl Alcohol"}, "score": 2, "keywords": ["세테아릴알코올", "cetearyl alcohol"]},
    "Sodium Chloride": {"display": {"kr": "소듐클로라이드", "en": "Sodium Chloride"}, "score": 5, "keywords": ["소듐클로라이드", "sodium chloride"]},
    "Algae Extract": {"display": {"kr": "조류추출물", "en": "Algae Extract"}, "score": 5, "keywords": ["조류추출물", "algae extract"]}
}

# 3. 모낭염 주의 성분 (그대로 유지)
FOLLICULITIS_TRIGGERS = {
    "Fatty Acids": {
        "display": {"kr": "지방산류", "en": "Fatty Acids"},
        "keywords": ["라우릭애씨드", "미리스틱애씨드", "팔미틱애씨드", "스테아릭애씨드", "lauric acid", "myristic acid", "palmitic acid", "stearic acid"], 
        "desc": {"kr": "말라세지아균의 먹이가 되어 진균성 트러블을 유발할 수 있습니다.", "en": "Can feed Malassezia yeast, triggering fungal acne."}
    },
    "Esters/Oils": {
        "display": {"kr": "에스테르/오일류", "en": "Esters & Oils"},
        "keywords": ["폴리소르베이트","폴리솔베이트", "글리세릴스테아레이트", "에틸헥실팔미테이트", "아이소프로필팔미테이트", "polysorbate", "glyceryl stearate", "isopropyl palmitate", "ethylhexyl palmitate"], 
        "desc": {"kr": "진균 증식을 돕는 환경을 조성합니다.", "en": "Creates an environment that helps fungi thrive."}
    },
    "Fermented": {
        "display": {"kr": "발효 성분", "en": "Fermented Ingredients"},
        "keywords": ["갈락토미세스", "비피다", "발효", "ferment", "galactomyces"], 
        "desc": {"kr": "일부 모낭염 피부에 강한 자극이 될 수 있습니다.", "en": "Can cause irritation for fungal acne-prone skin."}
    }
}
