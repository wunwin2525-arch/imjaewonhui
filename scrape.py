import json
import os
import urllib.request

def get_summary(company):
    # API 키를 직접 변수에 넣으세요 (여기가 제일 중요합니다)
    api_key = "AQ.Ab8RN6KbqWY6pkFRHHntWCNYJHO6jMVR9-6nBTzWQG0TV65LYg"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    data = {
        "contents": [{"parts": [{"text": f"{company}의 현재 주가 전망과 주요 이슈를 투자자 입장에서 핵심만 3줄로 요약해줘."}]}]
    }
    
    req = urllib.request.Request(url, data=json.dumps(data).encode(), headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode())
        return result['candidates'][0]['content']['parts'][0]['text']

data = {
    "samsung": get_summary("삼성전자"),
    "hynix": get_summary("SK하이닉스")
}

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
