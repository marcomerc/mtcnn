#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
from mtcnn.mtcnn import MTCNN
import time

detector = MTCNN()

image = cv2.imread("test1.jpg")
start = time.time()
result = detector.detect_faces(image)
end = time.time()
print (end - start)
print("test")
# Result is an array with all the bounding boxes detected. We know that for 'ivan.jpg' there is only one.
print (result)


for detection in result:
    bounding_box = detection['box']
    keypoints = detection['keypoints']
    cv2.rectangle(image,
                  (bounding_box[0], bounding_box[1]),
                  (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
                  (0,155,255),
                  2)
    cv2.circle(image,(keypoints['left_eye']), 2, (0,155,255), 2)
    cv2.circle(image,(keypoints['right_eye']), 2, (0,155,255), 2)
    cv2.circle(image,(keypoints['nose']), 2, (0,155,255), 2)
    cv2.circle(image,(keypoints['mouth_left']), 2, (0,155,255), 2)
    cv2.circle(image,(keypoints['mouth_right']), 2, (0,155,255), 2)

cv2.imwrite("result.jpg", image)

print(result)
