## Excel 다루기


```bash
$ conda install openpyxl
```

```python
from openpyxl import Workbook

# 엑셀파일 쓰기
write_wb = Workbook()
# 이름이 있는 시트를 생성
write_ws = write_wb.create_sheet('생성시트')
# Sheet1에다 입력
write_ws = write_wb.active
write_ws['A1'] = '숫자'
#행 단위로 추가
write_ws.append([1,2,3])
#셀 단위로 추가
write_ws.cell(5, 5, '5행5열')
write_wb.save("./number.xlsx")

from openpyxl import load_workbook
# data_only=True로 해줘야 수식이 아닌 값으로 받아온다. 
load_wb = load_workbook("./number.xlsx", data_only=True)
# 시트 이름으로 불러오기 
load_ws = load_wb['Sheet']
# 셀 주소로 값 출력
print(load_ws['E5'].value)

```
