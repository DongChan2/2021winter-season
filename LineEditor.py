class ArrayList:
    def __init__(self):
        self.items=[1,2,3]
    def insert(self,pos,elem):
        self.items.insert(pos,elem)
    def delete(self,pos):
        self.items.pop(pos)
    def getEntry(self,pos):
        return self.items[pos]
    def isEmpty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items) 
    def clear(self):
        self.items=[]
    def sort(self):
        self.items.sort()
    def merge(self,lst):
        self.items.extend(lst)
    def replac(self,pos,str):
        self.items[pos]=str    
                



def myLineEditor():
    list=ArrayList()
    while True:
        command=input("메뉴선택] i-입력, d-삭제 r-변경 p-출력 l-파일읽기 s-저장 q-종료")
        if command=='i':
            pos=int(input("  입력행 번호  "))
            str=input("  입력행 내용:  ")
            list.insert(pos,str)
        elif command=='d':
            pos=int(input("  삭제행 번호  "))
            list.delete(pos)
        elif command=='r':
            pos=int(input("  변경행 번호  "))
            str=input("  변경행 내용:  ")    
            list.replac(pos,str)
        elif command=='q':
            return 
        elif command=='p':
            print("Line Editor")
            for line in range(list.size()):
                print("[%2d]"%line,end='')
                print(list.getEntry(line))
            print()
        elif command=='l':
            filename='test.txt'
            infile=open(filename,'r')
            lines=infile.readlines()
            for line in lines:
                list.insert(list.size(),line.rstrip('\n'))
            infile.close()
        elif command=='s':
            filename='test.txt'
            outfile=open(filename,'w')
            for i in range(list.size()):
                outfile.write(list.getEntry(i)+'\n')
            outfile.close()
                        
                
myLineEditor()        