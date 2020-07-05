
import image

def copy_image(img):
    '''
    Creates a copy of an image by iterating over the height and width and copying
    each pixel to a new image. 

    Preconditions:
        img is an image object

    Postconditions:
        return a copy of that image object
    '''
    assert isinstance(img, image.Image), 'img must be an Image object.'

    imgcp = image.Image(img.width(), img.height(), title='Copied Image')
    for r in range(img.height()):
        for c in range(img.width()):
            pixclr = img.get(c, r)
            imgcp.set(c, r, pixclr)
    return imgcp

def gray_copy(img):
    '''
    For now, this is just the same code that is in copy_image.
    Change it so that it returns a grayscale copy of the given image.
    '''
    imgcp = image.Image(img.width(), img.height(), title='Copied Image')
    for r in range(img.height()):
        for c in range(img.width()):
            pixclr = img.get(c, r)
            rc = pixclr[0]
            bc = pixclr[1]
            gc = pixclr[2]
            ave = (rc + bc + gc)/3
            newclr = (ave,ave,ave)
            imgcp.set(c, r, newclr)
    return imgcp




def main():
    img1 = image.Image(file='piechart.gif')
    img1.show()

    img2 = copy_image(img1)
    img2.show()
    
    img3 = gray_copy(img2)
    img3.show()
    
    
    
    


    image.mainloop()

if __name__ == '__main__':
    main()