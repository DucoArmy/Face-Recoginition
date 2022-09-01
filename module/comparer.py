from email.mime import image

import cv2 as cv
from sface import SFace
from yunet import YuNet

class Comparer:
    backend = [cv.dnn.DNN_BACKEND_OPENCV, cv.dnn.DNN_BACKEND_CUDA]
    target = [cv.dnn.DNN_TARGET_CPU, cv.dnn.DNN_TARGET_CUDA, cv.dnn.DNN_TARGET_CUDA_FP16]
    detectionModel = 'model/face_detection_yunet_2022mar.onnx'
    recognitionModel = 'model/face_recognition_sface_2021dec.onnx'
    dis_type = 0
    save = False
    vis = True

    undefined = "#UNDEFINED"
    success = "#SUCCESS"
    noMatch = "#NOMATCH"
    def __init__(self, standard):
        self.standard = standard

        self.detector = YuNet(modelPath=Comparer.detectionModel,
            inputSize=[320, 320],
            confThreshold=0.95,
            nmsThreshold=0.3,
            topK=5000,
            backendId=Comparer.backend[0],
            targetId=Comparer.target[0])

        self.recognizer = SFace(
            modelPath=Comparer.recognitionModel, 
            disType=Comparer.dis_type, 
            backendId=Comparer.backend[0], 
            targetId=Comparer.target[0])
        
        self.images = []
        for item in standard:
            image = cv.imread('./image/' + item + '.jpg')
            
            self.detector.setInputSize([image.shape[1], image.shape[0]])
            processed = self.detector.infer(image)
            self.images.append([
                image,
                processed
            ])


    def compare(self, target):
        img2 = target
        self.detector.setInputSize([img2.shape[1], img2.shape[0]])
        face2 = self.detector.infer(img2)

        try: 
            if face2.shape[0] <= 0: 
                return Comparer.undefined
        except:
            return Comparer.undefined

        result = []

        for idx, item in enumerate(self.images):
            res = self.recognizer.match(item[0], item[1][0][:-1], img2, face2[0][:-1])
            if res:
                return self.standard[idx]
        
        return Comparer.noMatch