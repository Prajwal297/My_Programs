def count_text_file(counting):
    word_count=0
    char_count=0
    line_count=0
    with open("counting","r") as file:
        for line in file:
            word_count+=len(line.split())
            char_count+=len(line)
            line_count+=1
    print("total words      :",word_count)
    print("total characters :",char_count)
    print("total lines      :",line_count)
def create_text_file(counting,content):
    with open("counting","w") as file:
        file.write(content)
counting="sample.txt"
content=input("enter the sentence to be counted :")
create_text_file(counting,content)
count_text_file(counting)