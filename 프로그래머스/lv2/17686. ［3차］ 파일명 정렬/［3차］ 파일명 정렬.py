def solution(files):
    pieces = []
    for file in files:
        piece = []
        flag = 0
        for idx in range(len(file)):
            if flag == 0 and file[idx] in '0123456789':
                piece.append(file[0:idx])
                flag = idx
            if flag:
                if file[idx] not in '0123456789':
                    piece.append(file[flag:idx])
                    piece.append(file[idx:])
                    break
                elif idx == len(file)-1:
                    piece.append(file[flag:])  
        pieces.append(piece)

    piece_sort = pieces.sort(key=lambda x: (x[0].lower(), int(x[1])))
    
    answer = []
    for piece in pieces:
        answer.append("".join(piece))
    return answer