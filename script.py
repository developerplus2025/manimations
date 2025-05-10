from textual.widgets import Button
from textual.app import App
import inquirer
from colorama import Fore, Back, Style
from random import randint
from asciimatics.screen import Screen
import questionary
import re
import keyboard
from tqdm import tqdm
from halo import Halo
from alive_progress import alive_bar
import time
from tqdm import *
from time import sleep
import numpy as np
import pandas as pd
from tqdm.rich import trange
from tqdm.auto import tqdm
from rich.progress import Progress, TextColumn, BarColumn, TaskProgressColumn
from urllib.request import urlopen
from rich.progress import wrap_file
response = urlopen("https://floravf.vercel.app/")
size = int(response.headers["Content-Length"])

with wrap_file(response, size) as file:
    for line in file:
        print(line.decode("utf-8"), end="")
        sleep(0.1)


def tqdm_pandas(t):
    from pandas.core.frame import DataFrame

    def inner(df, func, *args, **kwargs):
        t.total = groups.size // len(groups)

        def wrapper(*args, **kwargs):
            t.update(1)
            return func(*args, **kwargs)
        result = df.apply(wrapper, *args, **kwargs)
        t.close()
        return result
    DataFrame.progress_apply = inner


response = urlopen("https://floravf.vercel.app/")
size = int(response.headers["Content-Length"])
with Progress(
        TextColumn("[bold white]Progress 1[/]"),
        BarColumn(bar_width=None, complete_style="green"),
        TaskProgressColumn(style="bold red"),  # Đổi màu 100% tại đây
) as progress:
    task = progress.add_task("Progress 1", total=100)
    for i in range(100):
        progress.update(task, advance=1)
        sleep(0.01)
for i in trange(100, colour="cyan", desc="[bold white]Progress 1[/]"):
    sleep(0.01)
print("")

for i in trange(500, colour="green", desc="Progress 2"):
    sleep(0.001)
print("")

for i in trange(300, colour="magenta", desc="Progress 3"):
    sleep(0.001)
print("")
spinner = Halo(text='Loading', spinner='dots', color="cyan")

spinner.start()
time.sleep(0.2)
spinner.stop()
questions = [
    inquirer.Text('name', message="What's your name"),
    inquirer.Text('surname', message="What's your surname"),
    inquirer.Text('phone', message="What's your phone number",
                  validate=lambda _, x: re.match('\+?\d[\d ]+\d', x),
                  )
]
answers = inquirer.prompt(questions)
request = questionary.select(
    "What do you want to do?",
    choices=[
        'Calculator Axis Of Symmetry Of Parabol',
        'Solve Quadratic Equation',
        'Animated Video Graph'
    ]).ask()  # returns value of selection
if request == "Calculator Axis Of Symmetry Of Parabol":
    print(Fore.RED, "Calculator Axis Of Symmetry Of Parabol", Fore.GREEN)
    a = float(input("Enter your coefficient a: "))
    b = float(input("Enter your coefficient b: "))
    c = float(input("Enter your coefficient c: "))
    axis_of_symmetry_x = -b/(2*a)
    axis_of_symmetry_y = -(b**2-4*a*c) / 4*a
    print(
        Fore.RED, f"Axis of symmetry is : ({axis_of_symmetry_x};{axis_of_symmetry_y})")
elif request == "Solve Quadratic Equation":
    print("Comming Soon")
else:
    print("Comming Soon")
