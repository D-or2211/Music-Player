import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("600x800")
canvas.config(bg= 'pink')

rootpath = "C:\\Users\\user\\Documents\\APRENDIENDO\\musicPlayer\\musica"
pattern = "*.mp3"

mixer.init()

prev_img = tk.PhotoImage(file = "prev_img.png")
stop_img = tk.PhotoImage(file = "stop_img.png")
play_img = tk.PhotoImage(file = "play_img.png")
pause_img = tk.PhotoImage(file = "pause_img.png")
next_img = tk.PhotoImage(file = "next_img.png")

def select():
	label.config(text = listBox.get("anchor"))
	mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
	mixer.music.play()

def stop():
	mixer.music.stop()
	listBox.select_clear('active')

def play_next():
	next_song = listBox.curselection()
	next_song = next_song[0] + 1
	next_song_name = listBox.get(next_song)
	label.config(text = next_song_name)

	mixer.music.load(rootpath + "\\" + next_song_name)
	mixer.music.play()

	listBox.select_clear(0, 'end')
	listBox.activate(next_song)
	listBox.select_set(next_song)

def play_prev():
	next_song = listBox.curselection()
	next_song = next_song[0] - 1
	next_song_name = listBox.get(next_song)
	label.config(text = next_song_name)

	mixer.music.load(rootpath + "\\" + next_song_name)
	mixer.music.play()

	listBox.select_clear(0, 'end')
	listBox.activate(next_song)
	listBox.select_set(next_song)

def pause_song():
	if pauseBtn["text"] == "Pause":
		mixer.music.pause()
		pauseBtn["text"] = "Play"
	else:
		mixer.music.unpause()
		pauseBtn["text"] ="Pause" 


listBox = tk.Listbox(canvas,fg ="#79FF42", bg ="black", width = 100, font =('ds-digital', 14))
listBox.pack(padx =15, pady=15)

label = tk.Label(canvas, text ='', bg = 'red', fg = 'white', font = ('dis-digital', 18))
label.pack(pady= 15)

top = tk.Frame(canvas, bg = "black")
top.pack(padx = 10, pady = 5, anchor = 'center')


prevBtn = tk.Button(canvas, text = "Previous", image= prev_img, bg='black', borderwidth = 0, command = play_prev)
prevBtn.pack(pady = 15, in_ = top, side = 'left')

stopBtn = tk.Button(canvas, text = "Stop", image= stop_img, bg='black', borderwidth = 0, command = stop)
stopBtn.pack(pady = 15, in_ = top, side = 'left')

playBtn = tk.Button(canvas, text = "Play", image= play_img, bg='black', borderwidth = 0, command= select)
playBtn.pack(pady = 15, in_ = top, side = 'left')

pauseBtn = tk.Button(canvas, text = "Pause", image= pause_img, bg='black', borderwidth = 0, command =pause_song)
pauseBtn.pack(pady = 15, in_ = top, side = 'left')

nextBtn = tk.Button(canvas, text = "Next", image= next_img, bg='black', borderwidth = 0, command = play_next)
nextBtn.pack(pady = 15, in_ = top, side = 'left')


for root, dirs, files in os.walk(rootpath):
	for filename in fnmatch.filter(files, pattern):
		listBox.insert('end', filename)     


canvas.mainloop()





