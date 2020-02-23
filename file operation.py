# # print(open.__doc__)
# # --------- ---------------------------------------------------------------
# # 'r'       open for reading (default)
# # 'w'       open for writing, truncating the file first
# # 'x'       create a new file and open it for writing
# # 'a'       open for writing, appending to the end of the file if it exists
# # 'b'       binary mode
# # 't'       text mode (default)
# # '+'       open a disk file for updating (reading and writing)
# # 'U'       universal newline mode (deprecated)
# # ========= ===============================================================
# # f=open("demo.txt","r")
# # content=f.read()
# # print(content)
# # f.close()
# #Read by line
# #print.readline()
# #print.readlines()
# # how to read line by line
#
# f=open("demo.txt","r")
# print(f.readlines())
# # content=f.read()
# # for line in f:
# #     print(line)
# #
# f.close()
# append mode
# f=open("roshan.txt","a")
# a=f.write("roshan is learning file operation\n")
# f.close()\


try:
    f = open("roshan2.txt", "r+")
    f.write("roshan is learning file operation\n")
    f.close()
except Exception as e:
    print(e)
print("out of reach")
