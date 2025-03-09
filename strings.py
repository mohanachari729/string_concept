# #print the characters at even indices
# sentence = "python is amazing"
# result = sentence[: :2]
# print(result)

# # Replace all spaces in the string with underscores(_)
# s = "python is fun and powerful"
# modified_string =s.replace(" " , "_")
# print(modified_string)

# #. Check if the string contains only digits.
# s = "12345"
# digits = s.isnumeric()
# print(digits)

# ##Print the string in reverse order.
# s = "python is amazing"
# print(s[ : :-1])


# ##Capitalize the first letter of each word in the string and print the modified string.
# s = "python programming is fun"
# l = s.split()
# m = []
# for i in l :
#     result = i.capitalize()
#     m.append(result)
# print(' ' . join(m))

#---------------------or-------------------



##Capitalize the first letter of each word in the string and print the modified string.
s= "python programming is fun"
print(s.title())