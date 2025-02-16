T = int(input())

for t in range(1, T + 1):
    deck = [[0] * 13 for _ in range(4)]  # 문양별 13개의 카드
    s = input()
    flag = True  # 중복 여부 확인
    suit_dict = {'S': 0, 'H': 2, 'C': 3, 'D': 1}  # 문양을 인덱스로 변환

    for i in range(0, len(s), 3):  # 3글자씩 끊어서 처리
        suit = s[i]  # 문양
        num = int(s[i + 1:i + 3])  # 카드 숫자

        suit_idx = suit_dict[suit]  # 해당 문양의 인덱스 가져오기
        if deck[suit_idx][num - 1]:  # 이미 존재하면 ERROR
            flag = False
            break

        deck[suit_idx][num - 1] = 1  # 해당 카드 체크

    if flag:
        result = [13 - sum(deck[i]) for i in range(4)]  # 부족한 카드 수 계산
        print(f'#{t} {" ".join(map(str, result))}')
    else:
        print(f'#{t} ERROR')
