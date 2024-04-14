from PIL import Image
import imageio

def shift_pixels(image, offset):
    width, height = image.size
    pixels = image.load()

    shifted_image = Image.new("RGB", (width, height))
    shifted_pixels = shifted_image.load()

    for y in range(height):
        for x in range(width):
            shifted_x = (x + offset) % width
            shifted_pixels[shifted_x, y] = pixels[x, y]

    return shifted_image

def shift_gif(input_gif_path, step=1, to_left=False):
    output_gif_path = "output.gif"
    frames = []

    with imageio.get_reader(input_gif_path) as reader:
        for i, frame in enumerate(reader):
            image = Image.fromarray(frame)
            shifted_image = shift_pixels(image, (i + 1) * -1 * step if to_left else (i + 1) * step)
            frames.append(shifted_image)

    imageio.mimsave(output_gif_path, frames, format='GIF', duration=0.1)
    print(f"Frames shifted and saved to {output_gif_path}.")

if __name__ == "__main__":
    shift_gif("input.gif", 1, True)