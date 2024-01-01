import imageio
import numpy as np
import gradio as gr
from PIL import Image
from subprocess import PIPE, run

from demo.animate import MagicAnimate

from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="runwayml/stable-diffusion-v1-5", local_dir="./stable-diffusion-v1-5"
)
snapshot_download(repo_id="stabilityai/sd-vae-ft-mse", local_dir="./sd-vae-ft-mse")
snapshot_download(repo_id="zcxu-eric/MagicAnimate", local_dir="./MagicAnimate")

animator = MagicAnimate()


def animate(reference_image, motion_sequence_state, seed, steps, guidance_scale):
    return animator(reference_image, motion_sequence_state, seed, steps, guidance_scale)


app = gr.Blocks()
with app:
    animation = gr.Video(format="mp4", label="Animation Results", autoplay=True)

    with gr.Row():
        reference_image = gr.Image(label="Reference Image")
        motion_sequence = gr.Video(format="mp4", label="Motion Sequence")

        with gr.Column():
            random_seed = gr.Textbox(label="Random seed", value=1, info="default: -1")
            sampling_steps = gr.Textbox(
                label="Sampling steps", value=25, info="default: 25"
            )
            guidance_scale = gr.Textbox(
                label="Guidance scale", value=7.5, info="default: 7.5"
            )
            submit = gr.Button("Animate")

    def read_video(video):
        # size = int(size)
        reader = imageio.get_reader(video)
        fps = reader.get_meta_data()["fps"]
        assert fps == 25.0, f"Expected video fps: 25, but {fps} fps found"
        return video

    def read_image(image, size=512):
        return np.array(Image.fromarray(image).resize((size, size)))

    # when user uploads a new video
    motion_sequence.upload(read_video, motion_sequence, motion_sequence)
    # when `first_frame` is updated
    reference_image.upload(read_image, reference_image, reference_image)
    # when the `submit` button is clicked
    submit.click(
        animate,
        [reference_image, motion_sequence, random_seed, sampling_steps, guidance_scale],
        animation,
    )

if __name__ == "__main__":
    app.launch(share=False)
