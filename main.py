from tkinter import *
from plu import *

PADX = 20
PADY = 10

#---- ROOT -------

root = Tk()
root.title("PLU ALDI")
root.resizable(False, False)

#----- FRAMES -------

radio_frame = Frame(root)
radio_frame.pack(padx=PADX, pady=PADY)
radio_frame.config(relief="groove", bd=2)

buttons_frame = Frame(root)
buttons_frame.pack(padx=PADX, pady=PADY)

#----- RADIOS --------

variable_radio = StringVar(value="vacio")

verdura_radio = Radiobutton(radio_frame, value="verdura", variable=variable_radio, text="Verdura").pack(padx=PADX, pady=PADY, anchor="w")
fruta_radio = Radiobutton(radio_frame, value="fruta", variable=variable_radio, text="Fruta").pack(padx=PADX, pady=PADY, anchor="w")
pan_radio = Radiobutton(radio_frame, value="pan", variable=variable_radio, text="Pan").pack(padx=PADX, pady=PADY, anchor="w")
otros_radio = Radiobutton(radio_frame, value="otros", variable=variable_radio, text="Otros").pack(padx=PADX, pady=PADY, anchor="w")
todo_radio = Radiobutton(radio_frame, value="todo", variable=variable_radio, text="Todo").pack(padx=PADX, pady=PADY, anchor="w")

#---- BUTTONS --------

def empezar():
	radio = variable_radio.get()
	if radio != "vacio":
		plu = Plu()
		plu.set_selection(radio)
		question = StringVar(value=plu.get_question())
		corrected = StringVar()

		new_window = Toplevel()
		new_window.resizable(False, False)
		new_window.title(radio.capitalize())
		new_window.transient(master=root)
		new_window.grab_set()

		def siguiente():
			if answer_entry["state"] == "normal":
				answer = answer_entry.get()
				correct, solution = plu.get_correction(question.get(), answer)
				if correct:
					corrected.set("Correcto: "+ solution)
					correction_label["fg"] = "blue"
				else:
					corrected.set("Incorrecto: "+ solution)
					correction_label["fg"] = "red"
				answer_entry["state"] = "disabled"
			else:
				question.set(plu.get_question())
				answer_entry["state"] = "normal"
				answer_entry.delete(0, END)
				corrected.set("")
				

		def press_return(event):
			siguiente()

		question_label = Label(new_window, textvariable=question)
		question_label.pack(padx=PADX, pady=PADY)

		correction_label = Label(new_window, textvariable=corrected)
		correction_label.pack(padx=PADX, pady=PADY)

		answer_entry = Entry(new_window)
		answer_entry.pack(padx=PADX, pady=PADY)
		answer_entry.focus()
		answer_entry.bind('<Return>', press_return)
		answer_entry.bind('<KP_Enter>', press_return)

		siguiente_button = Button(new_window, text="Siguiente", command=siguiente)
		siguiente_button.pack(padx=PADX, pady=PADY)

empezar_button = Button(buttons_frame, text="Empezar", command=empezar)
empezar_button.pack(padx=PADX, pady=PADY)

###############

root.mainloop()