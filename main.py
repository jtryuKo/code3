import pandas
import os

desired_width = 320
pandas.set_option('display.width', desired_width)
pandas.set_option('display.max_column', 12)


#폴더에서 파일을 검색하기
dir = 'C:/Users/ryuje/Desktop/PyProject/blog6'
files = os.listdir(dir)
global dataframeFile  # 데이터프레임의 전역화

# 데이터프레임초기화
dataframeFile = pandas.DataFrame(index=range(0, 0), columns=['파일명', '이름', '확장자', '위치정보'])

def file_search(dir, dataframeFile):
    files = os.listdir(dir)
    for file in files:
        fullname_file = os.path.join(dir, file)
        if os.path.isdir(fullname_file):
            dataframeFile = file_search(fullname_file, dataframeFile)  # 재귀함수 호출
        else:
            name, ext = os.path.splitext(file)
            #데이터 프레임에 점검결과를 빈칸으로 설정을 함
            dic_file = {'파일명': file, '이름': name, '확장자': ext, '위치정보': fullname_file, '점검결과': ''}
            dataframeFile = dataframeFile.append(dic_file, ignore_index=True)
    # 데이터프레임 리턴
    return dataframeFile

# 재귀함수 호출
dataframeFile = file_search(dir, dataframeFile)

# 데이터프레임 결과출력
print(dataframeFile)

#엑셀파일만 추출해 내기


