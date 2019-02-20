from PIL import Image
from PIL import ImageFilter 
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

im2 = Image.open(picture_path + 'gakki2.png')

print(im2.format, im2.size, im2.mode)

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
box = (300, 100, 700, 550) 
##将im表示的图片对象拷贝到region中，大小为box            
region = im.crop(box)                  
region.show()

"""
     |  paste(self, im, box=None, mask=None)
     |      Pastes another image into this image. The box argument is either
     |      a 2-tuple giving the upper left corner, a 4-tuple defining the
     |      left, upper, right, and lower pixel coordinate, or None (same as
     |      (0, 0)).  If a 4-tuple is given, the size of the pasted image
     |      must match the size of the region.
     |      
     |      If the modes don't match, the pasted image is converted to the mode of
     |      this image (see the :py:meth:`~PIL.Image.Image.convert` method for
     |      details).
     |      
     |      Instead of an image, the source can be a integer or tuple
     |      containing pixel values.  The method then fills the region
     |      with the given color.  When creating RGB images, you can
     |      also use color strings as supported by the ImageColor module.
     |      
     |      If a mask is given, this method updates only the regions
     |      indicated by the mask.  You can use either "1", "L" or "RGBA"
     |      images (in the latter case, the alpha band is used as mask).
     |      Where the mask is 255, the given image is copied as is.  Where
     |      the mask is 0, the current value is preserved.  Intermediate
     |      values will mix the two images together, including their alpha
     |      channels if they have them.
     |      
     |      See :py:meth:`~PIL.Image.Image.alpha_composite` if you want to
     |      combine images with respect to their alpha channels.
     |      
     |      :param im: Source image or pixel value (integer or tuple).
     |      :param box: An optional 4-tuple giving the region to paste into.
     |         If a 2-tuple is used instead, it's treated as the upper left
     |         corner.  If omitted or None, the source is pasted into the
     |         upper left corner.
     |      
     |         If an image is given as the second argument and there is no
     |         third, the box defaults to (0, 0), and the second argument
     |         is interpreted as a mask image.
     |      :param mask: An optional mask image.
"""
box= [300, 300, 400, 400]
im_crop = im.crop(box)
print(im_crop.size, im_crop.mode)
im.paste(im_crop, (100, 100))
im.paste(im_crop, (400, 400, 500, 500))
im.show()


"""
im.filter(filter) ⇒ image
     |  filter(self, filter)
     |      Filters this image using the given filter.  For a list of
     |      available filters, see the :py:mod:`~PIL.ImageFilter` module.
     |      
     |      :param filter: Filter kernel.
     |      :returns: An :py:class:`~PIL.Image.Image` object.
     
返回一个使用给定滤波器处理过的图像的拷贝。具体参考图像滤波在ImageFilter 模块的应用,
在该模块中，预先定义了很多增强滤波器，可以通过filter( )函数使用，预定义滤波器包括：
BLUR、CONTOUR、DETAIL、EDGE_ENHANCE、EDGE_ENHANCE_MORE、EMBOSS、
FIND_EDGES、SMOOTH、SMOOTH_MORE、SHARPEN。
其中BLUR就是均值滤波，CONTOUR找轮廓，FIND_EDGES边缘检测，使用该模块时，需先导入。

"""
##均值滤波
bluF = im2.filter(ImageFilter.BLUR)
##找轮廓        
conF = im2.filter(ImageFilter.CONTOUR)
##边缘检测
edgeF = im2.filter(ImageFilter.FIND_EDGES)

im2.show()
bluF.show()
conF.show()
edgeF.show()

"""
     |  resize(self, size, resample=0)
     |      Returns a resized copy of this image.
     |      
     |      :param size: The requested size in pixels, as a 2-tuple:
     |         (width, height).
     |      :param resample: An optional resampling filter.  This can be
     |         one of :py:attr:`PIL.Image.NEAREST`, :py:attr:`PIL.Image.BOX`,
     |         :py:attr:`PIL.Image.BILINEAR`, :py:attr:`PIL.Image.HAMMING`,
     |         :py:attr:`PIL.Image.BICUBIC` or :py:attr:`PIL.Image.LANCZOS`.
     |         If omitted, or if the image has mode "1" or "P", it is
     |         set :py:attr:`PIL.Image.NEAREST`.
     |         See: :ref:`concept-filters`.
     |      :returns: An :py:class:`~PIL.Image.Image` object.

"""
im_resize = im.resize((300, 300), resample=Image.BILINEAR)
im_resize.show()


"""
    blend(im1, im2, alpha)
        Creates a new image by interpolating between two input images, using
        a constant alpha.::
        
            out = image1 * (1.0 - alpha) + image2 * alpha
        
        :param im1: The first image.
        :param im2: The second image.  Must have the same mode and size as
           the first image.
        :param alpha: The interpolation alpha factor.  If alpha is 0.0, a
           copy of the first image is returned. If alpha is 1.0, a copy of
           the second image is returned. There are no restrictions on the
           alpha value. If necessary, the result is clipped to fit into
           the allowed output range.
        :returns: An :py:class:`~PIL.Image.Image` object.
        
使用给定的两张图像及透明度变量alpha，插值出一张新的图像。这两张图像必须有一样的尺寸和模式
"""
