import cv2

img = cv2.imread("opera_house.jpg")

cv2.imshow("Output", img)

height, width = img.shape[0:2]

print(img.shape[0:2])

rotationMatrix = cv2.getRotationMatrix2D((width/2, height/2), 90, .5)

rotatedImage = cv2.warpAffine(img, rotationMatrix, (width, height))

cv2.imshow("Rotated Image", rotatedImage)



startRow = int(height*0.15)

startCol = int(width*0.15)

endRow = int(height*0.85)

endCol = int(width*0.85)

croppedImage = img[startRow:endRow, startCol:endCol]

cv2.imshow("Cropped Image", croppedImage)



rotationMatrix60 = cv2.getRotationMatrix2D((width/2, height/2), 60, .5)

imgrot60 = rotatedImage60 = cv2.warpAffine(img, rotationMatrix60, (width, height))

resizedImage = cv2.resize(imgrot60, (int(width*0.8), int(height*0.8)))

cv2.imshow("Resized Image", resizedImage)



edge_img = cv2.Canny(img, 100, 200)

cv2.imshow("Detected Edges", edge_img)

img_grey = cv2.imread("triangle_wallpaper.jpg", cv2.IMREAD_GRAYSCALE)

thresh = 120

img_binary = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)[1]

cv2.imwrite("triangle_wallpaper_bw.jpg", img_binary)

cv2.imshow("b&w", img_binary)



tri2 = cv2.imread("triangle_2.png")

tri2gray = cv2.cvtColor(tri2, cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(tri2gray, 30, 200)

conts, heirarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

tri2Cont = cv2.drawContours(tri2, conts, -1, (0, 255, 0), 3)

cv2.imshow("Tri2+Conts", tri2Cont)

tribw = cv2.imread("triangle_wallpaper_bw.jpg")

triEdge = cv2.Canny(tribw, 30, 200)

triconts, heirarchy = cv2.findContours(triEdge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

tricont = cv2.drawContours(tribw, triconts, -1, (0, 255, 0), 3)

cv2.imshow("Tri+Conts", tricont)

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    cv2.imshow("Output", img)
    cv2.waitKey(0)

cv2.waitKey()

cv2.destroyAllWindows()