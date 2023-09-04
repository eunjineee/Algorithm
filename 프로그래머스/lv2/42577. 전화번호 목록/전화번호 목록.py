def solution(phone_book):

    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        i_len = len(str(phone_book[i]))
        if phone_book[i] == phone_book[i+1][:i_len]:
            return False
    return True