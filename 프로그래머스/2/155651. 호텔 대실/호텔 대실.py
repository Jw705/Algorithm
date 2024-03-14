def solution(book_time):
    answer = 0
    room=['']*1000
    book_time.sort(key = lambda x:(x[0][0:2],x[0][3:5]))
    for book in book_time:
        start_h=int(book[0][0:2])
        start_m=int(book[0][3:5])
        i=0
        while True:
            if room[i]=='':
                room[i]=book
                break
            else:
                end_h=int(room[i][1][0:2])
                end_m=int(room[i][1][3:5])+10
                if end_m>=60:
                    end_h+=1
                    end_m-=60
                if end_h<start_h or (end_h==start_h and end_m<=start_m):
                    room[i]=book
                    break
                else:
                    i+=1
                
    for i in range(1000):
        if room[i]=='':
            break
        else:
            answer+=1
    return answer