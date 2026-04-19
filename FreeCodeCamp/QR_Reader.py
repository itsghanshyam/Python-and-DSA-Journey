#Code for daily challenge in free code camp for QR code reader.




def decode_qr(qr_code):
    qr_code = list(map(list,qr_code))
    for code in qr_code:
        print(code)
    print("----------------------")
    def rotate(qr):
        new_qr = [["a0","a1","a2","a3","a4","a5"],
["b0","b1","b2","b3","b4","b5"],
["c0","c1","c2","c3","c4","c5"],
["d0","d1","d2","d3","d4","d5"],
["e0","e1","e2","e3","e4","e5"],
["f0","f1","f2","f3","f4","f5"]]
        for index,row in enumerate(qr):
            for index2,element in enumerate(row):
                new_qr[index2][5-index] = element
        return new_qr
    def check(qr):
        if qr[0][0] =="1" and qr[0][1] =="1" and qr[1][0] == "1" and qr[1][1]=="1":
            if qr[0][4] == "1" and qr[0][5] == "1" and qr[1][4] == "1" and qr[1][5] == "1":
                if qr[4][0] == "1" and qr[4][1] == "1" and qr[5][0] == "1" and qr[5][1] == "1":
                    return qr
                else:
                    qr = rotate(qr)
                    return check(qr)
            else:
                qr = rotate(qr)
                return check(qr)
        else:
            qr = rotate(qr)
            return check(qr)
    qr_code = check(qr_code)
    def read(qr):
        code = ""
        for index,row in enumerate(qr):
            for index2,element in enumerate(row):
                if index <2 and index2>1 and index2<4:
                    code += element
                if index >=2 and index <4:
                    code += element
                if index >= 4 and index2>1:
                    code += element
        return code
    qr_code = read(qr_code)
    return qr_code
