import os
import json
import google.generativeai as genai

# 코드에 직접 넣지 말고, 환경변수에서 가져옵니다
api_key = os.environ.get("API_KEY")
genai.configure(api_key=api_key)

def get_summary(company):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(f"{company}의 현재 주가 전망과 주요 이슈를 투자자 입장에서 핵심만 3줄로 요약해줘.")
    return response.text

data = {
    "samsung": get_summary("삼성전자"),
    "hynix": get_summary("SK하이닉스")
}

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
