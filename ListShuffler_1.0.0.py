import pandas as pd

prt1 = '''파일 이름 입력:
(확장자는 xlsx입니다. 확장자를 빼고 입력하세요.)'''

def shuffle():
    result_df = target_df.sample(frac=1).reset_index(drop=True)
    result_df['순번'] = result_df.index + 1
    result_df.to_excel('%s_랜덤순서.xlsx' %(target), index=False)
    return print(result_df)

print(prt1)
target = str(input())
target_df = pd.read_excel('%s.xlsx' %(target))
# print(target_df)

shuffle()