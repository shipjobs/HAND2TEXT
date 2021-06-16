from PIL import Image

# file_output_path = 'C:\\Mydata\\svg2png\\'  #$png 변환
# img = Image.open( file_output_path + "0.png")

# # area = (x1, y1, x2, y2)
# cropping_area = (441,374,518,411)   #좌표 지정
# cropped_img = img.crop(cropping_area)
# cropped_img.save('C:\\Mydata\\word_root\\0png_1.png')
#참조 :  https://blog.naver.com/khw11044/222003896258


# dic_bounding_lt_rb = 좌상, 우하 [{'x': 556.0, 'y': 343.0}, {'x': 556.0, 'y': 343.0}]
def save_text_boundingbox_from_png( source_image_url ,dic_bounding_lt_rb :dict , file_output_folder_path , file_name ):

    img = Image.open( source_image_url )  #text 값을 파일명으로

    # area = (x1, y1, x2, y2)
    #cropping_area = (441,374,518,411)   #좌표 지정
    #cropping_area = ( dic_bounding_lt_rb[0] ,374,518,411)   #좌표 지정
    cropping_area = ( dic_bounding_lt_rb[0]['x'],
                    dic_bounding_lt_rb[0]['y'],
                    dic_bounding_lt_rb[1]['x'],
                    dic_bounding_lt_rb[1]['y'])                    
    
    cropped_img = img.crop(cropping_area)
    cropped_img.save("C:\\Mydata\\word_root\\" + file_name + ".png")

from json_Ctrl import *

dic_bounding_lt_rb = []
dic_bounding_lt_rb = get_vertices_list_from_json("./sample_data/sample.json" )

source_image_url        = "C:\\Mydata\\svg2png\\0.png"
file_output_folder_path = "C:\\Mydata\\word_root\\"   

# png 이미지 경로 , 텍스트 영역 좌표 ,  저장 경로, 저장_파일명 (텍스트 이름으로 저장) 


for index_cnt , vertices in enumerate( dic_bounding_lt_rb ) :
    #save_text_boundingbox_from_png( source_image_url , dic_bounding_lt_rb[0]  , file_output_folder_path , "HELLO_WORLD0")
    save_text_boundingbox_from_png( source_image_url , vertices   , file_output_folder_path , str(index_cnt)) 
