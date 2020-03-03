import pandas as pd

prt = '''입력할 목록 양식은 samplelist.xlsx 파일을 참고해주세요.
목록은 xlsx 파일 이어야 합니다. 확장자를 빼고 입력하세요.
파일 이름 입력:'''

def shuffle():
    result_df = target_df.sample(frac=1).reset_index(drop=True)
    result_df['순번'] = result_df.index + 1
    result_df.to_excel('%s_랜덤순서.xlsx' %(target), index=False)
    return print(result_df)

print(prt)
target = str(input())
target_df = pd.read_excel('%s.xlsx' %(target))
# print(target_df)

shuffle()
