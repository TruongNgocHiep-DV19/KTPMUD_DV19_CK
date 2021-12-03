import random

class STUDENT():

    def __init__(self, id=None , points=None , credits=None):
        if points is not None:
            self._points = points
        else:
            self._points = round((random.uniform(0, 4)),1)
        if credits is not None:
            self._credits = credits
        else:
             self._credits = random.randint(0, 250)
        if id is not None:
            self._id = id
        else:
            self._id = "SinhVien_{}".format(random.randint(0, 10000))

    def result(self):
        if self._points >= 3.8 and self._points <= 4:
            return "A+"
        elif self._points >= 3.3 and self._points <= 3.7:
            return "A"
        elif self._points >= 3.0 and self._points <= 3.2:
            return "B+"
        elif self._points >= 2.6 and self._points <= 2.9:
            return "B"
        elif self._points >= 1.8 and self._points <= 2.5:
            return "C"
        elif self._points < 1.8:
            return "D"
    
    def graduated(self):
        if self.result != 'D'  and self._credits <= 250 and self._points >= 1.8:
            return True
        else: 
            return False

def sort(x: STUDENT):
    return x._points

def danh_sach_sinh_vien():
    #n = input("Nhap so sinh vien: ")
    list_graduated = []
    list_student = []
    for i in range(int(n)):
        s = STUDENT()
        list_student.append(s)
        if s.graduated():
            list_graduated.append(s)
    count = 0
    list_student.sort(key=sort, reverse=True)
    print(f'MSSV co diem cao nhat: {list_student[0]._id}')
    for student in list_student:
        #print(f'{student._id}: {student._score}, result: {student.result()}, credit: {student._credits}, graduate: {student.graduate()}')
        if student.graduated() == True:
            count = count + 1
        print(f'{student._id}: {student._points}, result: {student.result()}, credit: {student._credits}, graduated: {student.graduated()}')
    print(f'Tổng số sinh viên tốt nghiệp : , {count}')
#danh_sach_sinh_vien()
if __name__ == "__main__":
    n = input("Nhap so sinh vien: ")
    danh_sach_sinh_vien()