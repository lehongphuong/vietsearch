# vietsearch
VietSearch python engineer code challenges

=>> Bài 1, 2, 3 em làm Bằng Jupyter Notebook anh vào file p1.ipynb là sẻ thấy hoặc có thể xem source em copy ra file p123.py

=>> Bài 4 em làm bằng scrapy. project ở trong thư mục khoahoc. Vì tất cả data của categories đó tới 55691 no crawl rất lâu, nên em chỉ lấy 2268 để test nội dung data lưu trong file khoa-hoc.json

=>> bài 5, 6 em làm trong 2 thư mục mydatabaseES chứa database, em settup Elasticsearch bằng docker composer cho nhanh nên anh chỉ cần vào thư mục đó chạy docker-composer up là được
Còn api thì em làm bằng django framework có thể chạy bằng docker composer hoặc bình thường cũng được. Chạy bình thường anh cần install các thư viện của nó bằng cách chạy lệnh sau:
    => pip install -r requirements.txt
Sau đó start server django lên bằng lệnh: 
    => python manage.py runserver

=>>>>> Và anh có thể test các api với thông tin như sau:
Sẽ đọc all data from file khoa-hoc.json rồi insert vào index articles của ES(Data get được rất nhiều khoảng 55691 record nên file json load không nỗi nên em chỉ lấy 2268 record trong https://vnexpress.net/khoa-hoc để test)
insertAllDataFromJSON
	Method Get
	
createDataArticles 
	Method Post:
	Data Post:	{
					"title": "Vụ va chạm thiên hà tạo ra 'bóng ma' vũ trụ",
					"content": "phuong create",
					"public_date": "Thứ năm, 31/10/2019, 00:00 (GMT+7)",
					"id": 1
				}
				
readDataArticles 
	Method Post:
	Data Post: 	{
					"id": 111
				}	
	
readManyDataArticles  
	Method Post:
	Data Post: [
					{
						"id": 1
					},
					{
						"id": 2
					}
				]
	
readAllDataArticles 
	Method Get
	
updateDataArticles  
	Method Post:
	Data Post:	{
					"title": "Vụ va chạm thiên hà tạo ra 'bóng ma' vũ trụ",
					"content": "phuong Update",
					"public_date": "Thứ năm, 31/10/2019, 00:00 (GMT+7)",
					"id": 1
				}
deleteDataArticles   
	Method Post:
	Data Post:	{
					"id": 1
				} 
deleteManyDataArticles
	Method Post:
	Data Post: 	[
					{
						"id": 1
					},
					{
						"id": 2
					}
				]

Về search thì có thể tryền đủ data 3 property hoặc 1 trong 3 điều được		
searchDataArticles
	Method Post:
	Data Post: 	{
					"title": "Vụ va chạm thiên hà tạo ra 'bóng ma' vũ trụ",
					"content": "phuong Update",
					"public_date": "Thứ năm, 31/10/2019, 00:00 (GMT+7)"
				}
  