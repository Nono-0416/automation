這是一個使用 Python + Selenium + Pytest 實作的自動化測試專案，針對 Practice Test Automation (https://practicetestautomation.com/practice-test-login/)網站 執行登入登出測試且支援 Chrome 與 Firefox。

📂專案結構
automation/
├── conftest.py                           # 共用設定
├── requirements.txt                      # 套件需求
├── run_all.py                            # 手動本地跑 Chrome/Firefox 測試
├── utils.py                              # 截圖工具
├── pages/
│   ├── login_page.py                     # Page Object：登入頁
│   └── secure_area_page.py               # Page Object：登入成功後頁面
├── tests/
│   ├── test_login_success.py             # 成功登入測試
│   ├── test_login_failure.py             # 帳密錯誤測試
│   └── test_logout.py                    # 登出測試
└── screenshots/                          # 截圖儲存位置


🚀 快速開始

✅ 安裝套件
pip install -r requirements.txt

✅ 執行測試（Chrome 預設）
pytest

✅ 指定瀏覽器（Chrome / Firefox）
pytest --browser=firefox

✅ 一次跑兩個瀏覽器
python run_all.py


📸 自動截圖

每個測試步驟都會截圖，並儲存於 screenshots/ 資料夾，命名包含：測試名稱。
時間戳記範例：login_failure_20250612_153251.png


📌 測試場景

1.成功登入檢查
2.帳號輸入錯誤，錯誤訊息檢查
3.密碼輸入錯誤，錯誤訊息檢查
4.成功登出檢查
