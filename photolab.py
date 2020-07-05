""" 
File name: photolab.py
Author username(s): denneyen, jaltarnr
Date: 11/9/2017
"""
import image

def negative(img):
    '''
    Creates and returns a negative copy of an image.
    
    Parameters:
    img: an image object
    
    Preconditions: img is an image object
    
    Postconditions/Return Values: returns a negative copy of an image.
    '''
    assert isinstance(img, image.Image), 'img must be an Image object.'
    
def scale(img, f):
    '''
    Creates and returns a scaled copy of an image.
    
    Parameters:
    img: an image object
    f: a float object
    
    Preconditions:
    img is an image object
    f is a positive float
    
    Postconditions/Return Values: returns a scaled copy of an image.
    '''
    assert isinstance(img, image.Image), 'img must be an Image object.'
    assert isinstance(f, float), 'f must be a float.'
    assert (f > 0), 'f must be a positive float.'
    
def average(img, row, column):
    offsets = [(-1, -1), (-1, 0), (0, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    rows = img.height()
    columns = img.width()
    count = 0
    tot_red = 0
    tot_green = 0
    tot_blue = 0
    for offset in offsets:
        new_row = row + offset[0]
        new_column = column + offset[1]
        if (new_row >= 0 and new_row < rows) and (new_column >= 0 and new_column < columns):
            count = count + 1
            clr = img.get(new_row, new_column)
            tot_red = tot_red + clr[0]
            tot_green = tot_green + clr[1]
            tot_blue = tot_blue + clr[2]
            avg_red = tot_red // count
            avg_green = tot_green // count
            avg_blue = tot_blue // count
            new_color = (avg_red, avg_green, avg_blue)
    return new_color
    

def blur(img):
    '''
    Creates and returns a blurred copy of an image.

    Preconditions:
    img is an image object

    Postconditions/Return Value: returns a blurred copy of the original image.
    '''
    assert isinstance(img, image.Image), 'img must be an Image object.'

    imgcp = image.Image(img.width(), img.height(), title='Copied Image')
    count = 0
    for r in range(img.height()):
        for c in range(img.width()):
            image_blur = average(img, r, c)
            imgcp.set(c, r, image_blur)
    return imgcp

def main():
    '''
    Displays an image and the subsequent changes to the image from the functions negative(img), scale(img, f), and blur(img)
    
    Parameters: None
    
    Preconditions:
    img1 must be an image object
    img2 must be an image object
    img3 must be an image object
    img4 must be an image object
    
    Postconditions/Return Vale: None
    '''
    img1 = image.Image(file='piechart.gif')
    assert isinstance(img1, image.Image), 'img1 must be an Image object.'
    img1.show()

    #img2 = negative(img1)
    #assert isinstance(img2, image.Image), 'img2 must be an Image object.'
    #img2.show()

    #img3 = scale(img1)
    #assert isinstance(img3, image.Image), 'img3 must be an Image object.'
    #img3.show()
    
    img4 = blur(img1)
    assert isinstance(img4, image.Image), 'img4 must be an Image object.'
    img4.show()

    image.mainloop()

if __name__ == '__main__':
    main()

