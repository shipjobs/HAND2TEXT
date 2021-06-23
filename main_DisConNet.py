from myClass.json_Ctrl import *
from myClass.Image_Ctrl import *

from myClass.png2NBPOCR  import cSVG2JSON , png2NBPOCR  #나의 클래스 - NBP 연결용
from myClass.SVGurl2Png  import cHand_writing_confituration
import myClass.util as myutil


###########################################################################
# 작 성자 : insung-lee
# 작 성일 : 2021-06-10
# 파 일명 : main_DisConNet.py
# 목   적 : 손글씨 자동 채점 프로젝트 개발을 이한 정답 영역 추출 및 텍스트화
# 내   용 : Readme.md 참조
# 특이사항: 네크웍이 연결 되지 않는 경우를 고려한, main
#   - 기존 확보된 json 파일들의 정보를 기준으로 텍스트 인식 작업 수행
###########################################################################


#------------------------------------------------------------------------------------
# [1] 정의된 Excel 로부터 svg 서버 정보 얻어오기  
#------------------------------------------------------------------------------------
H2Wconfonfiguration = cHand_writing_confituration()

#손글씨 Excel 파일 보관 경로 (추후, web url로 변경...필요)
file_input_path = 'C:\\Mydata\\source\\'
file_save_path  = 'C:\\Mydata\\svg2png\\'
file_json_path  = "C:\\Mydata\\json\\"

file_name       = '20210521_svg_url.xlsx'  #전체 800개 svg url
file_name       = 'svg_url_test.xlsx'      #개발용 약  5 ~ 10개


file_output_folder_path = "C:\\Mydata\\word_root\\"  

#로컬의 Json 파일 목록 읽어오기
read_jsons = myutil.read_json_list_from_Mydir(file_json_path)

#Json 파일
dic_bounding_lt_rb = []  #이미지 텍스트 좌표 데이터

for json_path in read_jsons:
    dic_bounding_lt_rb = get_vertices_list_from_json(json_path)
    
    #'C:\\Mydata\\json\\0.png.json' 와 매칭되는 이미지 파일명 가져오기 
    image_name = json_path.split('\\')[3].split('.')[0:2]    
    image_name = image_name[0] + "." + image_name[1]
    source_image_url        = "C:\\Mydata\\svg2png\\" + image_name  #잘라낼 소스 이미지 URL + 파일명    
    #파일 존재 여부 확인, 존재 하는 경우만 자르기
    
    for index_cnt , vertices in enumerate( dic_bounding_lt_rb ) :
        try:
            cropped_img , file_name = save_text_boundingbox_from_png( source_image_url , vertices   , file_output_folder_path , image_name )   
            
            print("[ ", index_cnt , " ]",  cropped_img.size )
            
            if( cropped_img.size[0] != 0 and cropped_img.size[1] != 0 ):                                   
                cropped_img.save( file_output_folder_path + file_name + ".png")  #파일명 : 텍스트_부모파일명 * 부모파일은 참조용

        except AttributeError as e:
            print("for json_path in read_jsons :  AttributeError [ " , e , " ] \n")
            
        except OSError as e:
            print("for json_path in read_jsons :  OSError [ " , e , " ] \n")


#https://dsc-sookmyung.tistory.com/29  #이미지내 문자 인식
