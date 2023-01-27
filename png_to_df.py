import numpy as np
from PIL import Image

def open_image(filepath, size: list):
    img = Image.open(filepath)
    img.thumbnail(size=size)
    return img


def png_to_csv(image: Image.Image, max_alpha_iters = 4, alpha_range: list = None):
    alpha_iter_size = int(256 / 4)
    image_arr = np.array(image)
    alpha_range_ = list(range(alpha_iter_size, max_alpha_iters * alpha_iter_size + 1, alpha_iter_size))
    if not alpha_range is None:
        alpha_range_ = alpha_range
    print(image_arr.shape)
    data = [["a", "b"]]
    for rown, row in enumerate(image_arr.tolist()[::-1]):
        for coln, pixel in enumerate(row):
            pixel_alpha = sum(pixel) / len(pixel)
            for iter in alpha_range_[::-1]:
                if iter < pixel_alpha:
                    break
                data.append([str(coln), str(rown)])
    with open('output.csv', 'w') as file:
        file.write("\n".join([",".join(a) for a in data]))
                
image = open_image("mhr.jpg", (256, 256))
png_to_csv(image, alpha_range=[0, 50, 80, 90, 120, 130, 140, 150, 200, 250])
