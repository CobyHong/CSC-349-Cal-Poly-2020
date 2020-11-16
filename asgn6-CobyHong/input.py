import sys


def createDictionary():
    file = open(sys.argv[1], "r")
    content = file.readlines()

    str1 = content[0].strip()
    str2 = content[1].strip()
    
    for i in range(0, len(content)):
        content[i] = content[i].rstrip('\n')
        content[i] = content[i].split(' ')

    scores = {}
    hor = content[2]
    for i in range(3, len(content)):
        ver = content[i]
        for j in range(1, len(ver)):
            if(hor[j] != ' '):
                scores[ver[0] + hor[j]] = int(ver[j])
    return str1, str2, scores


def wunsch(seq1, seq2, dictionary):
    seq1_len = len(seq1)  
    seq2_len = len(seq2)

    scoring = []
    for i in range(seq2_len+1):
        scoring.append([])
        for j in range(seq1_len+1):
            scoring[-1].append(0)

    for i in range(0, seq2_len + 1):
        scoring[i][0] = dictionary["-" + seq2[i-1]] * i
    for j in range(0, seq1_len + 1):
        scoring[0][j] = dictionary[seq1[j-1] + "-"] * j
    
    for i in range(1, seq2_len + 1):
        for j in range(1, seq1_len + 1):
            match = scoring[i - 1][j - 1] + dictionary[seq1[j-1] + seq2[i-1]]
            delete = scoring[i-1][j] + dictionary["-" + seq2[i-1]]
            insert = scoring[i][j-1] + dictionary[seq1[j-1] + "-"]
            scoring[i][j] = max(match, delete, insert)
    
    align1 = ""
    align2 = ""
    max_score_len_x = seq2_len
    max_score_len_y = seq1_len

    while seq2_len > 0 and seq1_len > 0:
        current_score = scoring[seq2_len][seq1_len]
        diagonal_score = scoring[seq2_len-1][seq1_len-1]
        score_up = scoring[seq2_len][seq1_len-1]
        score_left = scoring[seq2_len-1][seq1_len]
    
        if current_score == diagonal_score + dictionary[seq1[seq1_len-1] + seq2[seq2_len-1]]:
            align1 += seq1[seq1_len-1]
            align2 += seq2[seq2_len-1]
            seq2_len -= 1
            seq1_len -= 1
        elif current_score == score_up + dictionary[seq1[seq1_len-1] + '-']:
            align1 += seq1[seq1_len-1]
            align2 += '-'
            seq1_len -= 1
        elif current_score == score_left + dictionary['-' + seq2[seq2_len-1]]:
            align1 += '-'
            align2 += seq2[seq2_len-1]
            seq2_len -= 1

    while seq1_len > 0:
        align1 += seq1[seq1_len-1]
        align2 += '-'
        seq1_len -= 1
    while seq2_len > 0:
        align1 += '-'
        align2 += seq2[seq2_len-1]
        seq2_len -= 1

    align1 = align1[::-1]
    align2 = align2[::-1]

    return align1, align2, str(scoring[max_score_len_x][max_score_len_y])


sequences = createDictionary()
out1, out2, score_total = wunsch(sequences[0], sequences[1], sequences[2])
print("x: " + " ".join(out1))
print("y: " + " ".join(out2))
print("Score: " + score_total)
