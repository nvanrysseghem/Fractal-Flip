import PIL.Image as Image

def flip_image_horizontally(image):
    """Flips an image horizontally.

    Args:
        image: A PIL Image object.

    Returns:
        A flipped PIL Image object.
    """

    return image.transpose(Image.FLIP_LEFT_RIGHT)

def flip_image_vertically(image):
    """Flips an image vertically.

    Args:
        image: A PIL Image object.

    Returns:
        A flipped PIL Image object.
    """

    return image.transpose(Image.FLIP_TOP_BOTTOM)

def main():
    """Duplicates the image `image.png` 4 times and arranges them all in a row.
    Also duplicates the row, flips the duplicates vertically, and arranges them in a column below the original row.
    Flips the second and fourth images horizontally.
    Duplicates the new image and flips it vertically, then pastes it below the original new image.
    Crops the final image from the center, so the resulting image is 3840x2160.
    Increases the resolution of the final image to 300 ppi.

    Saves the new image as `new_image.png`.
    """

    # Load the image
    image = Image.open("image.png")

    # Duplicate the image 4 times
    images = []
    for i in range(4):
        images.append(image.copy())

    # Flip the second and fourth images horizontally
    images[1] = flip_image_horizontally(images[1])
    images[3] = flip_image_horizontally(images[3])

    # Arrange the images in a row
    row_image = Image.new("RGB", (4 * 1024, 1024))
    for i in range(4):
        row_image.paste(images[i], (i * 1024, 0))

    # Duplicate the row
    rows = []
    for i in range(2):
        rows.append(row_image.copy())

    # Flip the duplicates vertically
    rows[0] = flip_image_vertically(rows[0])
    rows[1] = flip_image_vertically(rows[1])

    # Arrange the rows in a column below the original row
    new_image = Image.new("RGB", (4 * 1024, 2 * 1024))
    new_image.paste(row_image, (0, 0))
    new_image.paste(rows[0], (0, 1024))
    new_image.paste(rows[1], (0, 2048))

    # Duplicate the new image
    new_images = []
    for i in range(2):
        new_images.append(new_image.copy())

    # Flip the duplicates vertically
    new_images[1] = flip_image_vertically(new_images[1])

    # Arrange the new images in a column below the original new image
    final_image = Image.new("RGB", (4 * 1024, 4 * 1024))
    final_image.paste(new_image, (0, 0))
    final_image.paste(new_images[1], (0, 2048))

    # Crop the final image from the center to 3840x2160
    width, height = final_image.size
    left = (width - 3840) / 2
    top = (height - 2160) / 2
    right = (width + 3840) / 2
    bottom = (height + 2160) / 2
    final_image = final_image.crop((left, top, right, bottom))

    # Increase the resolution of the final image to 300 ppi
    final_image = final_image.resize((3840, 2160), resample=Image.LANCZOS)
    final_image.info['dpi'] = (300, 300)

    # Save the final image
    final_image.save("final_image.png", dpi=(300, 300))

if __name__ == "__main__":
    main()
