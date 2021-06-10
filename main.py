from myClass.json_Ctrl import *
from myClass.png2NBPOCR  import cSVG2JSON , png2NBPOCR  #나의 클래스 - NBP 연결용
from myClass.SVGurl2Png  import cHand_writing_confituration
import myClass.util as myutil

#from myClass.SVGurl2Png  import *

#from myClass.json_Ctrl  import add #myClass 패키지의 json_Ctrl 모듈  impot 변수, 함수, 클래스

###########################################################################
#작성자 : insung-lee
#작성일 : 2021-06-10
#목적 : 손글씨 자동 채점 프로젝트 개발을 이한 정답 영역 추출 및 텍스트화
#내  용 : Readme.md 참조
###########################################################################

#------------------------------------------------------------------------------------
# [1] 정의된 Excel 로부터 svg 서버 정보 얻어오기  
#------------------------------------------------------------------------------------
H2Wconfonfiguration = cHand_writing_confituration()

#손글씨 Excel 파일 보관 경로 (추후, web url로 변경...필요)
file_input_path = 'C:\\Mydata\\source\\'
file_save_path  = 'C:\\Mydata\\svg2png\\'
file_name       = '20210521_svg_url.xlsx'
#
Sheet_Excel_Data =  H2Wconfonfiguration.read_inforamtion_from_excel(file_input_path   ,  file_name)

#------------------------------------------------------------------------------------
# [2] svg - png 변환 하기   
# SVG 파일 URL 목록을 주면. 지정된 경로에 png 파일을 저장시키자
#------------------------------------------------------------------------------------
H2Wconfonfiguration.read_svg_from_URL_save_png( URLlist = Sheet_Excel_Data  , save_path =  file_save_path )

#------------------------------------------------------------------------------------
# [3] 저장된 png 이미지로 부터 NBP OCR Service 이용하기
#------------------------------------------------------------------------------------
#1. OCR 사용 정보
api_GW_url     = 'https://3a3d0f78582b4a09b6a0f243d3278715.apigw.ntruss.com/custom/v1/9243/0d0568b38429c576171f867783373a9c981dd0444cbb7854b50412b119d992d5/general'
secret_key     = 'T0RtWXVFTXh1dXBaZVRMalRsQ0R5cERIWGdEUldvaGQ='

#2. NBP OCR 정보 설정
#2-1. png2NBPOCR 내 Create_Json 데이터 클래스 생성.. 
png2NBPOCR = png2NBPOCR( api_GW_url ,  secret_key)

dir = "C:\\Mydata\\svg2png\\"
#3. 경로내 파일 목록 가져오기 - (없으면 경로 생성은 나중에)
files_names = myutil.get_file_list_derectory( dir )

#4. 얻어온 파일목록 -> 기록 (png 파일명, png 파일경로)
# 4-1. dir 파일 경로, 파일명 집합
dataClass_Svg2Json = cSVG2JSON()  
dataClass_Svg2Json = png2NBPOCR.create_image_infom( dir , files_names )

#5. "dataClass_Svg2Json"  정보로
#5-1 "소스 파일명, 파일 이미지 경로, json 파일명, 생성된 json 파일 저장 경로" 파일 생성     
dataClass_Svg2Json = png2NBPOCR.get_json_from_OCR( png2NBPOCR.dataClass_Svg2Json )
