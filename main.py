# filename: main.py
# author(s): elia deppe
# date: 3/30/22
#
# description: program that generates an image that is a blocked gradient. must be ran from the terminal. the program
#              can take 3 command line arguments: two hex color codes followed by the number of blocks per vector.

# imports
from imagehash import average_hash
from random import randint
from PIL import Image, ImageDraw
import sys

SIZE = 1024


def create_image(img, start_color, end_color, blocks_per_vector):
    """
    :create_image: creates the image, based on the given colors and the number of blocks per vector.

    :param img:               Image  | the Image object that is being used to create a gradient
    :param start_color:       string | the starting color for the gradient
    :param end_color:         string | the ending color for the gradient
    :param blocks_per_vector: int    | number of blocks in a given row or columns
    :return:                  None
    """
    start_color = hex_to_int(start_color)
    end_color = hex_to_int(end_color)

    gradient = generate_gradient(start_color, end_color, blocks_per_vector)
    block_size = SIZE // blocks_per_vector

    draw = ImageDraw.Draw(img)
    for row in range(blocks_per_vector):
        for col in range(blocks_per_vector):
            current_block = col + row * blocks_per_vector
            x0, y0 = block_size * col, block_size * row
            x1, y1 = block_size * col + block_size, block_size * row + block_size

            draw.rectangle([x0, y0, x1, y1], fill=tuple(gradient[current_block]))


def hex_to_int(color):
    """
    :hex_to_int: converts a string hexadecimal rgb code to a tuple rgb code consisting or integer values for each
                 channel.

    :param color: string    | hex code for a color (does not include the hashtag)
    :return:      (r, g, b) | a tuple rgb code in integer form
    """
    return int(color[:2], 16), int(color[2:4], 16), int(color[4:], 16)


def generate_gradient(start_color, end_color, blocks_per_vector):
    total_steps = blocks_per_vector ** 2
    gradient = [[None for _ in range(3)] for _ in range(total_steps)]

    color = start_color
    step = 0

    for rgb_code in gradient:
        rgb_code[0], rgb_code[1], rgb_code[2] = color[0], color[1], color[2]

        step += 1
        r = lerp(start_color[0], end_color[0], step, total_steps)
        g = lerp(start_color[1], end_color[1], step, total_steps)
        b = lerp(start_color[2], end_color[2], step, total_steps)
        color = (r, g, b)

    return gradient


def generate_random_color():
    """
    :generate_random_color: generates a random color in the form of a tuple rgb code (integer form)

    description: generates a random rgb code for a color.
    :return: tuple(int, int, int) | rgb code
    """
    return (randint(0, 255) for _ in range(3))


def lerp(channel1, channel2, current_step, total_steps):
    """
    :lerp: linear interpolation function for traversing a gradient

    :param channel1:     int | the rgb channel for the starting color in the gradient.
    :param channel2:     int | the rgb channel for the ending color in the gradient.
    :param current_step: int | the current step (block) in the gradient.
    :param total_steps:  int | the total number of steps (blocks) in the gradient.
    :return:             int | the rgb channel value for the next color in the gradient.
    """
    return int(channel1 + (channel2 - channel1) * (current_step / total_steps))


def main(argv):
    """
    :main: generates a gradient image and then saves to the current directory, it's name set to an average_hash of the
           image.

    :param argv: [start_color, end_color, blocks_per_vector] | command line arguments for the program. start_color
                 start_color -->       string | hex code for the starting color excluding the #
                 end_color -->         string | hex code for the ending color excluding the #
                 blocks_per_vector --> string | number of blocks per vector (row or column)
    :return:     None
    """
    img = Image.new('RGBA', (SIZE, SIZE))
    create_image(img, argv[0], argv[1], int(argv[2]))
    img.save(f'./{average_hash(img)}.png')


if __name__ == '__main__':
    main(sys.argv[1:])
