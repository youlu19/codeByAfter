from apps.api import urls

print(urls.app_name)  # 对象.成员
print(urls.url_parttens)

v1 = getattr(urls, "app_name", 123)  # urls.app_name
print(v1)

#
# path = "apps.api.urls"
# import importlib
#
# md = importlib.import_module(path)
#
# v1 = getattr(md, "url_parttens") # md.url_parttens
# print(v1)
#
# v2 = getattr(md, "app_name") # md.app_name
# print(v2)
