from time import sleep
import pyautogui

def convert_to_bincode(a):
    res = ''
    if(len(a) == 3):
        res = '0000'
    for i in a:
        q = int(i, 16)
        q = bin(q).split('b')[1]
        while len(q) < 4:
            q = '0' + q
        res += q
    print(res)
    return res

INPUT_FILE_NAME = 'code.txt'
INTERVAL = 0.1
SLEEP_TIME = 5

file = open(INPUT_FILE_NAME, "r")

start_point = '0'

print("you have " + str(SLEEP_TIME) + " secs")
sleep(SLEEP_TIME)
print("START")
for line in file.readlines():
    data = line.split()
    if len(data) == 3:
        start_point = data[0]
        data[1] = data[2]
        print(start_point, convert_to_bincode(start_point))
    adress = data[0]
    code = data[1]
    pyautogui.typewrite(convert_to_bincode(adress), INTERVAL)
    pyautogui.press('f4', interval=INTERVAL)
    pyautogui.typewrite(convert_to_bincode(code), INTERVAL)
    pyautogui.press('f5', interval=INTERVAL)


pyautogui.typewrite(convert_to_bincode(start_point), INTERVAL)
pyautogui.press('f4', interval=INTERVAL)

print("finished")