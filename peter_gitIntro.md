1. 建立 GitHub 帳號
前往 GitHub 網站。
點擊右上角的 Sign Up 按鈕。
輸入你的 Email、密碼，並選擇使用者名稱。
確認 Email 驗證後，你將成功建立 GitHub 帳號。
2. 安裝 Git
如果尚未安裝 Git，可以從 Git 官方網站 下載並安裝。

3. 設定 Git 使用者
使用 Git 前，你需要設定使用者資訊，以便 Git 可以將變更記錄到正確的人名下。

bash
複製程式碼
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
4. 初始化 Git 倉庫
bash
複製程式碼
# 進入專案目錄
cd your-project-directory

# 初始化一個 Git 倉庫
git init
此命令會在該目錄中建立一個 .git 資料夾，開始管理該專案的版本控制。

5. 新增檔案並提交
bash
複製程式碼
# 檢查當前 Git 狀態
git status

# 新增檔案到暫存區
git add <檔案名稱>   # 可以是特定檔案，如 git add README.md
git add .             # 或新增所有變更

# 提交變更
git commit -m "提交訊息"   # 如 git commit -m "初次提交"
6. 將本地倉庫連接到 GitHub
進入 GitHub，並建立一個新倉庫（Repository）。
在本地端執行以下指令，將倉庫連接到 GitHub：
bash
複製程式碼
# 連接遠端倉庫（將網址替換為你的 GitHub 倉庫 URL）
git remote add origin https://github.com/username/repository.git

# 推送本地倉庫到 GitHub
git push -u origin master
7. 使用 git checkout 切換分支
bash
複製程式碼
# 查看所有分支
git branch -a

# 切換到其他分支
git checkout branch_name

# 建立並切換到新分支
git checkout -b new_branch_name
這些指令能幫助你在本地和 GitHub 之間進行基本的 Git 操作。如果你想進行更多進階的功能，如合併、衝突解決等，未來可以再進一步學習。