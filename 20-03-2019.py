#Q1.Write a program to write a text file named "lines.txt" with 100 lines
file1 = open("lines.txt","w+")
file1.write("Following contains 100 lines:")
for value in range(1,101):
    line = "\t\n"+"Line Number : "+str(value)+"\n"
    file1.write(line)
file1.close()

#Q3.Write a program to append the above file and add 20 more lines
file1 = open("lines.txt","a+")
file1.seek(0,2)
file1.write("\n\n"+"Appended Lines:")
for value in range(101,121):
    append_lines = "\n"+"Appended Line: "+str(value)+"\n"
    file1.write(append_lines)
file1.seek(0,0)
file1.close()

    