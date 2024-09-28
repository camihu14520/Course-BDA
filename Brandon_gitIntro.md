1.安裝VScode和Git

2.Git基本設定與初始化

在終端機輸入Git設定指令:

git --version(確認電腦有無安裝到Git)
git config --global user.name "使用者"(設定使用者名稱)
git config --global user.email "email"(設定使用者email)

git init(初始化，將資料夾變更為有版本控制管理功能的資料夾)

3.Git檔案狀態

git status(檢查目錄中每個檔案的狀態)
git add 檔案名稱(可將未追蹤的檔案變更為可追蹤，未追蹤的檔案Git不會去紀錄)
git commit -m "必須附帶簡短訊息"(上傳的指令)
git add .(將當前目錄中所有變更都放到暫存區)

4.檢視提交紀錄與檔案還原

git log(列出先前commit過的所有歷史紀錄，按下q可離開檢視模式)
git log --oneline(git log簡化版，適合快速瀏覽過去的提交紀錄，每個上傳點有自己的id編號)
git diff id編號 --檔案名稱(比較新舊版本內容差異)
git checkout 欲還原點的id --檔案名稱(將檔案還原至先前的版本，需要用commit提交後才會將檔案還原)
git reset --hard 欲還原點的id(將所有檔案還原至先前的版本，此操作不可逆，建議先做備份)

刪除檔案需再git add 檔案名稱，並commit一次

5.忽略檔案清單

在目錄內建立一個叫.gitignore的檔案，將不需要進行版控的檔名或副檔名寫在裡面，這樣能避免無關的檔案混到Git儲存庫中)

6.GitHub同步儲存庫

可以透過GitHub這個協作平台，讓我們把在本地的Git資料夾備份到GitHub，可以指定儲存庫要設定為私人或公開。
設定好後，GitHub有提供現成的指令協助我們把本地的檔案上傳到雲端，第一行是用來連結本地和遠端的儲存庫，第二行是把原來的master
改成main，第三行是把本地位於main分支的資料上傳至雲端，上傳完成後就能在GitHub上看到所有已上傳的檔案，也能看到所有commit紀錄，
之後要做版本更新，只需再加git push指令就能上傳到GitHub。

7.加入協作者至專案

GitHub建立專案者可以透過輸入帳號名稱或email邀請其他人成為此專案的協作者，擁有對此專案的存取和修改權。
如欲將專案下載到本地端可以將儲存庫的網址複製下來，再VScode的終端機中輸入git clone 網址，就能將儲存庫下載到本地端。
如此專案有push新檔案時，協作者只要輸入git pull指令就能將新檔案拉到自己的電腦。

8.建立分支

git checkout -b 新分支名稱
git push origin 剛建立的分支名稱(建立好分支修改好要push回去的指令)