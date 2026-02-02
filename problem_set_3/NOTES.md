## ⚠️ 代码修正 / Fixes

由于 `unittest.makeSuite` 在较新的 Python 版本（如 Python 3.13）中已被移除，运行 `test_ps3_student.py` 时会出现 `AttributeError`。请按以下方式修改代码：

**文件位置**: `test_ps3_student.py` (第 534 行)

```diff
-    suite.addTest(unittest.makeSuite(TestPrepData))
-    suite.addTest(unittest.makeSuite(TestWordFrequency))
-    suite.addTest(unittest.makeSuite(TestLetterFrequency))
-    suite.addTest(unittest.makeSuite(TestGetFrequentWords))
-    suite.addTest(unittest.makeSuite(TestSimilarity))
-    suite.addTest(unittest.makeSuite(TestTFIDF))
+    loader = unittest.TestLoader()
+    suite.addTest(loader.loadTestsFromTestCase(TestPrepData))
+    suite.addTest(loader.loadTestsFromTestCase(TestWordFrequency))
+    suite.addTest(loader.loadTestsFromTestCase(TestLetterFrequency))
+    suite.addTest(loader.loadTestsFromTestCase(TestGetFrequentWords))
+    suite.addTest(loader.loadTestsFromTestCase(TestSimilarity))
+    suite.addTest(loader.loadTestsFromTestCase(TestTFIDF))

```
