class multipleFunctions():  
    def BMI():
        BMI=int(input("Enter the BMI index:"))
        if(BMI<18.5):
            print("underweight")
            message="underweight"
        elif(BMI<24.9):
            print("Normal")
            message="Normal"
        elif(BMI<29.9):
            print("over weight")
            message="over weight"
        else:
            print("very overweight")
            message="very overweight"
        return message
    def list_ai_fields():
        print("AI subfields they are:")
        ai_fields = ["Machine Learning,Neural Networks",
                     "Computer Vision",
                     "Robotics",
                     "Speech Processing",
                     "Natural Language Processing"]
        for field in ai_fields:
            print(field)

    def oddEven():
        num=int(input("Enter a number:"))
        if((num%2)==1):
            print("52452 is odd number")
            message="52452 is odd number"
        else:
            print("52452 is Even number")
            message="52452 is Even number"
            return message
    def percentage():
        subj1 = 98
        print("subject1 =", subj1)
        subj2 = 87
        print("subject2 =", subj2)
        subj3 = 95
        print("subject3 =", subj3)
        subj4 = 95
        print("subject4 =", subj4)
        subj5 = 93
        print("subject5 =", subj5)

        total_marks = subj1 + subj2 + subj3 + subj4 + subj5
        print("Total Marks:", total_marks)

        percent = total_marks / 5
        print("Percentage:", percent)
        return percent

    def triangle(): 
        height = 32
        print("Height:", height)
        breadth = 34
        print("Breadth:", breadth)
        area = (height * breadth) / 2
        print("Area formula:(height * breadth) / 2")
        print("Area of triangle:", area)
        height1 = 2
        print("Height1:", height1)
        height2 = 4
        print("Height2:", height2)
        breadth = 4
        print("Breadth:", breadth)
        print("Perimeter of triangle:height1 + height2 + breadth")
        area = height1 + height2 + breadth
        print("Perimeter of triangle:", area)
        return area
    def marriageEligibility(Male=21,Female=18):
        age=int(input("your Genter:"))

        if(Female<18):
            print("eligible")
            message="eligible"
        elif(Male<21):
            print("eligible")
            message="eligible"
        else:
            print("Not eligible")
            message="Not eligible"
        return message