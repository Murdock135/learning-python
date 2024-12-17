import os
# print(dir(os))
# print()
# print(help(os))

print(os.getcwd())
print(os.environ.get('HOME'))
filePath = os.path.join(os.environ.get('HOME'),'test.txt')

print(filePath)
