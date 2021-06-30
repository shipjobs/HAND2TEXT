# -*- coding: utf-8 -*-
######################################################################
#  Open CV 기능 구현 
#  1. 구현 기능
#     - 문제지 vs 정답지 분리
#     - 이미지로 부터 글자 영역 추출
#  2. Python Open CV 
#     - Document 
#       : https://blog.naver.com/PostView.nhn?blogId=monkey5255&logNo=221598376164&from=search&redirect=Log&widgetTypeCall=true&directAccess=false
######################################################################
import cv2


# 문제지와 정답지를 분리하여 정답만 인식 될수 있도록
def convert_correct_image_for_OCR(img_path , img_w_path):
    
    img_source = cv2.imread(fname , 0)

    ret,img_result1 = cv2.threshold(img_source, 127, 255, cv2.THRESH_BINARY) #  배경 문제 지문 vs 답안 지문 분리 (가장 높은 인식률값)
    ret, img_result2 = cv2.threshold(img_source, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU) 
    
    img_blur = cv2.GaussianBlur(img_source, (5,5), 0)
    ret, img_result3 = cv2.threshold(img_blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    cv2.imshow("SOURCE", img_source)
    cv2.imshow("THRESH_BINARY", img_result1)  #  배경 문제 지문 vs 답안 지문 분리 (OCR 인식 결과가 가장 좋은 값 찾기)
    cv2.imshow("THRESH_OTSU", img_result2)  
    cv2.imshow("THRESH_OTSU + Gaussian filtering", img_result3)

    cv2.imwrite('org', img_w_path)  #변환이미지 저장

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 한글자씩 찾기   (단어집 )

# bounding box 좌표

# 이미지, 결과, 저장 
        

# TEST    
#######################################################################################
fname = "C:\\Mydata_correct\\correct_root\\K-007.png"
fwname = "C:\\Mydata_correct\\correct_root\\K-007_gray.png"
#######################################################################################
#
#

convert_correct_image_for_OCR(fname , fwname)
