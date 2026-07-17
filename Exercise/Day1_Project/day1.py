from rich import print

numbers=[1,2,3,4,5]
#java way to print squares of numbers in a list
#for(int i=0;i<numbers.length;i++){System.out.println(numbers[i]*numbers[i])}

#Pythonic way using comprehension

squares=[i*i for i in numbers]
print(squares)

#context manager
with open("output.txt","w") as file:
    file.write("\n".join(str(n) for n in squares))

with open("output.txt") as file:
    print(file.read())