from tkinter import*

root=Tk()
root.title("Fibonacci Series")
root.geometry("600x700")

label_series=Label(root,text="Fibonacci Series - ")
label_series.pack()
label_flower=Label(root)
label_flower.pack()
label_spiral=Label(root)
label_spiral.pack()
label_sum=Label(root, text="Fibonacci Sum - ")
label_sum.pack()
def fibonacci():
    num=10
    first_num=0
    second_num=1
    sum=0
    counter=1
    
    while(counter<=num):
        label_series["text"] += str(sum) + " , "
        counter=counter+1
        first_num=second_num
        
        second_num=sum
        sum=first_num+second_num
        result=8+80
        label_sum["text"]= "Fibonacci Sum - " + str(result)
    label_flower["text"]="flower is bloomed"


btn1=Button(root,text="show fibonacci Series", command=fibonacci) 
btn1.pack()

root.mainloop()

