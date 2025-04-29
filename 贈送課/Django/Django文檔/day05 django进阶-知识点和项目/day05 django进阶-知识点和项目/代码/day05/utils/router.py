class DemoRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.model_name in ["role", 'depart']:
            return "bak"
        if model._meta.model_name in ["userinfo"]:
            return "default"

    def db_for_write(self, model, **hints):
        if model._meta.model_name in ["role", 'depart']:
            return "bak"
        if model._meta.model_name in ["userinfo"]:
            return "default"

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # python manage.py migrate app01 --database=default
        # python manage.py migrate app01 --database=bak
        # True  ->生成到数据库
        # False -> 不生成

        if db == 'bak':
            if model_name in ["role", 'depart']:
                return True
            else:
                return False

        if db == 'default':
            if model_name in ['userinfo']:
                return True
            else:
                return False
