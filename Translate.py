from tkinter import *
# from tkinter import ttk # For future purposes
from translate import Translator


# Translation code
def Translation():
    translator = Translator(from_lang=Inputlang.get(), to_lang=Outputlang.get())
    translation = translator.translate(sentenceVar.get())
    OutputVar.set(translation)


# Same as translation code but switched the input and output languages
def Switch():
    translator = Translator(from_lang=Outputlang.get(), to_lang=Inputlang.get())
    translation = translator.translate(sentenceVar.get())
    OutputVar.set(translation)


# The structure of the Window of the app
Window = Tk()
Window.title("Translator")
Window.geometry("450x150")

# Variables to show for tkinter
Inputlang = StringVar()
Outputlang = StringVar()

# array for the languages the user can choose from 
Choiceslang = ('Arabic', 'Bengali', 'Chinese', 'English', 'French', 'German', 'Hindi', 'Indonesian', 'Japanese',
               'Portuguese', 'Russian', 'Spanish', 'Urdu')

# for the first menu it'll be empty
Inputlang.set('')
Outputlang.set('')

# The menu which you choose the language you want to write with
InputMenu = OptionMenu(Window, Inputlang, *Choiceslang)
Label(Window, text="Input Language").grid(row=0, column=0)
InputMenu.grid(row=1, column=0)

# The menu which you choose the langauge you want to be translated to
OutputMenu = OptionMenu(Window, Outputlang, *Choiceslang)
Label(Window, text="Output Language").grid(row=0, column=2)
OutputMenu.grid(row=1, column=2)

# The area to write down what you want to translate
Label(Window, text="Enter Text").grid(row=2, column=0)
sentenceVar = StringVar()
Entry(Window, textvariable=sentenceVar).grid(row=2, column=1)

# The area that the translating outputs
Label(Window, text="Translate").grid(row=3, column=0)
OutputVar = StringVar()
Entry(Window, textvariable=OutputVar).grid(row=3, column=1)

# The button you press for the translation to start
startbtn = Button(Window, text="Translate", command=Translation, relief=GROOVE)
startbtn.grid(row=2, column=2, columnspan=3)

# The switch button (to switch the languages)
# ex. English to Spanish
# after clicking the switch button Spanish to English (Still testing it)
switchbtn = Button(Window, text="⇌", command=Switch, )
switchbtn.grid(row=1, column=1)

# It runs python's GUI
Window.mainloop()
