


def fun1():
    print('Hello')

def fun2():
   lines = "HelloHello"
   print(lines)
   words = lines.flatMap(lambda line:line.split(' '))
   print(words)





if __name__ == "__main__":
    fun1()
    fun2()