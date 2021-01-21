from copy import deepcopy


class Box:
    __counter = 0
    sortedDic={}
    #keyorder=[]
    def __init__(self, **coordinates):
        type(self).sortedDic={}

        self.__dict__.update(**coordinates)
        #print(self.__dict__)
        if len(coordinates)==4:
           keyorder= ["x1","y1","x2","y2"]
           type(self).sortedDic=dict(sorted(self.__dict__.items(), key = lambda i: keyorder.index(i[0])))

        if len(coordinates)==2:
           keyorder=["p1","p2"]
           type(self).sortedDic=dict(sorted(self.__dict__.items(), key = lambda i: keyorder.index(i[0])))



    def __str__(self):

        """ User friend representation of the object"""
        print(type(self).sortedDic)
        string = ""
        temp=list(type(self).sortedDic)
        j=-1
        if len(temp)==4:

           for i in temp[:len(temp)-1]:
               if i==j:
                  continue
               try:
                  j=temp[temp.index(i)+1]
               except (ValueError, IndexError):
                  j = None
               string= string + " ({},{})".format(type(self).sortedDic[i],type(self).sortedDic[j])
           return string
        if len(temp)==2:
            for i in temp[:len(temp) - 1]:
                string = string + " ({})".format(type(self).sortedDic[i])
            return string






class TexBox(Box):
    sortedDic={}
    def __init__(self,**arguments):

        type(self).sortedDic={}
        argument = deepcopy(arguments)
        if "text" in arguments.keys():
            argument.pop("text", None)
        print(arguments)
        #print(argument)
        super().__init__(**argument)
        #self.__dict__.update(**arguments)

        if "text" in arguments:
            print("yes")
            text=arguments["text"]
            self.__dict__["text"]=text
        keyorder=["x1","y1","x2","y2","text"]
        print(self.__dict__)
        type(self).sortedDic= sorted(self.__dict__.items(), key=lambda i: keyorder.index(i[0]))


    def __str__(self):
        return str(type(self).sortedDic)

b=TexBox(x1=2,x2=3,y1=1,y2=4,text="Box1")
print(b)
