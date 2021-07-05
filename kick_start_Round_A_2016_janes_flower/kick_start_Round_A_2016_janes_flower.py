def total_cash(M, C, r):
    cash = 0
    # 左辺の中の一番右のレートは(1 + r)^0=1だから1
    rate = 1
    # これは入力例1の左辺の一番右から計算している。# MはMonth, 月毎なので-1ずつ減っていくループで最終的に0になれば終了＝左辺の中の右から2番目の値で終了
    for i in range(M, 0, -1):  
        cash += C[i] * rate 
        rate *= 1 + r
    cash -= C[0] * rate
    return cash

def solution(M, C):
    """
    適切な解solを返すように，関数solutionの中身を作ってみよう!
    """
    left, right = -1, 1 # rの制約が-1以上１以下なのでその最大値でおく
    while right - left > 10e-10: # 左右の誤差が10^-10までになるまで計算を繰り返す
        # 真ん中(= 仮のr)求める
        middle = (left + right) / 2
       
        # 仮のrでのIRRを出す
        irr = total_cash(M, C, middle)
      
        # IRRが０以上(下界と中間の符号が同じならば {= 左が０以上 = 左の符号が "+"ならば?})
        if irr > 0:
            left = middle # 仮のrを左側に寄せていく
        # 符号が違うならば (= 左が０以下 = 符号 "-"ならば)
        else:
            right = middle # 右側を寄せていく
            
    sol = middle
    return sol

T = int(input())
for case_number in range(1, T + 1):
    M = int(input())
    C = list(map(int, input().split()))
    # 組み込み関数round(x, y)は値xを小数第y位までに丸めて（四捨五入して）返す関数である．
    print(f'Case #{case_number}: {round(solution(M, C), 9)}')
    # yのデフォルト値は0であり，yが0のときは整数への丸めを意味する