import tkinter as tk
from tkinter import TclError, ttk


def change_option(option):
    print(option)


def create_input_frame(container):
    frame = ttk.Frame(container)

    # grid layout for the input frame
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=3)

    # Age
    ttk.Label(frame, text="Enter Age:").grid(column=0, row=0, sticky=tk.W)
    keyword = ttk.Entry(frame, width=10)
    keyword.focus()
    keyword.grid(column=1, row=0, sticky=tk.W)

    # Options
    options = [
        "koponya",
        "koponya-mellkas",
        "koponya-mellkas-has",
        "koponya-mellkas-has-kismedence",
        "mellkas",
        "mellkas-has-kismedence",
        "has-kismedence",
        "embolia",
    ]
    clicked = tk.StringVar()
    clicked.set("koponya")

    dropdown = ttk.OptionMenu(
        frame,
        clicked,
        *options,
        command=change_option,
    )
    #
    dropdown.grid(column=0, row=1, sticky=tk.W)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame


def create_button_frame(container):
    frame = ttk.Frame(container)

    frame.columnconfigure(0, weight=1)

    ttk.Button(frame, text="Find Next").grid(column=0, row=0)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame


def create_main_window():
    root = tk.Tk()
    root.title("Effektív dózis kalkulátor ver. 1.0")  # Elnevezzük
    root.resizable(0, 0)
    try:
        # windows only (remove the minimize/maximize button)
        root.attributes("-toolwindow", True)
    except TclError:
        print("Not supported on your platform")

    root.columnconfigure(0, weight=4)
    root.columnconfigure(1, weight=1)

    input_frame = create_input_frame(root)
    input_frame.grid(column=0, row=0)

    button_frame = create_button_frame(root)
    button_frame.grid(column=1, row=0)
    root.mainloop()


def other():
    # window.geometry("500x400")  # Megadjuk a méretét
    # window.configure(bg="#f5edec")
    tk_bg = "#f5edec"
    font_bold = "Helvetica 14 bold"
    font_regular = "Helvetica 14 bold"

    options = [
        "koponya",
        "koponya-mellkas",
        "koponya-mellkas-has",
        "koponya-mellkas-has-kismedence",
        "mellkas",
        "mellkas-has-kismedence",
        "has-kismedence",
        "embolia",
    ]

    clicked = tk.StringVar()
    clicked.set("koponya")

    # TOP FRAME
    frame = ttk.Frame(
        master=window,
        height=10,
        width=10,
    )
    frame.pack(
        fill=tk.BOTH,
        side=tk.TOP,
    )
    # FAME 1
    frame1 = ttk.Frame(
        master=window,
        width=50,
        height=50,
    )
    label_a = ttk.Label(
        frame1,
        text="Üdvözlöm!",
        font=font_bold,
    )
    label_a["padding"] = (5, 5, 5, 5)
    label_a.grid()
    frame1.pack(
        fill=tk.BOTH,
        side=tk.LEFT,
        expand=True,
    )

    # FAME 2
    frame2 = ttk.Frame(
        master=window,
        width=20,
        height=50,
    )
    frame2.pack(
        fill=tk.BOTH,
        side=tk.LEFT,
        expand=True,
    )
    dropdown = ttk.OptionMenu(
        frame2,
        clicked,
        *options,
        command=change_option,
    )
    #
    dropdown.grid()

    # Label0 = tk.Label(
    #    text="Üdvözlöm!",
    #    font=font_bold,
    #    bg=tk_bg,
    # )
    # Label0.grid(
    #    row=2,
    #    column=2,
    # )
    # beköszönő szöveg

    #
    # Label1 = tk.Label(
    #    window,
    #    text="Select the option type:",
    #    font=tk_font_regular,
    #    bg=tk_bg,
    # )
    # Label1.grid(row=4, column=0)
    #
    # Label2 = tk.Label(
    #    window,
    #    text="TEST",
    #    font=tk_font_regular,
    #    bg=tk_bg,
    # )
    # Label2.grid(row=5, column=0)
    #
    # Label2b = tk.Label(
    #    window,
    #    text="TEST",
    #    font=tk_font_regular,
    #    bg=tk_bg,
    # )
    # Label2b.grid(row=6, column=0)

    # Application Settings

    ## Application Output


if __name__ == "__main__":
    create_main_window()
