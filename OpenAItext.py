#env: openai==0.28.0, pandas==2.2.2

import os
import openai
import pandas as pd

# 设置 OPENAI_API_KEY 环境变量
openai.api_key = "sk-gG0jtlFztSOcTuYp592c203e049a483b8c98EdBcD27f9e75"

# 设置 OPENAI_BASE_URL 环境变量（如果需要自定义基础 URL）
openai.api_base = "https://api.xiaoai.plus/v1"  # 如果你使用的是自定义的 API 地址

# 读取源 Excel 文件
input_file = r'D:\Project\textOpenAI\data.xlsx'
df = pd.read_excel(input_file)

# 确保第一列是要变换的列
for i, row in df.iterrows():
    text_to_transform = row[0]  #此处可修改输入的列数 "n-1"  

    # 进行对话生成
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 使用 GPT-3.5 或 GPT-4 模型
        messages=[
            {"role": "system", "content": "你是识别国家iso编码的助手"},   #可修改AI角色设定
            {"role": "user", "content": f"请告诉我 {text_to_transform} 这个国家的 ISO 3 位编码，只回复 3 个大写字母，不要包含其他内容。"}   #可修改任务
        ]
    )

    # 获取模型的回答
    transformed_text = response['choices'][0]['message']['content']
    df.at[i, 1] = transformed_text  # 将结果写入第二列,此处可修改输出的列数 "n-1" 
    print(f"已完成第{i}行")

# 保存为新的 Excel 文件
output_file = r'D:\Project\textOpenAI\result.xlsx'
df.to_excel(output_file, index=False)

print("处理完成，输出文件已保存。")
