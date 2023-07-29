# gradio_api.py
import gradio as gr
import subprocess

def run_streamlit_app():
    subprocess.call(["streamlit", "run", "app.py"])

gr.Interface(fn=run_app).launch(share=True)
