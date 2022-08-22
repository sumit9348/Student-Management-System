#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import getpass

def valid_password(pwd):                                            #check validity of passwords of student teacher
   flag=0
   l=['!','@','$','%','%','^','&','*','/']
   for i in pwd:
      if i in l and len(pwd)>5:
         flag=1
         break
      else:
          flag=0
   if flag!=1:
     return False
   else:
      return True

   
def display_student():                                            #display contents of student file                              
   print("--------------------------------------")
   print("student file is:")
   try:
      file=open("student_data1.txt",'r')
      for line in file:
         print(line)
   except FileExistsError:
      print("file doesn't exist")
   finally:
      file.close()

def display_teacher():                                            #display contents of teacher file
   print("--------------------------------------")
   print("teacher file is:")
   try:
      file=open("teacher_data1.txt",'r')
      for line in file:
         print(line)
   except FileExistsError:
      print("file doesn't exists")
   finally:
      file.close()

def update_student(id,m1,m2,m3,m4,m5):     #update student details
     newfile=[]
     try:
        obj=open("student_data1.txt",'r')
        for l in obj.readlines():
           s=list(l.strip().split('\t'))
           if s[0]==id:
              s[3]=m1
              s[4]=m2
              s[5]=m3
              s[6]=m4
              s[7]=m5
              newfile.append(s)
           else:
              newfile.append(s)
     except FileExistsError:
        print("above file doesn't exists")
     finally:
        obj.close()
     try:
        obj=open("student_data1.txt",'w')
        for l in newfile:
           obj.write("\t".join(l))
           obj.write("\n")
     except FileExistsError:
        print("above file doesn't exists,you are directed to main menu")
        call()
     finally:
        obj.close()
        print("\nupdate success")

def delete_student(id):                                    #delete the student details
     try:
        obj=open("student_data1.txt",'r')
        newfile=[]
        for l in obj.readlines():
           s=list(l.strip().split('\t'))
           if s[0]==id:
             pass
           else:
             newfile.append(s)
     except FileExistsError:
        print("above file doesn't exists,you are directed to main menu")
        call()
     finally:
        obj.close()
     try:
        obj=open("student_data1.txt",'w')
        for l in newfile:
           obj.write("\t".join(l))
           obj.write("\n")
     except FileExistsError:
        print("above file doesn't exists,you are directed to main menu")
        call()
     finally:
        obj.close()
        print("\ndelete success")

def delete_teacher(id):   #delete the teacher details
     newfile=[]
     try:
        obj=open("teacher_data1.txt",'r')
        for l in obj.readlines():
           s=list(l.strip().split('\t'))
           if s[0]==id:
              pass
           else:
              newfile.append(s)
     except FileExistsError:
        print("above file doesn't exists,you are directed to main menu")
        call()
     finally:
        obj.close()
     try:
        obj=open("teacher_data1.txt",'w')
        for l in newfile:
           obj.write("\t".join(l))
           obj.write("\n")
     except FileExistsError:
        print("above file doesn't exists,you are directed to main menu")
        call()
     finally:
        obj.close()
        print("\ndelete success")

def update_teacher(id,sub):                        #update teacher details
     newfile=[]
     try:
        obj=open("teacher_data1.txt",'r')
        for l in obj.readlines():
           s=list(l.strip().split('\t'))
           if s[0]==id:
              s[3]=sub
              newfile.append(s)
           else:
              newfile.append(s)
     except FileExistsError:
        print("above file doesn't exists,you are directed to main menu")
        call()
     finally:
        obj.close()
     try:
        obj=open("teacher_data1.txt",'w')
        for l in newfile:
           obj.write("\t".join(l))
           obj.write("\n")
     except FileExistsError:
        print("above file doesn't exists,you are directed to main menu")
        call()

     finally:
        obj.close()
        print("\nupdate success")

def add_teacher(id,name,grade,sub):                    #add teacher details
     try:
        file=open("teacher_data1.txt",'a')
        file.write(id+'\t'+name+'\t'+grade+'\t'+sub)
        file.write("\n")
     finally:
        file.close()
        print("\nteacher data added sucessfully")

def add_student(id,name,grade,m1,m2,m3,m4,m5):          #add student details
     try:
        file=open("student_data1.txt",'a')
        file.write(id+'\t'+name+'\t'+grade+'\t'+m1+'\t'+m2+'\t'+m3+'\t'+m4+'\t'+m5)
        file.write("\n")
     finally:
        file.close()
        print("\nstudent data added sucessfully")

def search_teacher(id):                                   #search for the teacher
     flag=1
     try:
        file=open("teacher_data1.txt",'r')
        for data in file.readlines():
           data=data.strip()
           l=list(data.split('\t'))
           if l[0]==id:
              flag=1
              print("\n--details found--")
              print("name:",l[1])
              print("id:",l[0])
              print("grade:",l[2])
              print("sub:",l[3])
           else:
              flag=0
     except FileExistsError:
        print("above file doesn't exists,you are directed to main menu")
        call()
     finally:
        file.close()
     if flag!=1:
           print("\nnot found")

def valid_student(id):                                   #validity of student to check whether he is appropriate to create login id and password
   flag=1
   try:
      file=open("student_data1.txt",'r')
      for data in file.readlines():
         data=data.strip()
         l=list(data.split('\t'))
         if l[0]==id:
            flag=1
            print("valid student of the school")
            return True
         else:
            flag=0
   except FileExistsError:
        print("above file doesn't exists,you are directed to main menu")
   finally:
      file.close()
   if flag!=1:
      print("not a valid student")
      return False

def valid_teacher(id):                                       #validity of student to check whether he is appropriate to create login id and password
   flag=1
   try:
      file=open("teacher_data1.txt",'r')
      for data in file.readlines():
         data=data.strip()
         l=list(data.split('\t'))
         if l[0]==id:
            flag=1
            print("valid teacher of the school")
            return True
         else:
            flag=0
   except FileExistsError:
        print("above file doesn't exists,you are directed to main menu")
   finally:
      file.close()
   if flag!=1:
      return False
             
   
def search_student(id):                               #search for student
     flag=1
     try:
        file=open("student_data1.txt",'r')
        for data in file.readlines():
           data=data.strip()
           l=list(data.split('\t'))
           if l[0]==id:
              flag=1
              print("\n--details found--")
              print("name:",l[1])
              print("id:",l[0])
              print("grade:",l[2])
              print("mark1:",l[3])
              print("mark2:",l[4])
              print("mark3:",l[5])
              print("mark4:",l[6])
              print("mark5:",l[7])
              return True
           else:
              flag=0
     except FileExistsError:
        print("above file doesn't exists,you are directed to main menu")
        call()         
     finally:
        file.close()
     if flag!=1:
        print("\nnot found")
        return False
def login_admin():                                        #login function for admin
     uid=input("enter the userid")
     pwd = input("enter the password")
     if pwd=="admin" and uid=="admin":
          print("welcome admin\n---MENU OF ADMIN---")
          print("\n'as'-add student\n'ss'-search student\n'at'-add teacher\n'st'-search teacher\n'dis'-display student\n'dit'-display teacher\n'us'-update_student\n'ut'-update_teacher\n'ds'-delete student\n'dt'delete teacher\n'e'-exit to main menu")
          ch=input("enter the choice from menu of admin")
          while ch!='e':
               menu(ch)
               ch=input("enter the choice from menu of admin")
          call()     
          
     else:
          print("\nwrong credentials")

def create_pwd_teacher():                                   #create password for teacher
     uid=input("enter the new user id")
     pwd=input("enter the new password(atleast 6 characters and must have a special characters)")
     if valid_password(pwd):
        try:
           file=open("teacher_pwd1.txt",'a')
           file.write(uid+','+pwd)
           file.write("\n")
        except FileExistsError:
           print("above file doesn't exists,you are directed to main menu")
           call()   
        finally:
           file.close()
        print("\nuser id and password created successfully")
        print("\nyou can login now again with the new credentials")
     else:
        print("password has no necessary characters")
        login_teacher()
def login_teacher():                             #login for teacher
     flag=0
     print("\n---login teacher menu----")
     print("\n1.create pwd(default pwd and id is 'teacher')\n2.login\n")
     ch=input("enter choice from teacher login menu or else enter any key to go back to main menu of system")
     if ch=='1':
               uid=input("enter the default userid")
               pwd = getpass.getpass(prompt="enter deafault password")
               if uid=='teacher' and pwd=='teacher':
                    print("\nyou need to update id and password,now you are directed to create your own id and password")
                    id=input("enter your school id")
                    if (valid_teacher(id)):
                       create_pwd_teacher()
                       login_teacher()
                    else:
                       print("not a valid student")
                       login_teacher()
               else:
                    print("\nwrong credentials")
                    login_teacher()
     elif ch=='2':
          uid=input("enter the userid")
          pwd =input("enter the password")
          file=open("teacher_pwd1.txt",'r')
          for data in file.readlines():
               data=data.strip()
               l=list(data.split(','))
               if l[0]==uid and l[1]==pwd:
                    flag=1
                    print("\nsuccessfully logged in\nhello:",l[0])
                    print("\n---MENU OF TEACHER---s\n'as'-add student\n'ss'-search student\n'us'-update_student\n'ds'-delete student\n'e'-exit to main ")
                    ch=input("enter the choice from menu of student")
                    while ch!='e':
                         if ch=='ss' or ch=='e' or ch=='as' or ch=='us' or ch=='ds':
                              menu(ch)
                              ch=input("enter the choice from menu of teacher")
                         else:
                              print("wrong choice")
                              ch=input("enter the choice from menu of teacher")
                    call()   
                         
          if flag!=1:
               print("\ninvalid credentials")
               login_teacher()
     else:
        call()

                    
def create_pwd_student():                  #create password for student        
     uid=input("enter the new user id")
     pwd=input("enter the new password(atleast 6 characters and must have a special characters)")
     if (valid_password(pwd)):
        try:
           file=open("student_pwd1.txt",'a')
           file.write(uid+','+pwd)
           file.write("\n")
        finally:
           file.close()
        print("\nuser id and password created successfully")
        print("\nnow you can login again with the new credentials")
     else:
        print("password has no necessary characters")
        login_student()
def login_student():                             #login for student
     flag=0
     print("\n---login student menu----")
     print("\n1.create pwd(default pwd and id is 'student'\n2.login\n")
     ch=input("enter choice or else enter any key to go back to main menu of system")
     if ch=='1':
               uid=input("enter the default userid")
               pwd = getpass.getpass(prompt="enter deafault password")
               if uid=='student' and pwd=='student':
                    print("\nyou need to update id and password,now you are directed to create your own id and password")
                    id=input("enter your school id")
                    if (valid_student(id)):
                       create_pwd_student()
                       login_student()
                    else:
                       print("not a valid student")
                       login_student()
               else:
                    print("\nwrong credentials")
                    login_student()
     elif ch=='2':
          uid=input("enter the userid")
          pwd =input("enter the password")
          file=open("student_pwd1.txt",'r')
          for data in file.readlines():
               data=data.strip()
               l=list(data.split(','))
               if l[0]==uid and l[1]==pwd:
                    flag=1
                    print("\nsuccessfully logged in\nhello:",l[0])
                    print("\n---MENU STUDENT---\n'ss'-search student\n'e'-exit to main menu")
                    ch=input("enter the choice from menu of student")
                    while ch!='e':
                         if ch=='ss' or ch=='e':
                              menu(ch)
                              ch=input("enter the choice from menu of student")
                         else:
                              print("wrong choice")
                              ch=input("enter the choice from menu of student")
                    call()   
                         
          if flag!=1:
               print("\ninvalid credentials")
               login_student()
     else:
        call()
        
def menu(ch):                                             #menu for the operation for various actions to be taken
     if ch=='as':
          name=input("enter the name of student")
          id=input("enter id")
          g=input("enter the grade")
          m1,m2,m3,m4,m5=input("enter marks with commas").split(',')
          add_student(id,name,g,m1,m2,m3,m4,m5)
     elif ch=='ss':
          id=input("enter the id to search")
          search_student(id)
          
     elif ch=='at':
          name=input("enter the name of teacher")
          id=input("enter id")
          grade=input("enter the grade")
          sub=input("enter the sub")
          add_teacher(id,name,grade,sub)
     elif ch=='st':
          id=input("enter the id to search")
          search_teacher(id)
     elif ch=='us':
          id=input("enter the id to update student")
          m1,m2,m3,m4,m5=input("enter the new marks").split(',')
          update_student(id,m1,m2,m3,m4,m5)
     elif ch=='ut':
          id=input("enter the id to update subject")
          sub=input("enter the subject to change")
          update_teacher(id,sub)
     elif ch=='ds':
          id=input("enter id to delete")
          delete_student(id)
     elif ch=='dt':
          id=input("enter id to delete")
          delete_teacher(id)
     elif ch=='dis':
          display_student()
     elif ch=='dit':
          display_teacher()
          


def call():                                                #main calling function which will drive your main menu
     print("----MENU OF THE SYSTEM------")
     print("\n1.login as admin\n2.login as student\n3.login as teacher\n4.studentfile display\n5.teacherfile_dispaly\n6.exit the system")
     ch=input("\nenter your choice above or else enter 6 to exit")
     if ch=='1':
        login_admin()           
     elif ch=='2':
        login_student()               
     elif ch=='3':
        login_teacher()               
              
     elif ch=='4':
        display_student()
        call()           
               
     elif ch=='5':
        display_teacher()
        call()
     else:
        print("\nthank you for visiting student management system!!!!!")
        pass
               
               
print("----------------------------welcome to student management sysytem----------------------------")
call()      #program start


# In[ ]:




