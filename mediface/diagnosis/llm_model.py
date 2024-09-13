import requests
import os
import json

#APIキーの登録
os.environ["OPENAI_API_KEY"] = "__YOUR KEY__"

# 環境変数からAPIキーを取得
api_key = os.getenv('OPENAI_API_KEY')

# APIエンドポイント
url = 'https://api.openai.iniad.org/api/v1/chat/completions'

def diagnose(symptoms):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    # リクエストデータの作成
    request_data = {
        'model': 'gpt-4o-mini',
        'messages': [{'role': 'user', 'content': f'以下の症状から考えられる病名を教えてください: {symptoms}'}]
    }

    # APIリクエストを送信
    response = requests.post(url, headers=headers, data=json.dumps(request_data))

    # レスポンスのJSONデータを取得
    if response.status_code == 200:
        response_data = response.json()
        # LLMの返答を取得
        diagnosis = response_data['choices'][0]['message']['content']
        return diagnosis
    else:
        return "診断できませんでした。再度試してください。"
