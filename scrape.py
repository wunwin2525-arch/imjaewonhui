import os
import json
import google.generativeai as genai

# 1. GitHub Secrets에서 API 키를 가져옵니다.
api_key = os.environ.get("API_KEY")

# 2. 키가 설정되어 있는지 확인합니다.
if not api_key:
    raise ValueError("API_KEY 환경변수가 설정되지 않았습니다. GitHub Secrets를 확인하세요.")

genai.configure(api_key=api_key)

def get_summary(company):
    # 안정적인 gemini-1.5-flash 모델을 사용합니다.
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(f"{company}의 현재 주가 전망과 주요 이슈를 투자자 입장에서 핵심만 3줄로 요약해줘.")
    return response.text

# 3. 뉴스 요약을 진행합니다.
try:
    data = {
        "samsung": get_summary("삼성전자"),
        "hynix": get_summary("SK하이닉스")
    }

    # 4. 결과를 data.json 파일로 저장합니다.
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
    print("성공적으로 업데이트되었습니다.")
except Exception as e:
    print(f"오류 발생: {e}")
    exit(1) # 오류 발생 시 Actions를 중단시킴
