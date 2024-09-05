import openai

# OpenAI APIのキーを設定
openai.api_key = 'PTrkdxkDM24TVJ7OaVp4-8CxRpigL2ReJbvyoYVHJSkG_Jl7hsL14KPBpigKGDBCTcFyFppL7y_nPbxRZ-VcYYQ'

def diagnose(symptoms):
    prompt = f"以下の症状を基に考えられる病名を教えてください: {symptoms}"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    
    return response.choices[0].text.strip()