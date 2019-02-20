from PIL import Image
import os

picture_path = os.getcwd().replace('/codes', '/') + 'pictures/'
#~ print(picture_path)
code_path = os.getcwd()
#~ print(code_path)

picture_list = os.listdir(picture_path)
#~ print(picture_list)

"""
Image.open(file) ⇒ image 
Image.open(file, mode) ⇒ image

open(fp, mode='r')
    Opens and identifies the given image file.
    
    This is a lazy operation; this function identifies the file, but
    the file remains open and the actual image data is not read from
    the file until you try to process the data (or call the
    :py:meth:`~PIL.Image.Image.load` method).  See
    :py:func:`~PIL.Image.new`.
    
    :param fp: A filename (string), pathlib.Path object or a file object.
       The file object must implement :py:meth:`~file.read`,
       :py:meth:`~file.seek`, and :py:meth:`~file.tell` methods,
       and be opened in binary mode.
    :param mode: The mode.  If given, this argument must be "r".
    :returns: An :py:class:`~PIL.Image.Image` object.
    :exception IOError: If the file cannot be found, or the image cannot be
       opened and identified.

"""
im = Image.open(picture_path + picture_list[0], mode='r')

"""
# show some information about image

#~ im.format ⇒ string or None
#~ format: JPEG, PNG....

#~ im.mode ⇒ string
#~ modes	描述
#~ 1		1位像素，黑和白，存成8位的像素
#~ L		8位像素，黑白
#~ P		8位像素，使用调色板映射到任何其他模式
#~ RGB		3×8位像素，真彩
#~ RGBA		4×8位像素，真彩+透明通道
#~ CMYK		4×8位像素，颜色隔离
#~ YCbCr	3×8位像素，彩色视频格式
#~ I		32位整型像素
#~ F		32位浮点型像素

#~ im.size ⇒ (width, height)
#~ 图像的尺寸，按照像素数计算，它的返回值为宽度和高度的二元组（width, height）

#~ im.palette ⇒ palette or None
#~ 颜色调色板表格。如果图像的模式是“P”，则返回ImagePalette类的实例；否则，将为None。 
#~ 如下为对非“P”模式下的图像进行palette信息显示
"""
print(im.format, im.size, im.mode, im.palette)

"""
# convert the image to other modes and return a new image

#~ 当从一个颜色图像转换为黑白图像时，PIL库使用ITU-R601-2 luma转换公式：
#~ L = R * 299/1000 + G * 587/1000 + B * 114/1000
#~ 当转换为2位图像（模式“1”）时，源图像首先被转换为黑白图像。结果数据中大于127的值
#~ 被设置为白色，其他的设置为黑色；这样图像会出现抖动。如果要使用其他阈值，更改阈值127，
#~ 可以使用方法point()。为了去掉图像抖动现象，可以使用dither选项。
"""
new_im = im.convert('P')


# image show 
im.show()
new_im.show()

# you can save image corespoding to the format, 
#~ im.save(outfile,options…) 
#~ im.save(outfile, format, options…)
#~ ----------------
im.save(picture_path + 'gakki2.png')

im = Image.open(picture_path + 'gakki2.png')

print(im.format, im.size, im.mode)

"""
Image.new(mode,size) ⇒ image 
Image.new(mode, size, color) ⇒ image

new(mode, size, color=0)
    Creates a new image with the given mode and size.
    
    :param mode: The mode to use for the new image. See:
       :ref:`concept-modes`.
    :param size: A 2-tuple, containing (width, height) in pixels.
    :param color: What color to use for the image.  Default is black.
       If given, this should be a single integer or floating point value
       for single-band modes, and a tuple for multi-band modes (one value
       per band).  When creating RGB images, you can also use color
       strings as supported by the ImageColor module.  If the color is
       None, the image is not initialised.
    :returns: An :py:class:`~PIL.Image.Image` object.
"""
# open a red image
red_im1 = Image.new(im.mode, im.size, (255, 0, 0))
red_im1.show()

red_im2 = Image.new("RGB", (128, 128), "#FF0000")
red_im2.show()

red_im3 = Image.new("RGB", (128, 128), "red")
red_im3.show()

"""
 crop(self, box=None)
     Returns a rectangular region from this image. The box is a
     4-tuple defining the left, upper, right, and lower pixel
     coordinate.
      
     Note: Prior to Pillow 3.4.0, this was a lazy operation.
      
     :param box: The crop rectangle, as a (left, upper, right, lower)-tuple.
     :rtype: :py:class:`~PIL.Image.Image`
     :returns: An :py:class:`~PIL.Image.Image` object.
""" 
##确定拷贝区域大小
box = (300, 100, 700, 700) 
##将im表示的图片对象拷贝到region中，大小为box            
region = im.crop(box)                  
region.show()
