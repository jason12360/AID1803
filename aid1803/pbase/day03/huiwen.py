s = input('请输入一段文字：')
print('您输入的是回文') if s == s[::-1] else print('您输入的不是回文')