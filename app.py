import gradio as gr


def greet(name: str) -> str:
    if not name:
        return "Hello World"
    return f"Hello {name}"


demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(label="Nom", placeholder="World"),
    outputs=gr.Textbox(label="Message"),
    title="Hello World",
)


if __name__ == "__main__":
    demo.launch()
