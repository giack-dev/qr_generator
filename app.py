import gradio as gr
import validators as val
import random
from typing import Tuple
import os
import qr


def validate_input_url(url: str) -> bool:
    return val.url(url)
    
def generate_qr(url: str, file: str = './generated_qr_codes') -> Tuple[str, str]:
    if validate_input_url(url):
        random_image_number = random.randint(1, 10000)
        filename = f"generated_qr_{random_image_number}.jpg"
        filepath = os.path.join(file, filename)
        qr.create_qr_code(url, filepath)
        return "QR Code generated successfully.", filepath
    else:
        return "Invalid URL. Cannot generate QR Code.", ""


def main() -> None:
    input_url = gr.Textbox(label="URL", placeholder="Enter a Full URL(e.g. https://www.google.com/)", interactive=True, lines="1", max_lines="10", show_label=True)
    output_text = gr.Textbox(label="Message", placeholder="", interactive=False, lines="1", max_lines="10", show_label=True)
    generated_qr = gr.Image(type="filepath", height=256, width=256, show_download_button=True, show_share_button=True)

    app = gr.Interface(
        title="QR Code Generator",
        fn=generate_qr,
        inputs=input_url,
        outputs=[output_text, generated_qr],
    )
    
    app.launch()

if __name__ == "__main__":
   main()