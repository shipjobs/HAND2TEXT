###########################################################################
# 작성자 : insung-lee
# 작성일 : 2021-06-10
# 목  적 : 이미지 처리 모듈
# 활  용 lib : 
#  - Pillow : https://pillow.readthedocs.io/en/stable/
#  - OpenCV : https://docs.opencv.org/master/ 
#  - PIL : https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
#  - Scikit-image : https://scikit-image.org/docs/stable/index.html 
###########################################################################

from PIL import Image


#PNG 파일에서 지정된 영역 잘라내서 저장 하기
# - source_image_url : 이미지 소스 URL
# - dic_bounding_lt_rb : 딕션어리 (텍스트 영역 좌표 모음)
# - file_output_folder_path : 저장하고자 하는 폴더 경로 URL 
# - parent_file_name : 잘나낸 파일의 부모 페이지 파일명
def save_text_boundingbox_from_png( source_image_url ,dic_bounding_lt_rb :dict , file_output_folder_path , parent_file_name ):

    img = Image.open( source_image_url )  #text 값을 파일명으로

    cropping_area = ( dic_bounding_lt_rb[0]['x'] - 15 ,
                    dic_bounding_lt_rb[0]['y'] - 15 ,
                    dic_bounding_lt_rb[1]['x']+ 15 ,
                    dic_bounding_lt_rb[1]['y']+ 15 )                    
    
    cropped_img = img.crop(cropping_area)
    
    file_name = dic_bounding_lt_rb[2] + "@" + parent_file_name  ##파일명 : 텍스트@부모파일명

    return cropped_img  , file_name   #잘라낸 이미지  , 파일명


####################################################
# 모듈 테스트 , 작업 영역
####################################################
# from json_Ctrl import *
# # 임시
# dic_bounding_lt_rb = [] 
# #dic_bounding_lt_rb (No, [좌상 좌표 , 우하 좌표, 텍스트])
# dic_bounding_lt_rb = get_vertices_list_from_json("./sample_data/sample.json" )

# image_name = "7.png"
# source_image_url        = "C:\\Mydata\\svg2png\\"   + image_name
# file_output_folder_path = "C:\\Mydata\\word_root\\"   


# # png 이미지 경로 , 텍스트 영역 좌표 ,  저장 경로, 저장_파일명 (텍스트 이름으로 저장) 
# for index_cnt , vertices in enumerate( dic_bounding_lt_rb ) :
#     cropped_img , file_name = save_text_boundingbox_from_png( source_image_url , vertices   , file_output_folder_path , image_name )   
#     cropped_img.save("C:\\Mydata\\word_root\\" + file_name + ".png")  #파일명 : 텍스트_부모파일명 * 부모파일은 참조용


