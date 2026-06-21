import json
import google.generativeai as genai

# 본인의 API 키를 여기에 입력하세요
genai.configure(api_key="AQ.Ab8RN6JF04JOMsREgPIxZ__EO2G5TBqLTrY6y7Ex2VbhCOu1jA")

def get_summary(company):
    # 모델 이름을 'gemini-1.5-flash-latest'로 변경
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    response = model.generate_content(f"{company}의 현재 주가 전망과 주요 이슈를 투자자 입장에서 핵심만 3줄로 요약해줘.")
    return response.text

data = {
    "samsung": get_summary("삼성전자"),
    "hynix": get_summary("SK하이닉스")
}

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
