import sys
import numpy as np
import cv2 as cv
import os


def viewImage(image):
    cv.namedWindow('Display', cv.WINDOW_NORMAL)
    cv.imshow('Display', image)
    cv.waitKey(0)
    cv.destroyAllWindows()


color_to_seek = (100, 100, 100)
main_dir = os.path.split(os.path.abspath(__file__))[0]
file_name = '2.png'
original = cv.imread(os.path.join(main_dir, file_name))
amount = 0
for x in range(original.shape[0]):
    for y in range(original.shape[1]):
        b, g, r = original[x, y]
        if (b, g, r) < color_to_seek:
            amount += 1
print(amount)  # площадь
###################################################################################################
image = cv.imread('example1.tif')
hsv_min = np.array([0, 0, 128])#это получается средний серый в HSV
hsv_max = np.array([0, 0, 0])#это вообще конкретно черный
hsv_img = cv.cvtColor(image, cv.COLOR_BGR2HSV)#переводим картинку в HSV, и она красная??
#viewImage(hsv_img)
thresh = cv.inRange(hsv_img, hsv_min, hsv_max)
hsv_img[thresh > 0] = ([0, 0, 200])#тут небольшая корректировка но она все равно красная!
viewImage(hsv_img)
RGB_again = cv.cvtColor(hsv_img, cv.COLOR_HSV2RGB)#обратно в ргб
gray = cv.cvtColor(RGB_again, cv.COLOR_RGB2GRAY)#делаем ее СЕРОЙ
viewImage(gray)#она серая
ret, threshold = cv.threshold(gray, 90, 255, cv.THRESH_BINARY)#фильтруем серый то что меньше 90 черный больше белый
viewImage(threshold)
contours, hierarchy = cv.findContours(threshold.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)#находим контуры по фильтрованной картинке
#contours, hierarchy = cv.findContours(threshold, cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)
cv.drawContours(image, contours, -1, (0, 0, 255), 3, cv.LINE_AA, hierarchy)#рисуем контуры
viewImage(image)  # 5 Конечный контур

# print(hierarchy)
###################################################################################################

fn = 'photo3.jpg'
img = cv.imread(fn)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
hsv_min = np.array((0, 0, 0), np.uint8)
hsv_max = np.array((138, 138, 138), np.uint8)

thresh = cv.inRange(hsv, hsv_min, hsv_max)
contours0, hierarchy = cv.findContours(thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# index = 0
# layer = 0
#
#
# def update():
#     vis = img.copy()
#     cv.drawContours(vis, contours0, index, (255, 255, 255), 3, cv.LINE_AA, hierarchy, layer)
#
#     cv.imshow('contours', vis)
#
#
# def update_index(v):
#     global index
#     index = v - 1
#     update()
#
#
# def update_layer(v):
#     global layer
#     layer = v
#     update()
#
# update_index(0)
# update_layer(0)
# cv.createTrackbar("contour", "contours", 0, 7, update_index)
# cv.createTrackbar("layers", "contours", 0, 7, update_layer)
#
# cv.waitKey()
# cv.destroyAllWindows()

def findGreatesContour(contours):
    largest_area = 0
    largest_contour_index = -1
    i = 0
    total_contours = len(contours)

    while i < total_contours:
        area = cv.contourArea(contours[i])
        if area > largest_area:
            largest_area = area
            largest_contour_index = i
        i += 1

    return largest_area, largest_contour_index


largest_area, largest_contour_index = findGreatesContour(contours)

print(largest_contour_index)
print(len(contours))
print(len(contours[largest_contour_index]))
