from typing import Union
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("FAKE_VALUE")
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_form():
    html_content = """
    <!DOCTYPE html>
<html>
<head>
	<title>下載 Excel 檔案</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<style>
		body {
			font-family: Arial, Helvetica, sans-serif;
			margin: 0;
			padding: 0;
		}

		.container {
			padding: 20px;
			display: flex;
			flex-direction: column;
			align-items: center;
		}

		.form-control {
			margin-bottom: 10px;
			width: 100%;
			padding: 10px;
			border: 1px solid #ccc;
			border-radius: 5px;
			box-sizing: border-box;
			font-size: 16px;
			resize: vertical;
		}

		.form-control:focus {
			border-color: #007bff;
			outline: none;
		}

		.btn {
			background-color: #007bff;
			color: #fff;
			padding: 10px 20px;
			border: none;
			border-radius: 5px;
			cursor: pointer;
			font-size: 16px;
		}

		.btn:hover {
			background-color: #0069d9;
		}
	</style>
</head>
<body>
	<div class="container">
		<h1>下載 Excel 檔案</h1>
		<form>
			<label for="name">姓名</label>
			<input type="text" id="name" class="form-control">

			<label for="date">日期</label>
			<input type="date" id="date" class="form-control">

			<label for="content">內容</label>
			<textarea id="content" class="form-control"></textarea>

			<button type="button" class="btn" onclick="downloadExcel()">下載</button>
		</form>
	</div>

	<script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.17.3/xlsx.full.min.js"></script>
	<script>
		function downloadExcel() {
			// 取得填寫的資料
			var name = document.getElementById("name").value;
			var date = document.getElementById("date").value;
			var content = document.getElementById("content").value;

			// 建立 Excel 物件
			var wb = XLSX.utils.book_new();
			var ws = XLSX.utils.json_to_sheet([
				{name: name, date: date, content: content}
			]);
			XLSX.utils.book_append_sheet(wb, ws, "Sheet1");

			// 將 Excel 物件轉換成 Blob 物件
			var wbout = XLSX.write(wb, {type: "array", bookType: "xlsx"});
			var blob = new Blob([wbout], {type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"});

			// 建立下載連結
			var url = URL.createObjectURL(blob);
			var link = document.createElement("a");
			// 綁定下載連結
			link.href = url;

			// 設定下載檔案的名稱
			link.download = "data.xlsx";

			// 模擬點擊下載連結
			link.click();

			// 釋放 Blob 物件佔用的記憶體
			URL.revokeObjectURL(url);
		}
	</script>
</body>
</html>

    """
    return html_content

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}