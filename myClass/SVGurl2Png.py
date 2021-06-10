import json
import os
from datetime import time #시간 벌기
import pandas as pd       #Excel 라이브러리 가져오기
import urllib.request     #HTTP 에러 처리
import requests


###############################################
# SVG 를 PNG 저장 하기위한 라이브러리들
import cairo
from svglib.svglib import svg2rlg 
import cairosvg

import time 
###########################################################################
#작성자 : insung-lee
#작성일 : 2021-06-10
#목적 : 손글씨 정보 구성하기
#내  용 : Readme.md 참조
###########################################################################
class cHand_writing_confituration:
    
    #Excel 파일 경로 넣어 주면, 손글씨.. 관리 규칙에 맞게 정보를 담는다.
    def __init__(self):
        pass
    
    #Excel 파일 경로 넣어 주면, 손글씨.. 관리 규칙에 맞게 정보를 담는다.
    #읽어올 파일의 DRM 이 해지 된지 확인하자.. 잊지 말자
    def read_inforamtion_from_excel(self,  file_input_path  , file_name  ):
        
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
        #        
        return read_data  #읽어온 데이터 반환
    
    
    
    #Excel 로 부터 읽어온 read_data 의  URLlist 
    def read_svg_from_URL_save_png(self,  URLlist  , save_path ='C:\\Mydata\\svg2png\\'):
        
        
        URLlist = URLlist        
        failcnt = 0  #실패 횟수 카운팅

        # 한줄씩 URL 에서 svg 파일을 읽어온다.
        # 웹특성.. 지연 및 진행 사항 체크를 위한 try 수행
        for cnt , row_svg_URL in enumerate(URLlist['제출파일URL']):
            
            file_save_path =  save_path  + str(cnt)  + '.png'
            try:
                cairosvg.svg2png(url= row_svg_URL , write_to = file_save_path  , background_color="white", dpi = 100) 
                file_save_path = ""
                
            except urllib.error.HTTPError as e:
                failcnt += 1
                print("HTTP error No: [" , str(failcnt), "]  [" , e.code , "] 5초 대기")
                time.sleep(5)  #import time
                
            except urllib.error.URLError as e:
                print("URL error No: [" , str(failcnt), "]  [" , e.code , "] 종료" )
                exit()
            else:
                failcnt += 1
                print("Other error No: [" , str(failcnt), "] 대기")
                time.sleep(5)
                
    
    