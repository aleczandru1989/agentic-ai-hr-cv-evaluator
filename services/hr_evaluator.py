from docling.document_converter import DocumentConverter
from openai import OpenAI

from const.prompts import Prompt


class HREvaluatorService():
    def __init__(self):
        self.openai = OpenAI()


    def chat(self, message, history):
        # if message["files"] is None or len(message["files"]) == 0:
        #     return "Please upload a candidate CV as a PDF file"

        system_prompt = self.get_system_prompt()

        user_prompt = self.get_user_message(message)

        messages = [{"role": "system", "content": system_prompt}] + self.get_normalized_history(history) + [{"role": "user", "content": user_prompt}]

        response = self.openai.chat.completions.create(model="gpt-4o-mini", messages=messages)

        print(message)

        return response.choices[0].message.content

    def get_system_prompt(self) -> str:
        with open("./resources/profile.md", "r") as file:
            content = "\n".join(file.readlines())

            return Prompt.get_system_prompt(content)

    def get_user_message(self, message):
        if message["files"] is not None and len(message["files"]) > 0:
            file_path = message["files"][0]

            convertor = DocumentConverter()

            result = convertor.convert(file_path)

            return result.document.export_to_markdown()
        else:
            return message["text"]

    def get_normalized_history(self, histories):
        for history in histories:
            if isinstance(history['content'], tuple):
                history['content'] = history['content'][0]

        return histories;
