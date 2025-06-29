import gradio as gr
from dotenv import load_dotenv
from services.hr_evaluator import HREvaluatorService
import os
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import gradio
print(gradio.__version__)

load_dotenv(override=True)

if __name__ == "__main__":
    hrEvaluator = HREvaluatorService()

    gr.ChatInterface(
        hrEvaluator.chat,
        textbox=gr.MultimodalTextbox(
            file_types=[".pdf"],
            label="Candidate CV",
            placeholder="Please upload a candidate CV as a PDF file"
        ),
        type="messages"
    ).launch(server_port=7860)