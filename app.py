import numpy as np

from src.person import Person



##positional and keyword argments
'''
def hello(*args,**kwargs):
    print(args)
    print(kwargs)

lst=list(('srihari','erigineni'))
dict_val={'age':27,'dob':1997}

hello(*lst,**dict_val)'''


if __name__=="__main__":
    person1=Person("Srihari","Erigineni")
    person1.display()


