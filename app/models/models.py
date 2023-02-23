from tortoise import fields, Model


class User(Model):
    """ 创建user表 """
    # pk=True, 设置为主键
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=64, description="用户名")
    password = fields.CharField(max_length=128, description="登录密码")
    create_at = fields.DatetimeField(auto_now_add=True, description="创建时间")
    modify_at = fields.DatetimeField(auto_now=True, description="更新时间")