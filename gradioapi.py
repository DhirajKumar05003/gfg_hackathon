# gradio_api.py
import gradio as gr
import subprocess

def run_streamlit_app():
    subprocess.call(["streamlit", "run", "streamlit_app.py"])

gr.Interface(fn=run_streamlit_app).launch(share=True)
