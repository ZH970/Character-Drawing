#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 11:38
# @Author  : ZH970
# @File    : Character drawing.py
# @Software: PyCharm

from PIL import Image
import tkinter

# 考虑后期加一个按比例缩放
widght = 70
Height = 20
image = str(input("Image:"))
# ASCII替换字符集
Ascii_char = list(
    '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'. '
)


# 彩色 黑白选择框
top = tkinter.Tk()

colors = ['Colorful', "Black & White"]
list_color = tkinter.Listbox(top)
for item in colors:
    list_color.insert(tkinter.END, item)

def a():
    if list_color.get(list_color.curselection()) is 'Colorful':
        top.destroy()
    elif list_color.get(list_color.curselection()) is 'Black & White':
        top.destroy()


bt = tkinter.Button(top, text='OK', command=a, width=5)


bt.pack()
list_color.pack()
top.mainloop()

# 将256灰度映射到70个字符上
def get_char(r, g, b, alpha=256):  # alpha透明度
    if alpha == 0:
        return ' '
    length = len(Ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)  # 计算灰度
    unit = (256.0 + 1) / length
    return Ascii_char[int(gray / unit)]  # 不同的灰度对应着不同的字符
    # 通过灰度来区分色块


if __name__ == '__main__':
    im = Image.open(image)
    im = im.resize((widght, Height), Image.NEAREST)
    txt = ""
    for i in range(Height):
        for j in range(widght):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'
    print(txt)
