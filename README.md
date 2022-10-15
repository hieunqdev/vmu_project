# VMU - Project
---
Ứng dụng tra cứu thông tin cho học viên Sau đại học thuộc viện đào tạo Sau đại học - trường Đại học Hàng Hải Việt Nam.

## Cài đặt:
---
**1.Clone the Repo**
`git clone https://github.com/hieunqdev/vmu_project.git`

**2.Setup venv & Install Requirements**
```
python3 -m venv venv
source venv/bin/activate
cd vmu
pip install -r requirements.txt
```

**3.Migrate Database**
```
python manage.py makemigrations 
python manage.py migrate
```

**5.Start Server**
`python manage.py runserver`
