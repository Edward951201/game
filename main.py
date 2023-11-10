import random
import xml.etree.ElementTree as ET

def load_settings(file_path="settings.xml"):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        x1 = int(root.find("x1").text)
        x2 = int(root.find("x2").text)
        max_attempts = int(root.find("max_attempts").text)
        return x1, x2, max_attempts
    except FileNotFoundError:
        print(f"找不到設定檔 {file_path}，使用預設值。")
        return 1, 100, 10
    except Exception as e:
        print(f"讀取設定檔時發生錯誤: {e}")
        return 1, 100, 10

def start_game(x1, x2, max_attempts):
    target_number = random.randint(x1, x2)
    attempts = 0

    print(f"遊戲開始！你有 {max_attempts} 次猜測的機會，目標數字在 {x1} 到 {x2} 之間。")

    while attempts < max_attempts:
        guess = int(input("請猜一個數字："))

        if guess == target_number:
            print(f"恭喜！你猜對了，目標數字就是 {target_number}。")
            break
        elif guess < target_number:
            print("太低了，再試一次。")
        else:
            print("太高了，再試一次。")

        attempts += 1
        remaining_attempts = max_attempts - attempts
        print(f"剩餘猜測次數：{remaining_attempts}")

    if attempts == max_attempts:
        print(f"抱歉，你已經猜了 {max_attempts} 次，遊戲結束。正確答案是 {target_number}。")

# 設定遊戲參數
x1, x2, max_attempts = load_settings()

# 啟動遊戲
start_game(x1, x2, max_attempts)
