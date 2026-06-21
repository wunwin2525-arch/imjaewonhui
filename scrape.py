import os
import json
import google.generativeai as genai

# 1. API 키 설정 (직접 입력 방식)
genai.configure(api_key="AQ.Ab8RN6KbqWY6pkFRHHntWCNYJHO6jMVR9-6nBTzWQG0TV65LYg")

def get_summary(company):
    # 최신 라이브러리 방식의 모델 호출
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(f"{company}의 현재 주가 전망과 주요 이슈를 투자자 입장에서 핵심만 3줄로 요약해줘.")
    return response.text

try:
    data = {
        "samsung": get_summary("삼성전자"),
        "hynix": get_summary("SK하이닉스")
    }
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
except Exception as e:
    print(f"오류 발생: {e}")
    exit(1)
