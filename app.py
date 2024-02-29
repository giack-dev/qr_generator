import gradio as gr
import validators as val
import qr


def validate_input_url(url: str) -> bool:
   val.url(url)




def main():
    inputURL: gr.Textbox = gr.Textbox(label="URL", value="Enter a URL(e.g. https://www.google.com/)", lines="1", max_lines="10", show_label=True)
    
    app: gr.Interface = gr.Interface(
        fn=validate_input_url,
        inputs=[inputURL],
        outputs=["text"],
    )
    
    app.launch()

if __name__ == "__main__":
   main()