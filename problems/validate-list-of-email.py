def fun(s):
    # return True if s is a valid email, else return False
    index = s.find("@")
    index2 = s.find(".")
    abc= 'abcdefghijlkmnopqrstuvwxyz0123456789_-'
    if index == -1 or s.count('@')!=1 or index ==0 or index2==0:
        return False
    for i in range(index):
        letter = s[i]
        if letter not in abc and letter not in abc.upper():
       
            return False
    if len(s[index2:]) >4:
        return False
    if  s[index:].count(".") != 1 :
        return False
        
    for i in range (index+1, index2):
        letter = s[i]
        if letter not in 'abcdefghijlkmnopqrstuvwxyz0123456789' and letter not  in 'abcdefghijlkmnopqrstuvwxyz.'.upper():
            return False  
    for i in range (index2+1, len(s)):
        letter = s[i]
        if letter not in 'abcdefghijlkmnopqrstuvwxyz' and letter not  in 'abcdefghijlkmnopqrstuvwxyz.'.upper():
            return False   
    return True     
        

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)