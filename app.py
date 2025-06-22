import gradio as gr
from dotenv import load_dotenv
from services.hr_evaluator import HREvaluatorService

load_dotenv(override=True)

hrEvaluator = HREvaluatorService()

gr.ChatInterface(hrEvaluator.chat,
                 textbox=gr.MultimodalTextbox(file_types=[".pdf"]),
                 type="messages").launch()