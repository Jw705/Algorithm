def solution(numbers):
    answer = []
    arr = [1,3,7,15,31,63]
    
    def is_possible(string):
        if len(string) not in arr:
            return is_possible('0' + string)
        else:
            root_node = len(string)//2
            if string[root_node] == '0':
                if int(string)==0:
                    return True
                else:
                    return False
            elif len(string) == 3 or len(string) == 1:
                return True
            elif is_possible(string[0:root_node]) and is_possible(string[root_node + 1:]):
                return True
            else:
                return False
            
        
        
    for number in numbers:
        binary_number_string = str(format(number,'b'))
        if is_possible(binary_number_string):
            answer.append(1)
        else:            
            answer.append(0)
    return answer


'''
    print(10**15,format(10**15,'b'))
    print(len(str(format(10**15,'b'))))
    print()
    
    def generate_binary(value):
        if format(int(value),'b')
        
        if(len(value)>50):
            print("안돼!")
        else:
            
'''