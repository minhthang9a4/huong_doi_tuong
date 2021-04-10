import random
import cmath
class Person:
    def __init__(self ,n):
        self.so_sinh_vien = n
        self.name = []
        self.age = []
        self.gender =[]
    def ho_va_ten(self):
        for i in range(0,self.so_sinh_vien):
            ho_ten =str(input("Họ và tên sinh viên thứ {} là: ".format(i+1)))
            self.name.append(ho_ten)
    def tuoi_sv(self):
        for i in range(0,self.so_sinh_vien):
            tuoi_sv = random.randrange(17, 25)
            self.age.append(tuoi_sv)
    def gioi_tinh_sv(self):
        for i in range(0,self.so_sinh_vien):
            gioi_tinh =str(input("Giới tính sinh viên {} là: ".format(i+1)))
            self.gender.append(gioi_tinh)
            
class Student(Person):
    def __init__(self, n):
        super().__init__(n)
        self.id= []
        self.classs = []
        self.grade = []
        self.danhsach = {}
    def ID_number(self):
        for i in range(0,self.so_sinh_vien):
           mssv = int(input("Mã id của sinh viên thứ {} là: ".format(i+1)))
           self.id.append(mssv)
           
    def CLASS(self):
        for i in range(0,self.so_sinh_vien):
            lop_hoc= str(input("Lớp của sinh viên {} là: ".format(i+1)))
            self.classs.append(lop_hoc)
            
    def GRADE(self):
        for i in range(0,self.so_sinh_vien):
            diem_so = float(input("Điểm của sinh viên {} là: ".format(i+1)))
            if diem_so < 0 or diem_so > 10:
                exit()
            self.grade.append(diem_so)
            
    def STT(self):
        for i in range(0,self.so_sinh_vien):
            q={" Họ và tên sinh viên thứ {}: ".format(i+1):self.name[i]}
            self.danhsach.update(q)
            w ={"Tuổi của sinh viên {}: ".format(i+1):self.age[i]}
            self.danhsach.update(w)
            e={"Giới tính của sinh viên {}: ".format(i+1):self.gender[i]}
            self.danhsach.update(e)
            r={"ID của sinh viên {}: ".format(i+1):self.id[i]}
            self.danhsach.update(r)
            t={"Lớp của sinh viên {}: ".format(i+1):self.classs[i]}
            self.danhsach.update(t)
            y={"Điểm của sinh viên {}: ".format(i+1):self.grade[i]}
            self.danhsach.update(y)
        return self.danhsach
    def name(self):
        return self.name
    def age(self):
        return self.age 
    def gender(self):
        return self.gender
class Test_max(Student):
    def __init__(self,n):
        super().__init__(n)
    def max_grade(self):
        maximum = max(self.grade)
        for i in range(0, self.so_sinh_vien):
            if self.grade[i+1] == maximum:
                return print(self.name[i+1],self.age[i+1],"tuổi","giới tính",self.gender[i+1],"ID:",self.id[i+1],"Lớp:",self.classs[i+1],"điểm cao nhất:",self.grade[i+1])        
class Complex:
    def __init__(self, n, real , image):
        super.__init__( real, image)
        self.real = real
        self.image = image
    def module_complex(self):
        m = cmath.sqrt(real ** 2 + image ** 2)
        return m

test = Test_max(3)
test.ho_va_ten()
test.tuoi_sv()
test.gioi_tinh_sv()
test.ID_number()
test.CLASS()
test.GRADE()
print(test.STT())
test.max_grade()
  
                    
        