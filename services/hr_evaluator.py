from openai import OpenAI

from const.prompts import Prompt


class HREvaluatorService():
    def __init__(self):
        self.openai = OpenAI()


    def chat(self, message, history):
        company_profile = self.get_company_profile()

        messages = [{"role": "system", "content": Prompt.get_system_prompt(company_profile)}] + history + [{"role": "user", "content": message}]

        response = self.openai.chat.completions.create(model="gpt-4o-mini", messages=messages)

        print(message)

        return response.choices[0].message.content

    def get_company_profile(self) -> str:
        with open("./resources/profile.md", "r") as file:
            content = file.readlines()

            return content