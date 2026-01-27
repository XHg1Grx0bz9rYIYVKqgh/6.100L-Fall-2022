## ⚠️ 代码修正 / Fixes

由于 `unittest.makeSuite` 在较新的 Python 版本中已被移除，运行 `test_ps2_student.py` 时可能会报错。请按以下方式修改代码：

**文件位置**: `test_ps2_student.py` (第 465 行)

```diff
- suite.addTest(unittest.makeSuite(TestPS2))
+ suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestPS2))
```