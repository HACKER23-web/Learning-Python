import os
from openai import OpenAI

client =OpenAI(
    api_key=os.environ.get("MOONSHOT_API_KEY"),
    base_url="https://api.moonshot.cn/v1",
)

completion=client.chat.completions.create(
    model="kimi-k3",
    messages=[
        {"role": "user", "content": "你好,我是学Python的大学生,用一句话鼓励我"}
    ]
)

print(completion.choices[0].message.content)