def main():
    loop = 0
    name = str(input("What is the word or Phrase?: "))
    f1 = open(name,"x")
    f1.close()
    f = open(name,"a")
    namespace = name+"\n"
    while True:
        f.write(namespace)
        if loop >= 500:
            break
        else:
            loop = loop+1
    print("Done")
main()
