# 猜數字大冒險 🚀

歡迎來到猜數字大冒險！這是一個簡單而有趣的遊戲，你可以透過調整設定檔中的數字範圍，挑戰自己的數學直覺！

## 🎮 如何開始

1. **安裝 Python:**
   如果你已經有 Python，恭喜你！如果沒有，請前往 [Python 官方網站](https://www.python.org/downloads/) 下載並安裝。

2. **Clone 專案:**
   在冒險之前，先複製這個專案到你的冒險目的地。
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

3. **執行遊戲:**
   啟動遊戲冒險，輸入以下指令，開始探險吧！
   ```bash
   python main.py
   ```

   如果你想讓冒險更方便，也可以使用 `pyinstaller` 工具將遊戲打包成一個獨立的冒險檔。
   ```bash
   pyinstaller --onefile main.py
   ```

4. **調整設定:**
   想要挑戰更大的數字或者增加冒險次數嗎？修改 `settings.xml` 檔案，調整 `<x1>`、`<x2>` 和 `<max_attempts>` 的值。

## 🚀 開始冒險吧！

這不是一場普通的數字遊戲，而是一場數學大冒險！你將在數字的海洋中遨遊，嘗試找到那個隱藏的寶藏數字。是時候展現你的數學功底，成為真正的冒險家！

## ⚙️ 遊戲設定

`settings.xml` 檔案是你的設定寶藏，打開它，發現更多有趣的冒險設定。

```xml
<settings>
    <x1>1</x1>
    <x2>100</x2>
    <max_attempts>10</max_attempts>
</settings>
```

- `<x1>`: 冒險的數字海洋起點。
- `<x2>`: 冒險的數字海洋終點。
- `<max_attempts>`: 你的冒險次數上限。
