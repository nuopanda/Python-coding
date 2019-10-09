from stack import Stack

stack=Stack()
stack.push("a")
stack.push("b")
stack.push("c")
temp=stack.__str__()
print(temp)
for letter in range(97,123):
    print(chr(letter))