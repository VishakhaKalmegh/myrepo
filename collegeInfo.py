class Department:

    def __init__(self,id,name):
        self.deptId=id
        self.deptName=name


    def __str__(self):
        return 'Dept Id : {},Dept Name : {}'.format(self.deptId,self.deptName)

    def __repr__(self):
        return str(self)




class Subject:

    def __init__(self,sid,sname):
        self.subId=sid
        self.subName=sname

    def __str__(self):
        return 'Subj Id : {},Subj Name : {}'.format(self.subId, self.subName)

    def __repr__(self):
        return str(self)



class Student:

    def __init__(self,id,stnm,age,addr,dept,marks):
        self.studId=id
        self.studName=stnm
        self.studAge=age
        self.studAddr=addr
        self.studDept=dept
        self.studMark=marks

    def __str__(self):
        return 'Stud Id : {},Stud Name : {}, Stud Age : {}, Stud Addr : {}, Stud Dept : {}, Stud Marks : {}'.format(self.studId, self.studName,
                                                                                        self.studAge,self.studAddr,self.studDept,self.studMark)

    def __repr__(self):
        return str(self)


class Professor:

    def __init__(self,id,name,age,paddr,salary,listofSubj,listofdept):
        self.profId = id
        self.profName = name
        self.profAge = age
        self.profAddr=paddr
        self.profSal = salary
        self.profDeptlist = listofdept
        self.profsubjlist = listofSubj

    def __str__(self):
        return ' prof Id : {},prof Name : {}, prof Age : {}, prof Addr : {}, prof salary : {}, Sub List: {},Dept List: {}'.format(
            self.profId, self.profName,
            self.profAge, self.profAddr, self.profSal, self.profsubjlist,self.profDeptlist)

    def __repr__(self):
        return str(self)



class College:

    def __init__(self,id,name,caddr,listofStud,listofdept,listofProf):
        self.clgId = id
        self.clgName = name
        self.clgAddr= caddr
        self.clgStudList = listofStud
        self.clgDeptlist = listofdept
        self.clgProflist = listofProf

    def __str__(self):
        return ' Clg Id : {},Clg Name : {},clg Addr : {}, Stud List: {},Dept List: {} , prof List : {}, '.format(
            self.clgId, self.clgName,
            self.clgAddr, self.clgStudList, self.clgDeptlist, self.clgproflist)

    def __repr__(self):
        return str(self)


