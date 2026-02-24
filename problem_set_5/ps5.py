"""
# Problem Set 5
# Name:
# Collaborators:
"""

from PIL import Image, ImageFont, ImageDraw
import numpy


def make_matrix(color):
    """
    Generates a transformation matrix for the specified color.
    Inputs:
        color: string with exactly one of the following values:
               'red', 'blue', 'green', or 'none'
    Returns:
        matrix: a transformation matrix corresponding to
                deficiency in that color
    """
    # You do not need to understand exactly how this function works.
    if color == 'red':
        c = [[.567, .433, 0], [.558, .442, 0], [0, .242, .758]]
    elif color == 'green':
        c = [[0.625, 0.375, 0], [0.7, 0.3, 0], [0, 0.142, 0.858]]
    elif color == 'blue':
        c = [[.95, 0.05, 0], [0, 0.433, 0.567], [0, 0.475, .525]]
    elif color == 'none':
        c = [[1, 0., 0], [0, 1, 0.], [0, 0., 1]]
    return c


def matrix_multiply(m1, m2):
    """
    Multiplies the input matrices.
    Inputs:
        m1,m2: the input matrices
    Returns:
        result: matrix product of m1 and m2
        in a list of floats
    """

    product = numpy.matmul(m1, m2)
    if type(product) == numpy.int64:
        return float(product)
    else:
        result = list(product)
        return result


def img_to_pix(filename):
    """
    Takes a filename (must be inputted as a string
    with proper file attachment ex: .jpg, .png)
    and converts to a list of representing pixels.

    For RGB images, each pixel is a tuple containing (R,G,B) values.
    For BW images, each pixel is an integer.

    # Note: Don't worry about determining if an image is RGB or BW.
            The PIL library functions you use will return the 
            correct pixel values for either image mode.

    Returns the list of pixels.

    Inputs:
        filename: string representing an image file, such as 'lenna.jpg'
        returns: list of pixel values 
                 in form (R,G,B) such as [(0,0,0),(255,255,255),(38,29,58)...] for RGB image
                 in form L such as [60,66,72...] for BW image
    
    -----------------------------------------------------------------
    
    接收一个文件名（必须作为带有正确文件扩展名的字符串输入，例如：.jpg, .png），
    并将其转换为表示像素的列表。

    对于 RGB 图像，每个像素是一个包含 (R,G,B) 值的元组。
    对于黑白 (BW) 图像，每个像素是一个整数。

    # 注意：不必担心如何判断图像是 RGB 还是 BW。
            你使用的 PIL 库函数会为任一图像模式返回
            正确的像素值。

    返回像素列表。

    输入：
        filename: 表示图像文件的字符串，例如 'lenna.jpg'
    返回：
        像素值列表 
                 对于 RGB 图像，格式为 (R,G,B)，例如 [(0,0,0),(255,255,255),(38,29,58)...]
                 对于黑白 (BW) 图像，格式为 L，例如 [60,66,72...]
    """
    image_1 = Image.open(filename)
    list_1 = list(image_1.getdata())
    return list_1

def pix_to_img(pixels_list, size, mode):
    """
    Creates an Image object from a inputted set of RGB tuples.

    Inputs:
        pixels_list: a list of pixels such as the output of
                img_to_pixels.
        size: a tuple of (width,height) representing
              the dimensions of the desired image. Assume
              that size is a valid input such that
              size[0] * size[1] == len(pixels).
        mode: 'RGB' or 'L' to indicate an RGB image or a 
              BW image, respectively
    returns:
        img: Image object made from list of pixels
        
    ------------------------------------------------------------------
    
    从输入的一组 RGB 元组创建 Image 对象。

    输入：
        pixels_list: 一个像素列表，例如 img_to_pixels 的输出结果。
        size: 一个表示所需图像尺寸的 (宽, 高) 元组。假设 size 
              是一个有效的输入，满足 size[0] * size[1] == len(pixels)。
        mode: 'RGB' 或 'L'，分别用来指示 RGB 图像或黑白 (BW) 图像。
    返回：
        img: 由像素列表生成的 Image 对象。
    """
    image_1 = Image.new(mode,size)
    image_1.putdata(pixels_list)
    return image_1

def filter(pixels_list, color):
    """
    pixels_list: a list of pixels in RGB form, such as
            [(0,0,0),(255,255,255),(38,29,58)...]
    color: 'red', 'blue', 'green', or 'none', must be a string representing 
           the color deficiency that is being simulated.
    returns: list of pixels in same format as earlier functions,
    transformed by matrix multiplication
    
    ------------------------------------------------------------------
    
    pixels_list: RGB 形式的像素列表，例如
            [(0,0,0),(255,255,255),(38,29,58)...]
    color: 'red'、'blue'、'green' 或 'none'，必须是一个表示
           正在模拟的颜色缺陷的字符串。
    returns: 格式与之前函数相同的像素列表，
    已通过矩阵乘法进行变换
    """
    list_float = []
    for l1 in pixels_list:
        l2 = matrix_multiply(make_matrix(color),l1)
        list_float.append(l2)
    list_int = []
    for t1 in list_float:
        l3= tuple(int(x) for x in t1)
        list_int.append(l3)
    return list_int


def extract_end_bits(num_end_bits, pixel):
    """
    Extracts the last num_end_bits of each value of a given pixel.

    example for BW pixel:
        num_end_bits = 5
        pixel = 214

        214 in binary is 11010110. 
        The last 5 bits of 11010110 are 10110.
                              ^^^^^
        The integer representation of 10110 is 22, so we return 22.

    example for RBG pixel:
        num_end_bits = 2
        pixel = (214, 17, 8)

        last 3 bits of 214 = 110 --> 6
        last 3 bits of 17 = 001 --> 1
        last 3 bits of 8 = 000 --> 0

        so we return (6,1,0)

    Inputs:
        num_end_bits: the number of end bits to extract
        pixel: an integer between 0 and 255, or a tuple of RGB values between 0 and 255

    Returns:
        The num_end_bits of pixel, as an integer (BW) or tuple of integers (RGB).
    -------------------------------------------------------------------
    
    提取给定像素每个值的最后 num_end_bits（末尾几位）位。

    黑白（BW）像素示例：
        num_end_bits = 5
        pixel = 214

        214 的二进制是 11010110。 
        11010110 的最后 5 位是 10110。
                              ^^^^^
        10110 转换回整数是 22，所以我们返回 22。

    RGB 像素示例：
        num_end_bits = 2  （注：原注释此处为2，但下方计算演示的是提取3位的过程）
        pixel = (214, 17, 8)

        214 的最后 3 位 = 110 --> 6
        17 的最后 3 位 = 001 --> 1
        8 的最后 3 位 = 000 --> 0

        所以我们返回 (6, 1, 0)

    输入 (Inputs)：
        num_end_bits: 要提取的末尾位数
        pixel: 0 到 255 之间的一个整数，或者是一个包含 0 到 255 之间 RGB 值的元组

    返回 (Returns)：
        像素的最后 num_end_bits 位，以整数（针对黑白像素）或整数元组（针对 RGB 像素）的形式返回。
    """
    if type(pixel) != int:
        return tuple(x % (2 ** num_end_bits) for x in pixel)
    else:
        return pixel % (2 ** num_end_bits)


def reveal_bw_image(filename):
    """
    Extracts the single LSB for each pixel in the BW input image. 
    Inputs:
        filename: string, input BW file to be processed
    Returns:
        result: an Image object containing the hidden image
        
    提取输入的黑白（BW）图像中每个像素的最低有效位（LSB，Least Significant Bit）。
    
    输入 (Inputs)：
        filename: 字符串，要处理的输入黑白图像文件名
        
    返回 (Returns)：
        result: 一个包含隐藏图像的 Image 对象
    """
    str_pix = img_to_pix(filename)
    str_ext = []
    for s in str_pix:
        n = extract_end_bits(1,s)
        str_ext.append(n * 255)
    return pix_to_img(str_ext,Image.open(filename).size,'L')
    


def reveal_color_image(filename):
    """
    Extracts the 3 LSBs for each pixel in the RGB input image. 
    Inputs:
        filename: string, input RGB file to be processed
    Returns:
        result: an Image object containing the hidden image
    -------------------------------------------------------------------
    提取输入的 RGB 图像中每个像素的 3 个最低有效位 (LSB)。 
    输入：
        filename: 字符串，要处理的输入 RGB 文件
    返回：
        result: 包含隐藏图像的 Image 对象
    """
    list_1 = img_to_pix(filename)
    list_2 = []
    for i in list_1:
        list_2.append(tuple(int(x * 255 / 7) for x in extract_end_bits(3, i)))
    return pix_to_img(list_2, Image.open(filename).size, 'RGB')


def reveal_image(filename):
    """
    Extracts the single LSB (for a BW image) or the 3 LSBs (for a 
    color image) for each pixel in the input image. Hint: you can
    use a function to determine the mode of the input image (BW or
    RGB) and then use this mode to determine how to process the image.
    Inputs:
        filename: string, input BW or RGB file to be processed
    Returns:
        result: an Image object containing the hidden image
    -----------------------------------------------------------------
    提取输入图像中每个像素的单个最低有效位 (LSB)（针对黑白图像）或 3 个最低有效位 (LSB)（针对彩色图像）。
    提示：你可以使用一个函数来确定输入图像的模式（黑白或 RGB），然后使用该模式来决定如何处理图像。
    输入：
        filename: 字符串，要处理的输入黑白 (BW) 或 RGB 文件
    返回：
        result: 包含隐藏图像的 Image 对象
    """
    im = Image.open(filename)
    if im.mode == '1' or im.mode == 'L':
        return(reveal_bw_image(filename))
    elif im.mode == 'RGB':
        return(reveal_color_image(filename))
    else:
        raise Exception("Invalid mode %s" % im.mode)


def draw_kerb(filename, kerb):
    """
    Draws the text "kerb" onto the image located at "filename" and returns a PDF.
    Inputs:
        filename: string, input BW or RGB file
        kerb: string, your kerberos
    Output:
        Saves output image to "filename_kerb.xxx"
        -----------------------------------------------------------
        将文本 "kerb" 绘制到位于 "filename" 的图像上并返回一个 PDF。
    输入：
        filename: 字符串，输入的黑白或 RGB 文件
        kerb: 字符串，你的 kerberos 标识
    输出：
        将输出的图像保存为 "filename_kerb.xxx"
    """
    im = Image.open(filename)
    font = ImageFont.truetype("noto-sans-mono.ttf", 40)
    draw = ImageDraw.Draw(im)
    draw.text((0, 0), kerb, "white", font=font)
    idx = filename.find(".")
    new_filename = filename[:idx] + "_kerb" + filename[idx:]
    im.save(new_filename)
    return


def main():
    pass

    # Uncomment the following lines to test part 1

    # im = Image.open('image_15.png')
    # width, height = im.size
    # pixels = img_to_pix('image_15.png')

    # non_filtered_pixels = filter(pixels,'none')
    # im = pix_to_img(non_filtered_pixels, (width, height), 'RGB')
    # im.show()

    # red_filtered_pixels = filter(pixels,'red')
    # im2 = pix_to_img(red_filtered_pixels,(width,height), 'RGB')
    # im2.show()

    # # Uncomment the following lines to test part 2
    # im = reveal_image('hidden1.bmp')
    # im.show()

    # im2 = reveal_image('hidden2.bmp')
    # im2.show()
    

if __name__ == '__main__':
    main()
