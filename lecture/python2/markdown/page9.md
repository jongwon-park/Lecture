## 크롤링

- csv파일로 저장


```python
# 앞의 코드에 이어서
import csv

filename = "네이버 영화 순위.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)
i = 1
for item in data:
  writer.writerow([i, item])
  i += 1
f.close()
```