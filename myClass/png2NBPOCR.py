from dataclasses import dataclass
import sys
import os
import hashlib
import hmac
import base64
from typing import Dict, List
import requests
import time

#import requests
import uuid
import time
import json

import pandas
from dataclasses import dataclass , field

###########################################################################
#작성자 : insung-lee
#작성일 : 2021-06-10
###########################################################################
# OCR 객체 사용 정보로 사용 하고자 합니다.
@dataclass(unsafe_hash=True)  
class cSVG2JSON: 
  id_page      = int  #문제 페이지 (key)
  img_source   = {} # 파일명 : png 경로  #  tag: List[str] = field(default_factory=list)
  fromNBP_json = {} # 파일명 : svg 경로  
  #XXXX Dict[str] = field(default_factory= Dict) 
 
#NAVER OCR Json - 데이터 전달 포맷 구조   
#-------------------------------------------------------------------------------
request_json = {
    'images': [
        {
            'format': 'png',
            'name': 'demo'
        }
    ],
    'requestId': str(uuid.uuid4()),
    'version': 'V2',
    'timestamp': int(round(time.time() * 1000))
}
payload = {'message': json.dumps(request_json).encode('UTF-8')}
      
###########################################################################
# png 파일이 주어지면 NBP OCR 서비스를 사용하여 Json 을 반환하는 Class
class png2NBPOCR:
    #
    def __init__(self, api_GW_url , secret_key ):                
        self.api_GW_url = api_GW_url
        self.secret_key = secret_key
        self.dataClass_Svg2Json = cSVG2JSON()  
        print( self.api_GW_url  , self.secret_key  , "\n" )
        

    #동작되는 pc 에 존재하는 image 파일과, 파일의 경로를 담아 둔다.
    # - 동작되는 PC 환경에 따른 이미지 소스 경로 문제 해결
    def create_image_infom(self, dir, file_names):    
        
        self.dir = dir
            
        for index , file in enumerate(file_names ):
            self.dataClass_Svg2Json.img_source[file]  = dir + file
            
        return self.dataClass_Svg2Json
    
    #저장된 png 이미지 경로로  NBP OCR GW 에 요청 하여, json 파일 구해오기
    #모든 정보는 데이터 클래스 "cSVG2JSON" 저장 하자 
    def get_json_from_NBP_OCR(self, cSVG2JSON): 
    
        for index , file_key in enumerate(self.dataClass_Svg2Json.img_source):

            open_file = self.dataClass_Svg2Json.img_source[file_key]  #파일명을 키로.. 파일 경로 받아 오기
            
            files   = [('file', open( open_file ,'rb'))]     
            headers = {'X-OCR-SECRET': self.secret_key }
            
            time.sleep(1) # 잠시 쉬었다가.. (웹의 불안 요소.. 예외처리는 나중에 하자)
            # NBP OCR 에 요청하기  (file 에 이미지 경로 -> url로 할까?)    
            # data = payload 데이터 전달
            response = requests.request("POST", self.api_GW_url , headers=headers, data = payload, files = files) #기본적인 사용 text 
            
            #결과 확인 -
            print(response.text.encode('utf8'))

            # Joson 값 담아 두기.. 경로는?            
            json_content = response.json()  
            
            #1. Json 파일로 저장 하기
            #Json 쓰기모드로 열기 - 쓰기
            with open( self.dir + file_key + '.json', 'w') as outfile:
                #json.dump(data, outfile)
                json.dump(json_content  , outfile, indent=4)  #indent 옵션 (줄맞춤)
            
            # 파일명  : {json 결과 , 경로} 로 기록 관리
            self.dataClass_Svg2Json.fromNBP_json[file_key + '.json']  =  json_content    #json 파일 명을 key 로 json 파일을 조회 할수 있도록 

        return self.dataClass_Svg2Json  #소스 파일명, 파일 이미지 경로, json 파일명, 생성된 json 파일 저장 경로
        


    # 네트워크 연결이 되지 않는 경우, 기 저장된 Json 파일을사용하여 데이터 채우기
    #  - NBP OCR 서버에 접근이 되지 않는 경우  (보안 등)
    #  - 네트워크 장애
    def get_json_from_Localhost(self, cSVG2JSON):
        print("get_json_from_Localhost")

        
