from tkinter import *
from check_html import *

root = Tk()

user_data = Entry(width = 20, bg = 'PaleTurquoise')
user_data.grid(row = 0, column = 0)

result_label = Label(text = '-', width = 20)
result_label.grid(row = 0, column = 2)

def find_result(event):
	user_tags = []
	if len(user_data.get()) > 0:
		user_tags = delete_excess(user_data.get())
		result = check_double_tags(user_tags)
		result_label['text'] = str(result)

button_result = Button(text = "find result")
button_result.grid(row = 0, column = 1)
button_result.bind('<1>', find_result)

root.geometry('500x300')
root.mainloop()