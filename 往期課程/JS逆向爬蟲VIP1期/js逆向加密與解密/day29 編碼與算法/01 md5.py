from hashlib import md5,sha1,sha256,sha512
from base64 import b64encode

data=b"123456"
salt=b"11111"
# obj=md5(salt)
obj=md5()
obj.update(data)
# e10adc3949ba59abbe56e057f20f883e 長度 32
print(obj.hexdigest(),"長度",obj.hexdigest().__len__())

obj=sha1()
obj.update(data)
# 7c4a8d09ca3762af61e59520943dc26494f8941b 長度 40
print(obj.hexdigest(),"長度",obj.hexdigest().__len__())

obj=sha256()
obj.update(data)
# 8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92 長度 64
print(obj.hexdigest(),"長度",obj.hexdigest().__len__())

obj=sha512()
obj.update(data)
# ba3253876aed6bc22d4a6ff53d8406c6ad864195ed144ab5c87621b6c233b548baeae6956df346ec8c17f5ea10f35ee3cbc514797ed7ddd3145464e2a0bab413 長度 128
print(obj.hexdigest(),"長度",obj.hexdigest().__len__())