import yagmail

# start server
mail = yagmail.SMTP(user="*****@163.com", password="***", host="smtp.163.com")

# do send
mail.send(to="zhoujy2019@163.com", subject="这是主题", contents="这是内容")
