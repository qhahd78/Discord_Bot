from .api import apifun

def test(word, li):
    # 입력 받은 문자 저장
    a = word
    # 리스트의 마지막 단어
    last = li[-1]
    # 마지막 언어의 마지막 글자 
    lala = last[-1]
    # 리스트에 입력 받은 문자 추가 
    li.append(a)
    return lala
    
# print("끝말잇기 시작!")

# 이전에 사용한 단어는 사용하지 못 하게 하기 위해 list 선언

def ggutoo (word): 
    li = []
    z= 0 

    # 단어의 글자수가 1일 경우 프로그램 종료 
    if len(word) == 1 : 
        # value = False
        return ("한 글자인 단어는 안 됩니다.")

    # 1이 아닌 경우 api 에서 검색 및 while 문에 들어간다 .
    else : 
        meaning = apifun(word)
        if meaning == False : 
            value = meaning
        # while 문 들어가도록 True 설정
        else : 
            print("단어 뜻 : %s" % meaning)
            # 한 줄 띄우기 
            # print("")
            li.append(word)
            value = True

    while value : 
        # 몇 번 진행되는지 세어주는 변수 z 
        # z += 1
        word = input("단어입력 : ")
        # 한 글자일 경우 어떤 경우에서든 false 
        if len(word) == 1 : 
            value = False 
            print("한 글자인 단어는 안 됩니다.")
        # 한 글자가 아닐 경우에만 사전 검색 및 끝말잇기 검사
        else : 
            lala = test(word, li)
            # 입력된 글자의 첫 글자와, 이 전의 글자의 마지막 글자의 비교 
            if word[0] == lala : 
                meaning = apifun(word) 
                # print(meaning)
                # api 에서 사전에서 검색 결과가 없으면 False 를 반환한다. 
                if meaning == False:
                    value = meaning
                    print("사전에 없는 단어입니다.")
                # false 가 아닐 경우 단어의 뜻 출력 
                else :
                    print("단어 뜻 : %s" % meaning)
                    print("")
            # 입력된 첫 글자와 이전의 단어의 마지막 글자가 동일하지 않은 경우 
            elif word[0] != lala :
                # while 문 나가기 
                value = False 

# print("끝말잇기를 종료합니다.")
# print("총 %d 번 진행됐네요. " % z)


    
    
