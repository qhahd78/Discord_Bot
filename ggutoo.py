print("끝말잇기 시작")

# while 문 무조건 들어가도록 
li = []
z= 0 
word = input("단어입력 : ")
li.append(word)
value = True

def test(word):
    # 입력 받은 문자 저장
    a = word
    # 리스트의 마지막 단어
    last = li[-1]
    # 마지막 언어의 마지막 글자 
    lala = last[-1]
    # 리스트에 입력 받은 문자 추가 
    li.append(a)
    return lala
    

while value : 
    z += 1
    word = input("단어입력 : ")
    lala = test(word)
    # 입력된 글자의 첫 글자와, 이 전의 글자의 마지막 글자의 비교 
    if word[0] == lala : 
        pass 
    elif word[0] != lala :
        print("틀렸습니다. 끝말잇기를 종료합니다.")
        print("총 %d 번 진행됐네요. " % z)
        value = False 
    


    
    
