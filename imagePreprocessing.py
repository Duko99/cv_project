import cv2

def edgeDetectCanny(im):
    t1 = 80
    t2 = 255

    img_cp = im.copy()

    # do Gaussian blur - helps prevent shrubbery being picked up by Canny
    img_cp = cv2.GaussianBlur(img_cp, (5,5), 0)

    # do Canny edge detection
    canny = cv2.Canny(img_cp, t1, t2)

    # apply Canny mask onto input image - lines are red channel as to prevent blending in
    # with background (mostly plants/trees)
    img_cp[canny != 0] = (0, 0, 255)
    return img_cp

# perform image equalization
def equalizeImage(im):
    im_hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    im_hsv[:,:,2] = cv2.equalizeHist(im_hsv[:,:,2])
    im_eq = cv2.cvtColor(im_hsv, cv2.COLOR_HSV2RGB)
    return im_eq