### **SVG 이미지 NBP OCR 적용해서 Json (텍스트, 좌표) 으로 기록 하**기

* 목적 : 손글씨 자동 채점을 위한 정답 영역 추출 및 텍스트화
* 작성자 : Insung-Lee  (https://shippauljobs.blogspot.com/)
* 작성일 : 2021.06.10

---

* 제공 자료
  * Excel : SVG 파일 url 정보
* 개발 환경
  * 언어: Python 3.8.3 64bit
  * 운영체제: Windows 10
  * 작업 환경 : Visual Studio Code

* 구현 기능 및 실행 순서
  * Excel 에 기록된 image(SVG) 파일이 담긴  url 정보를 읽기
  * 확보된 svg url 정보를 기초로, NBP OCR API 을 사용할수 있는 포멧이 jpg 또는 png 파일로 변환 (본인은 png)
    * 대량의 파일을 읽어옴에 따른 web 지연을 고려 해야함
  * NBP OCR 외부 접속 설정
    * 참조 : NBP 의 API GW URL , Secret_key 받아 오기  (필독 : 서비스  과금 정책)
  * API GW URL , Secret_key 을 사용하여 NBP OCR Service 이용 신청, 설정
    * source : png 파일
    * return  : source 이미지내 텍스트 (bouding box) 각 좌표 , text 정보
  * Json format 정보를 json 파일로 저장
  * Json 파일내 bouding box 좌표 이용하여 영역 추출-저장
  * "이미지+Label" 매핑
* 프로젝트 구성
  * root
  * /source
    * xxxxsvg.xlsx
  * /sample_data
    * hello.png
    * hello.svg
  * /myClass
    * SVGurl2Png.py
    * png2NBPOCR.py
    * json_ctrl.py
    * util.py
    * __init__.py
  * main.py
  * Readme.md
* 주요 라이브러리 설치
  * svg to png 관련
  * ```
    import cairo   
    from svglib.svglib import svg2rlg 
    import cairosvg
    ```
  * ```
    ######################################################################
    # 필요한 라이브러리 환경 설정 입니다.
    #  > 혹시모를 삽질을 방지하기 위해 설치 순서 준수, 관리자 권한으로 실행 하세요~!
    #-----------------------------------------------------

    #-----------------------------------------------------
    # 1. cairo 설치  (파이썬 버전과 cpXX 가 맞아야 함 )
    #  > https://frhyme.github.io/python-lib/python_a_what_is_svg/
    #  > https://wikidocs.net/75429  라이브러리 설치  ,
    #  > https://www.lfd.uci.edu/~gohlke/pythonlibs/#pycairo  설치
    # 설치 후 바로 import 되지 않으면 VS code 재시작.. 1~2회  필요

    #-----------------------------------------------------
    # - 파일명 : pycairo-1.20.0-cp38-cp38-win_amd64.whl       --> 파이썬 버전
    # > python -m pip install pycairo-1.20.0-cp38-cp38-win_amd64.whl
    # > easy_install .\pycairo-1.20.1-cp38-cp38-win_amd64.whl  # python -m pip install 설치 실패시
    # - Installing collected packages: pycairo
    # - Successfully installed pycairo-1.20.0

    #-----------------------------------------------------
    # 2. cairosvg 설치
    #-----------------------------------------------------
    # - Successfully installed pycairo-1.20.0
    # (base) pip3 install cairosvg

    #-----------------------------------------------------
    # 3. svglib 설치
    # > ckarh https://boltlessengineer.tistory.com/68
    #-----------------------------------------------------
    #  - pip3 install svglib

    #-----------------------------------------------------
    # 4. UniConverter2.0 설치  # Wondershare Uniconverter
    #-----------------------------------------------------
    #   > UniConverter 설치 경로에서 "dll"하위 디렉토리를 찾음 (ex) C:\Program Files\UniConvertor-2.0rc4\dlls).
    #   > 이 "dll"경로를 시스템 경로에 추가
    #   > VSCode를 닫고 프로젝트를 다시 로드
    #   > 서버를 다시 실행
    #   > 사용 : https://videoconverter.wondershare.net/?gclid=Cj0KCQjw--GFBhDeARIsACH_kdYVKcguQgYgqQRmiYjtpQ5O0T1XK4QG7hTkPJFcztkO8jkOeCnmF2gaAqWmEALw_wcB&gclsrc=aw.ds 
    #     - 다운로드 : https://downloads.sk1project.net/uniconvertor/2.0rc4/uniconvertor-2.0rc4-win64_headless.msi 
    #   > 사용 Code : https://github.com/pygobject/pycairo

    #-----------------------------------------------------
    # 5. gtk2-runtime-2.24.33-2021-01-30-ts-win64.exe 설치
    #   > https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer
    #-----------------------------------------------------
    
    #-----------------------------------------------------
    ## Open source OCR : Tesseract 설치   * Cloud 를 사용하지 않는 경우
    # 6. Tesseract at UB Mannheim
    #   > https://github.com/UB-Mannheim/tesseract/wiki 
    #-----------------------------------------------------
        
    
    ```
