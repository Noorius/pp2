def summ(arg1, arg2):
    print(arg1+arg2)

def document_it(func):
    def start_end(arg1,arg2):
        print('start')
        func(arg1,arg2)
        print('end')
    return start_end

cool=document_it(summ)
cool(3,5)



