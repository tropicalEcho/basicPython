from tkinter import *
import datetime

personalJournal = {}

def getTime():
    cT = datetime.datetime.now()
    return {
        "year": cT.strftime("%Y"),
        "month": cT.strftime("%m"),
        "day": cT.strftime("%d"),
        "hour": cT.strftime("%H"),
        "minute": cT.strftime("%M"),
        "second": cT.strftime("%S"),
        "week": cT.strftime("%a")
    }

def submission(text):
    if text.strip() == "":
        return
    timeData = getTime()
    timestamp = f"{timeData['year']}-{timeData['month']}-{timeData['day']} " \
                f"{timeData['hour']}:{timeData['minute']}:{timeData['second']}"
    personalJournal[timestamp] = text
    print("Journal Entry Saved:")
    print(timestamp, ":", text)
    entry.delete(0, END)

def showEntries():
    entriesWindow = Toplevel(window)
    entriesWindow.title("Your Journal Entries")
    textArea = Text(entriesWindow, wrap=WORD, font=("Courier New", 14))
    textArea.pack(expand=True, fill=BOTH)
    for ts, entry_text in personalJournal.items():
        textArea.insert(END, f"{ts}:\n{entry_text}\n\n")

window = Tk()
window.title("personalJournal")
window.geometry("800x500")

window.configure(background="#141414")

label = Label(
    window,
    text="Welcome!",
    font=('Courier New', 16, 'bold'),
    fg='white',
    bg='black',
    relief=RAISED,
    bd=4,
    padx=16,
    pady=8
)
label.pack(pady=10)

entry = Entry(
    window,
    font=("Courier New", 16)
)
entry.pack(pady=10)

submitBtn = Button(
    window,
    text="Enter",
    command=lambda: submission(entry.get())
)
submitBtn.pack(pady=10)

showBtn = Button(
    window,
    text="Show Journal",
    command=showEntries
)
showBtn.pack(pady=10)

window.mainloop()