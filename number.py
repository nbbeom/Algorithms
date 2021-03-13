def solution(phone_book):
    for i in range(0,len(phone_book)):
            for j in range(i+1,len(phone_book)):
                if phone_book[j].startswith(phone_book[i]):
                    print(phone_book[j])
                    print(phone_book[i])
                    print(phone_book[j].startswith(phone_book[i]))
                    return print("false")
    return print("true")

phone_book=["123", "456", "789"]
solution(phone_book)
