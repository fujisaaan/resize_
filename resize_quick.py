# リサイズ用（まとめてできるやつ・クイック版）
import tkinter as tk
from tkinter import ttk
from tkinterdnd2 import *

class Application(tk.Frame):
  def __init__(self,master = None):
    super().__init__(master)
    master.geometry("300x300")
    master.title("雛形")


def main():
  root = TkinterDnD.Tk()
  app = Application(master=root)
  app.mainloop()


if __name__ == '__main__':
  main()
