from PIL import ImageDraw
import gradio as gr


MARGIN = 20


def annotate_image(image):
    annotated = image.copy()
    draw = ImageDraw.Draw(annotated)
    width, height = annotated.size
    box_size = min(width, height) // 4
    top_left = (MARGIN, MARGIN)
    bottom_right = (MARGIN + box_size, MARGIN + box_size)
    draw.rectangle([top_left, bottom_right], outline="red", width=4)
    draw.text((MARGIN, MARGIN + 10 + box_size), "Annotated", fill="red")
    return annotated


def build_demo():
    with gr.Blocks() as demo:
        gr.Markdown("# RockJoint Image Annotation Demo")
        with gr.Row():
            input_image = gr.Image(type="pil", label="Upload image")
            output_image = gr.Image(type="pil", label="Annotated image")
        annotate_button = gr.Button("Annotate")
        annotate_button.click(annotate_image, inputs=input_image, outputs=output_image)
    return demo


if __name__ == "__main__":
    build_demo().launch()
