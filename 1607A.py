


phrases={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,
               'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,
               'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

def word():
    phrase=input('please Enter Your Wotrd :')
    return phrase

num_list=[]

def calculate_phrase_number():
    for i in word():
        num_list.append(phrases[i])
    print(num_list)


def abs_calc():
    result=[]
    liner_keyboard_result=0
    for i in range(1,len(num_list)):
        x=num_list[i]-num_list[i-1]
        result.append(x)
        liner_keyboard_result=abs(x)+abs(liner_keyboard_result)
    print(liner_keyboard_result)

    

if __name__=='__main__':
    calculate_phrase_number()
    abs_calc()
