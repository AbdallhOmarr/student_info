#making a class student info as i will use a several objects student 1 , student 2 , etc
class student_info:

    #student name as a method
    def student_name(self,name):
        self.student_name=name
        return name
    #student mark as a method
    def student_mark(self,mark):
        self.student_mark=mark
        return mark

    #method to calculate the avg
    def student_avg(self):
        avg = (self.student_mark/100)*100
        return avg

    #method to calculate the rating
    def student_rating(self):
        avg = self.student_avg()

        if avg < 50:
            return 'Fail'
        elif avg >= 50 :
            return 'succeed'

#adding lists to store several students data
name =[]
mark =[]
avg=[]
rating=[]

#for loop to get the information from the user
for i in range(3):
    i = student_info()
    name.append(i.student_name(input('Enter a name \n')))
    mark.append(i.student_mark(int(input('Enter his mark\n'))))
    avg.append(i.student_avg())
    rating.append(i.student_rating())

#printing all the data
print(name,',\t',mark,',\t',avg,',\t',rating,',\t')


