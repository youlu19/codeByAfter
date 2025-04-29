class Request(object):

    def get_p(self):
        return 123

    def set_p(self, value):
        pass

    POST = property(get_p, set_p)

    @property
    def FILES(self):
        return 123


request = Request()
# print(request.POST)
# request.POST = 999


print(request.FILES)
