def string_to_number(s):
    if s.isdigit() or (s[0] == "-" and s[1:].isdigit()) :
        return int(s)
    else:
        return False
    
    
    
    
print(string_to_number("-1234"))
print(string_to_number("1234"))
print(string_to_number("1234"))
print(string_to_number("Hello world"))
print(string_to_number("1234"))
print(string_to_number("1sad4"))


