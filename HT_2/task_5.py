"""
5. Write a script which accepts a decimal
number from user and converts it to hexadecimal.
"""

h = hex(int(input()))  #конвертуємо введене число в шістнадцяткову систему
print(h[2:])           #виводимо число без спец. символів на початку (якщо потрібно)