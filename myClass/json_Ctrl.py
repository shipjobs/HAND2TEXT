import json

file_path = "./sample.json"

###########################################################################
#작성자 : insung-lee
#작성일 : 2021-06-10
#목적 : 주어진 손글씨 Json 파일 관리
#내  용 : 일기, 저장, 수정 
#  - 손글씨 이미지 관리 Json 파일 디자인
###########################################################################

#진행중.............전체 글씨 분석후 카테고리 정리되면 추후정리
data = {}
data['WORD'] = []  # 하위 1
data['WORD'].append({   #하위 2-1
    "SVG URL": "XXXXXXXXXXXXXXXXX",
    "SVG FilePath": "XXXXXXXXXXXXXXXXX",
    "PNG URL": "XXXXXX"
})

data['WORD'].append({   #하위 2-1
    "TEXT URL": "XXXXXXXXXXXXXXXXX",
    "TEXT FilePath": "XXXXXXXXXXXXXXXXX"
})
#print(data)

########################################################################    
#Json 쓰기
def json_write(file_path):
    #Json 쓰기모드로 열기 - 쓰기
    with open(file_path, 'w') as outfile:
        #json.dump(data, outfile)
        json.dump(data, outfile, indent=4)  #indent 옵션



########################################################################    
#Json 읽기
def json_read(file_path):
    #file_path = "./sample.json"
    with open(file_path, "r") as json_file:
        json_data = json.load(json_file)  #읽기
        
        """   
        print(json_data)
        print("")
        print(json_data['WORD'])
        print("")
        #print(json_data['WORD'][0]['XXXX'])
        """
"""
json_data['posts'].append({
    "title": "How to parse JSON in android",
    "url": "https://codechacha.com/ko/how-to-parse-json-in-android/",
    "draft": "true"
})
"""
def json_add(file_path , json_data):
########################################################################
#기존 JSON 파일에 내용 추가해서 다시 저장
    #file_path = "./sample.json"
    json_data = {}
    
    #값을 불러 오기
    with open(file_path, "r") as json_file:
        json_data = json.load(json_file)

    #덥어 쓰기
    with open(file_path, 'w') as outfile:
        json.dump(json_data, outfile, indent=4)

