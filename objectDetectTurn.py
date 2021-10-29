import cv2

classNames = []
classFile = "coco.names"
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')
print(classNames)

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

cap = cv2.VideoCapture(0) #"home.mp4")

while True:
    success, img = cap.read()

    detectperson = 0;
    leftright = 0;

    height = 600  # height in pixels
    width = int(height * (img.shape[1] / img.shape[0]))
    dim = (width, height)

    # resize image
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    classIds, confs, bbox = net.detect(img, confThreshold=0.5)
    print(classIds, bbox)

    if len(classIds) > 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            cv2.rectangle(img, box, color=(255, 0, 255), thickness=3)

            cv2.putText(img, classNames[classId - 1], (box[0] + 10, box[1] + 30),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0), 3)

            if classNames[classId - 1] == 'person':
                detectperson = 1;
                if box[0]+box[2]/2 > width/2 :
                    leftright = 1 #right
                elif box[0]+box[2]/2 < width/2 :
                    leftright = -1 #left
                else:
                    leftright = 0 #no turning

    print(detectperson, leftright)

    cv2.imshow("output", img)
    cv2.waitKey(33)