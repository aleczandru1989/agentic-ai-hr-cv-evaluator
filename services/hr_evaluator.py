from docling.document_converter import DocumentConverter
from openai import OpenAI

from const.prompts import Prompt
from const.tools import Tools

import json

class HREvaluatorService():
    def __init__(self):
        self.openai = OpenAI()


    def chat(self, message, history):
        system_prompt = self.get_system_prompt()

        user_prompt = self.get_user_message(message)

        messages = [{"role": "system", "content": system_prompt}] + self.get_normalized_history(history) + [{"role": "user", "content": user_prompt}]
    
        try:
            response = self.openai.chat.completions.create(model="gpt-4o-mini", messages=messages, tools=Tools.get())

            finish_reason = response.choices[0].finish_reason
        
            if finish_reason == "tool_calls":
                tool_call = response.choices[0].message.tool_calls[0]
                tool_name = tool_call.function.name
                tool_args = tool_call.function.arguments

                if isinstance(tool_args, str):
                    tool_args = json.loads(tool_args)

                # Check type of tool_args and call accordingly
                if isinstance(tool_args, dict):
                    Tools.call_tool_by_name(tool_name, **tool_args)
                else:
                    Tools.call_tool_by_name(tool_name, tool_args)
            
                messages.append({"role": "assistant", "content": response.choices[0].message.content, "tool_calls": [tool_call]}) 
        except Exception as e:
            print(f"Error occurred: {e}")
            print("Retrying...")
    
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
