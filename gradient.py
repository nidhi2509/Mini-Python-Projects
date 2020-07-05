#Filename: gradient.py
#Author: jaltarnr
#date: 11/16/2017


import image

def gradient(color):
    '''
    This code creates an image that's fading to black from top to bottom with dimensions 200x200. 
    Parameters: A tuple of color values.
    Returns the new image.
    '''
    imgcp = image.Image(200, 200, title='Copied Image')
    for r in range(200):
        for c in range(200):
            
            newclr = (((200-r)*color[0])//200,((200-r)*color[1])//200,((200-r)*color[2])//200)
            imgcp.set(c, r, newclr)
    return imgcp




def main():
    img1 = gradient((20,250,20))
    img1.show()
    
    image.mainloop()

if __name__ == '__main__':
    main()