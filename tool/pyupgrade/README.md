# pyupgrade

A tool (and pre-commit hook) to automatically upgrade syntax for newer versions of the language.

## 使用

### Used

    pip install -r requirements.txt

#### commod

    # 初始化
    pre-commit install
    # change any 'test.py' content
    git add test.py
    # 用pre-commit检查并修改所有git文件
    pre-commit run --all-files
