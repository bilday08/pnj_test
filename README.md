# Customer Data Platform

## Mô tả
Dự án Customer Data Platform tích hợp dữ liệu khách hàng từ một SQL database và một RESTful API, 
chuẩn hóa và lưu trữ vào MongoDB (NoSQL).

## Phân tích bài toán
- Tích hợp dữ liệu khách hàng từ 2 nguồn: SQL (SQLite) và RESTful API
- Hợp nhất (normalize + deduplicate) thành 1 định dạng schema chuẩn
- Lưu trữ dữ liệu kết quả vào một NoSQL DB (MongoDB)
- Đảm bảo bảo mật, và dễ mở rộng

## Công nghệ sử dụng
| Thành phần     | Công nghệ                          |
|----------------|----------------------------------- |
| Ngôn ngữ chính | Python 3.12                        |
| SQL Extractor  | SQLite3 (`sqlite3` module)         |
| API Extractor  | REST client (`requests`)           |
| Chuẩn hóa      | Pandas                             |
| NoSQL Loader   | MongoDB (`pymongo`)                |
| API mock       | FastAPI (`mock_api.py`)            |
| Cấu hình       | `.env`, `config/settings.py`       |

## Kiến trúc tổng thể
![Customer Data Flow](https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Untitled%20Diagram.drawio&dark=auto#R%3Cmxfile%3E%3Cdiagram%20name%3D%22Page-1%22%20id%3D%223ciJk4QldlKrogkZa6mH%22%3E3Vjfb9owEP5rIm0PrZK4UHgkwNZJoHWj2tanyU2uiVcnjoxTyP76nROHJAT6Q6Iq7AV8n31n33eXzwGLjOP1Z0nTaC4C4JZrB2uLTCzXvRz08VMDeQn0HKcEQsmCEmoAC%2FYXDGgbNGMBLFsLlRBcsbQN%2BiJJwFctjEopVu1l94K3d01pCB1g4VPeRX%2ByQEUlOujZNX4FLIyqnR3bzMS0WmyAZUQDsWpAZGqRsRRClaN4PQauuat4Kf0%2B7ZndHExCol7iEJLF%2FIFfxb8zrzeWiySX6seZifJIeWYSXnybITChit7RJZijq7ziA7NI9TCVwoclkuutIqZgkVJfwytsAsQiFXO0HBzeUf8hlCJLgq%2BZ4iwBg5uNQSpY783I2fCE%2FQUiBiVzXFI5EENtvmWv6ko5Ff1Ro0p9g1HTHOEmdM0fDgyFr6DT7dD5fbq4uc%2B04%2Bj6y1GzSY6OzUoDGoRBgE%2BnMYVUkQhFQvm0Rr2CHNBhbbTqNTMhUkPWH1AqN1JDMyXaFMOaqV%2Fa%2FbxnrNvGzGRtIhdGXhkJ5ttw0uZtc652K6zKr8xPJ%2FV00ZADkUkfniCLGHGkMgT1xLrh7iaQwKlij%2B1zHLyipPN8TG%2B03MxoDhK%2FP1znWK9E5%2BtLlqrlR8vtc0zHC9gjDkM9PMPpcZRZU8fyRtZoqJdHwhoTa%2BQUnhHEUPnhMRuue6LNCmc71t5VWMePdK54c2UpZz6So8%2F1iqBzmqYsCfWlwwBvHSxrpPfxhvq8xTaeNSLpvqBbnd%2Fu62dk4g3E1b3sygHZJQeDt5KDixNUg4FDWnpwbveekYTCugbJkDR8Jg6uE%2B4LdYK8p070TrDUzmCwVeq69u9Ua%2BcUan3ZvRPWSlJ8l9%2FuARQz1S4Z5SxMcOwjNZpAT0seijUfmYmYBUHRHbsEs90xB9BM197STKermf0dkkneSjIH%2Fw%2B3F8fG7bDD7VwkoZh0r%2B5jest3t671i%2Fd%2Fy%2B%2F%2BBp0JGpxeh7rDNrVkxxvTgToUzfqPg2Ku8e8Lmf4D%3C%2Fdiagram%3E%3C%2Fmxfile%3E)

## Cách chạy

1. Di chuyển vào thư mục project
    ```bash
    cd pnj_test

2. Tạo virtual env
    ```bash
    python -m venv venv
    source venv/bin/activate    

3. Cài thư viện
    ```bash
    pip install -r requirements.txt

4. Chạy mock REST API:
    ```bash
    uvicorn mock_api:app --reload