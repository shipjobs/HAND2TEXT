import json


#손글씨 이미지의 Json Class 


# - 손글씨 관련 Josn 파일을 넣어 주면.. 해당 페이지내 글씨의 영역 좌표  (좌상단, 우하단) 를 반환
# - 손글씨 Json 에 대한  약속된 필드 정보를 가지고 있어 야함  (정책 수립 필요)   
def get_vertices_list_from_json( URL_json ):
    
    json_data = {}  #담을 공간
    dic_bounding_lt_rb = []

    #json_file (TEST IO Wraper) 으로 지정된 경로의 파일 읽어 오기
    with open(URL_json, "r") as json_file:  
        json_data = json.load(json_file)

    #좌표 정보 진입 경로
    #print(json_data['images'][0]['fields'][0]['boundingPoly']['vertices'][0])
    #print(json_data['images'][0]['fields'][1]['boundingPoly']['vertices'][2])
    
    cnt =  len( json_data['images'][0]['fields'][0] )  #개수 가져오기
    
    for index_cnt , vertices in enumerate( json_data['images'][0]['fields']  ) :
        
        #bounding box 별도로 담아 두기
        dic_bounding_lt_rb.insert(index_cnt , [vertices['boundingPoly']['vertices'][0]  ,    vertices['boundingPoly']['vertices'][2]])
        print( vertices['inferText'] )
    
    return dic_bounding_lt_rb

#get_vertices_list_from_json( "./sample_data/sample.json" )
print( get_vertices_list_from_json( "./sample_data/sample.json" ))
