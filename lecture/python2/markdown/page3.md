## 계산기 클래스 만들기

- 클래스 구상하기
  - 함수이름
  - 데이터 입력(set_data)
  - 연산 : 더하기(add), 빼기(sub), 곱하기(mul), 나누기(div)

<font size="6">

```python
## calculator.py
class Calculator:
   def set_data(self, input1, input2): # 데이터 입력
      self.input1 = input1
      self.input2 = input2

   def add(self):
      return self.input1 + self.input2

   def sub(self):
      return self.input1 - self.input2
   ...
```
</font>