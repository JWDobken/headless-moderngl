# https://github.com/moderngl/moderngl-window/blob/master/examples/headless.py
import moderngl
import moderngl_window
import numpy as np
from moderngl_window.conf import settings
from moderngl_window.timers.clock import Timer
from PIL import Image
from pyrr import Matrix44


class HeadlessOBJConfig(moderngl_window.WindowConfig):
    """
    Custom config for headless creation of PNG images.
    """

    samples = 0  # Headless is not always happy with multisampling
    # gl_version = (3, 3)
    aspect_ratio = 16 / 9
    # window_size = (1920, 1080)
    title = "Rebar Model"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Do initialization here
        # self.load_scene("/src/rebar.obj")
        # self.prog = self.ctx.program(...)
        # self.vao = self.ctx.vertex_array(...)

        # self.texture = self.ctx.texture(self.wnd.size, 4)
        self.scene = self.load_scene("/src/sitting.obj")
        # self.scene = self.load_scene('scenes/Apollo_17.stl')

        # self.camera.projection.update(near=0.1, far=100.0)
        # self.camera.velocity = 7.0
        # self.camera.mouse_sensitivity = 0.3

    def render(self, time, frame_time):
        """Render one frame, save to png and close it"""
        # self.ctx.enable_only(moderngl.DEPTH_TEST | moderngl.CULL_FACE)

        # translation = Matrix44.from_translation((0, 0, -1.5))
        # rotation = Matrix44.from_eulers((0, 0, 0))
        # model_matrix = translation * rotation
        # camera_matrix = self.camera.matrix * model_matrix

        # self.scene.draw(
        #     camera_matrix=camera_matrix,
        #     time=time,
        # )
        # Fill currently bound framebuffer with while background
        self.ctx.clear(1, 1, 1, 1)
        # Render the geometry
        # self.vao.render(mode=moderngl.TRIANGLES)

        # Wait for all rendering calls to finish (Might not be needed)
        self.ctx.finish()

        image = Image.frombytes(
            "RGBA", self.wnd.fbo.size, self.wnd.fbo.read(components=4)
        )
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
        image.save("sitting.png", format="png")

        self.wnd.close()


if __name__ == "__main__":
    HeadlessOBJConfig.run()
