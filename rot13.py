import codecs

text = input("input:  ")
print(text)

rot13 = codecs.encode(text, 'rot_13')
print(rot13)

text = codecs.decode(rot13, 'rot_13')
