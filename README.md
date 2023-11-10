# 猜數字遊戲

這是一個簡單的猜數字遊戲，玩家需要在指定的範圍內猜一個隨機生成的數字。遊戲參數可以透過 `settings.xml` 設定檔進行修改。

## 開始遊戲

1. **安裝 Python:**
   請確保你的電腦已安裝 Python。你可以從 [Python 官方網站](https://www.python.org/downloads/) 下載和安裝最新的 Python 版本。

2. **Clone 專案:**
   在終端機中使用以下指令複製專案到你的本地環境。
   ```
   git clone https://github.com/your-username/your-repository.git
   ```

3. **執行遊戲:**
   進入專案目錄，執行 `main.py` 檔案。
   ```
   cd your-repository
   python main.py
   ```

   如果你想要創建獨立的執行檔，可以使用 `pyinstaller` 工具，詳細步驟請參閱前述的說明。

4. **調整遊戲設定:**
   若要修改遊戲的範圍和嘗試次數，請編輯 `settings.xml` 檔案，調整 `<x1>`、`<x2>` 和 `<max_attempts>` 的值。

## 遊戲設定

`settings.xml` 檔案包含了遊戲的相關設定，你可以根據自己的需求進行調整。

```xml
<settings>
    <x1>1</x1>
    <x2>100</x2>
    <max_attempts>10</max_attempts>
</settings>
```

- `<x1>`: 數字範圍的下限。
- `<x2>`: 數字範圍的上限。
- `<max_attempts>`: 玩家可以嘗試猜測的最大次數。
