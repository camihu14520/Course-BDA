# Git安裝與基本功能
# Part 1 VSCode and Git 安裝 
VSCode 下載網頁：https://code.visualstudio.com/  
    第一步找適合自己電腦版本的下載安裝  
    第二步不想看英文把它弄成中文  
        1.最左邊那排找到四個小正方形圖案  
        2.尋找 Chinese  
        3.下載它 套用它  
        4.不會參照附圖 (VSCode_language.png)  
    第三步設定工作資料夾  
        1.左邊那排檔案總管  
        2.開啟資料夾名稱隨意  
        3.設定完後許多工作都會在這個資料夾下

Git下載網頁： https://git-scm.com/downloads 
    Windows 安裝：找適合自己電腦版本的下載安裝  
    Mac 安裝：  
        第一步按下 Command + 空白鍵叫出 Spotlight  
        第二步 Terminal 打開終端機介面  
        第三步在終端機裡輸入 xcode-select --install  
        第四步同意並安裝它  
    檢查有沒有安裝成功  
        第一步回到 VSCode 看上面工具列找到終端機新增終端機  
        第二步在跳出來的視窗中輸入 git --version  
        第三步有跳出版本代表成功  
        許多 Git 指令都會在終端機輸入執行

# Part 2 Git 基本設定
設定姓名與電子郵件，Git 在儲存版本變更時也會儲存作者資訊  
設定姓名：git config -- global user.name "你的名字"  
設定郵件：git config -- global user.email "你的 email"

目前設定完的資料夾只是普通的資料夾，要將它轉成可以記錄版本變更的資料夾要輸入指令：git init

若是嫌棄終端機的指令太多眼花撩亂，可以輸入 clear 指令清空終端機內容

# Part 3 Git 檔案狀態
建立檔案  
    第一步在工作區右鍵>新增檔案建立 Markdown格式的文件  
    第二步在右上的文字輸入區貼上想貼的內容

檢查檔案狀態  
    第一步在終端機內輸入 git status  
    第二步終端機內會顯示未追蹤的檔案(紅字)  
        1.此類檔案 Git 並不會紀錄檔案變更歷史

追蹤檔案  
    第一步輸入指令 git add 想要追蹤的檔案檔名  
    第二步看在工作資料夾下的檔案狀態從 U變成 A  
        1.此時代表檔案已被加入追蹤清單  
        2.用檢查檔案指令此時會變成綠字  
        3.如果想要一次加入多個檔案可以用空白連接 git add 想要追蹤的檔案檔名1(空白鍵)想要追蹤的檔案檔名2  
        4.如果要一次把所有變更過的檔案追蹤可以輸入 git add .

記錄檔案  
    第一步輸入指令 git commit -m "記錄名"  
        1.每次紀錄檔案都要給它一個紀錄的名字  
        2.此時檔案就被記錄了  
        3.git紀錄是對檔案的所有變更操作，包括刪除也算一種操作會被記錄

檢查紀錄  
    詳細記錄：輸入指令 git log  
        這時終端機會列出過去提交過的紀錄點，包括提交者資訊和時間  
    簡易紀錄：輸入指令 git log　--oneline  
        此時終端機只會列出記錄點， (HEAD -> master) 代表最新的紀錄點

比較紀錄  
    在終端機輸入：git diff 想比較的紀錄點的編號 -- 檔名  
        此時終端機會回傳比較紀錄點與現在紀錄點的差異

還原紀錄  
    方法一終端機輸入：git checkout 想還原的紀錄點的編號 -- 檔名  
        此變動一樣需要為它新增紀錄點  
        新增記錄點後檔案就會回到當時的狀態  
        雖然檔案被還原但所有的變更都有紀錄，這種還原是可逆的
    
    方法二終端機輸入：git reset -- hard 想還原的紀錄點的編號  
        注意這種方法是將整個檔案還原到某個時間點，這種還原是不可逆的

忽略檔案  
    如果不想要某個不重要的檔案被記錄可以在工作區新增一個 .gitignore 的當按把想被忽略的檔案名或副檔名寫進去  
    裡面的檔案就不會被 git 紀錄

# Part 4 GitHub
Git 與 GitHub 的差異  
    Git：Git 是一個檔案版本管理系統，用來追蹤文件與檔案變更  
    GitHub：GitHub 是一個雲端協作平台，可以讓使用者在雲端開發與協作

GitHub 網站：https://github.com/

# Part 5 連結 VSCode 裡的資料到 GitHub 
同步資料到 GitHub  
    第一步登入 GitHub 帳號  
    第二步在主頁面左邊建立儲存庫  
    第三步在後續頁面底部可以找到現成的指令把 VSCode 連結到 GitHub  
        1.用來連接本地儲存庫指令：git remote add origin 網址  
        2.將主線分支取名為 main 指令：git branch -M main  
        3.將本地位於 main 的資料推送到雲端指令：git push -u origin main  
        4.到 GitHub 重整頁面就可以看到推送的資料  
        5.在 Commit 這個頁面也可以看到過往提交的版本變更紀錄

# Part 6 下載與推送資料在 GitHub 與 VSCode ，專案共編
從 VSCode 推送資料到 GitHub  
    使用指令：git push

在 GitHub 上共編  
    1.打開設定，可以找到 Collaborators  
    2.輸入想邀請共編人的 email  
    3.這樣就可以讓對方共編項目

從 GitHub 下載資料到 VSCode  
    1.在 GitHub 上複製項目網址  
    2.回到 VSCode 輸入指令：git clone 複製的網址  
    3.這樣 VSCode 就會下載 GitHub 上的項目  
    4.要注意下載後的項目是放在工作區的子資料夾  
    5.想要開始編輯要輸入指令來切換工作區：cd 資料庫名  
    6.有了第一次連接後續只要輸入指令 git pull 就可以一直保持同步

# Part 7 開設分支
如果想編輯又怕修改到原本的資料，可以開設分支在分支上編輯  
    1.開設分支指令 git checkout -b 分支名  
    2.開設分支一樣可以用之前的指令來紀錄檔案變更  
    3.將分支推送指令：git push origin 分支名
    4.可以利用 GitHub 上的 pull request 來合併項目

