from tkinter import Tk, simpledialog, messagebox

window = Tk()
window.withdraw()

if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements
    happy = simpledialog.askstring(title='question', prompt="Are You Happy?")

    if happy == 'yes':
        print("Keep doing whatever you're doing")


    thing = simpledialog.askstring(title='not happy', prompt="Do You Want To Be Happy?")

    if happy == 'no':
        print(thing)

    if thing == 'yes':
        print("Change Something")

    if thing == 'no':
        print("Keep Doing Whatever You're Doing")

    pass
