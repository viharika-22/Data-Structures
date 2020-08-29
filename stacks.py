class stack:
    def __init__(self,size):
        self.stacks=[]
        self.size=size
    def push(self,item):
        self.stacks.append(item)
    def pop(self):
        item=self.stacks[len(self.stacks)-1]
        self.stacks.pop(len(self.stacks)-1)
        print(item)
    def length(self):
        print(len(self.stacks))
    def peek(self):
        print(self.stacks[len(self.stacks)-1])
    def overflow(self):
        if len(self.stacks)>self.size:
            print("overflow")
        else:
            print("not overflow")
s1=stack(4)
s1.push(62)
s1.push(50)
s1.push(37)
s1.push(58)
s1.push(40)
s1.length()
s1.pop()
s1.length()
s1.peek()
s1.push(1)
s1.overflow()