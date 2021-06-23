#기본적인 라이브러리 호출
import os
import pandas as pd       #Excel 라이브러리 가져오기

###########################################################################
#작성자 : insung-lee
#작성일 : 2021-06-10
#목적 : 프로젝트에 사용되는 재사용 가능한 함수를 별도로 분리하여.. 재사용
#내  용 : Readme.md 참조
###########################################################################

#지정된 경로에 존재하는 파일 목록 가져오게 하기
def get_file_list_derectory(dir = "C:\\Mydata\\svg2png\\"):
    
       
    return os.listdir(dir)         #폴더내 파일명 가져오기


#Excel 로 부터 SVG 파일을 읽어 온다.
def read_svglist_from_excel(self,  file_input_path  , file_name  ):
    
    #해당 경로가 없으면
    if not os.path.exists(file_input_path):
        os.makedirs(file_input_path)  #없으면 만든다.
    
    #파일 DRM 해제 필요
    file_source_url = file_input_path + file_name  #file_url = "20210521_svg_url.xlsx"  #경로 포맷 문제  & 

    #파일이 존재 하는 경우만
    if os.path.isfile(file_source_url) != True:
        exit()

    #손글씨 Excel 파일 포맷 맞추기
    #나중에.. 전체 데이터 확보 되면. 구조.. 변경 필요
    #
    read_data = pd.read_excel(file_source_url , engine="openpyxl" , sheet_name="Sheet1") 
    new_df = read_data.loc[ :,['과목코드','단계코드','진도번호','페이지구분코드','제출파일URL']] 
    #
    return read_data  #읽어온 데이터 반환


#Excel 로 부터 Json 파일 목록을 읽어 온다.
def read_json_list_from_Mydir(self,  file_input_path = "C:\\Mydata\\json\\"):
    
    
    #해당 경로가 없으면
    if not os.path.exists(file_input_path):
        os.makedirs(file_input_path)  #없으면 만든다.
    
    #svg 파일 목록 불러오기
    files_names = get_file_list_derectory( file_input_path )
    
    read_data = []
    
    for file_name in files_names:
        #파일 DRM 해제 필요
        file_json_url = file_input_path + file_name  #file_url = "20210521_svg_url.xlsx"  #경로 포맷 문제  & 

        #파일이 존재 하는 경우만
        if os.path.isfile(file_json_url) != True:
            exit()

        read_data.append( file_json_url  )
        #손글씨 Excel 파일 포맷 맞추기
        #나중에.. 전체 데이터 확보 되면. 구조.. 변경 필요
        #
        #read_data = pd.read_excel(file_source_url , engine="openpyxl" , sheet_name="Sheet1") 
        #new_df = read_data.loc[ :,['과목코드','단계코드','진도번호','페이지구분코드','제출파일URL']] 
    #
    return read_data  #읽어온 데이터 반환
