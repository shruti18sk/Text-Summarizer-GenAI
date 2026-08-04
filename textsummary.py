import torch
import gradio as gr

from transformers import pipeline

model_path= "../Models/models--sshleifer--distilbart-cnn-12-6/snapshots/a4f8f3ea906ed274767e9906dbaede7531d660ff"

text_summary = pipeline(
    "summarization",
    model=model_path,
    torch_dtype=torch.float32
)

#text='''Elon Reeve Musk (/ˈiːlɒn/ ⓘ EE-lon; born June 28, 1971) is a businessman and former public official who is the CEO and largest shareholder of Tesla and SpaceX. Musk has been the wealthiest person in the world since 2025, and became the only trillionaire in terms of US dollars in June 2026; as of July 23, 2026, Forbes estimates his net worth to be US$744 billion.'''
#print(text_summary(text,
   # max_length=40,
    #min_length=15,
   # do_sample=False));
def summary (input):
       output = text_summary(input)
       return output[0]['summary_text']
gr.close_all()

#demo = gr.Interface(fn=summary, inputs="text", outputs="text")
demo = gr.Interface(
    fn=summary,
    inputs=[gr.Textbox(label="Input text to summarize", lines=6)],
    outputs=[gr.Textbox(label="Summarized text", lines=4)],
    title="Gen Artificial Intelligence Project 1: Text Summarizer",
    description="This application will summarize the text"
)

demo.launch()
