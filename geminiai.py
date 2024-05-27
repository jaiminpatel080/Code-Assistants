import google.generativeai as genai
genai.configure(api_key="AIzaSyDR_tvNx0k2OjdpoGXe5rTOGpoMOxe_WkU")
# import pprint
# for model in genai.list_models():
#     pprint.pprint(model)
model=genai.GenerativeModel("gemini-pro")

prompt=input('Enter your prompt:')

response=model.generate_content(prompt)

print(response.text)