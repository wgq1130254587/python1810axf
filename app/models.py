from django.db import models

# Create your models here.
from django.db import models


# 基础类
class Base(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=8)

    class Meta:
        abstract = True

# 轮播图 模型类
class Wheel(Base):
    class Meta:
        db_table = 'axf_wheel'

# 导航模型类
class Nav(Base):
    class Meta:
        db_table = 'axf_nav'

# 每日必够 模型类
class Mustbuy(Base):
    class Meta:
        db_table ='axf_mustbuy'

# 商品部分(分类) 模型类
class Shop(Base):
    class Meta:
        db_table = 'axf_shop'

# 商品列表
class MainShow(models.Model):
    trackid = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=20)
    brandname = models.CharField(max_length=100)

    img1 = models.CharField(max_length=100)
    childcid1 = models.CharField(max_length=20)
    productid1 = models.CharField(max_length=20)
    longname1 = models.CharField(max_length=100)
    price1 = models.CharField(max_length=10)
    marketprice1 = models.CharField(max_length=10)

    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=20)
    productid2 = models.CharField(max_length=20)
    longname2 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=10)
    marketprice2 = models.CharField(max_length=10)

    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=20)
    productid3 = models.CharField(max_length=20)
    longname3 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=10)
    marketprice3 = models.CharField(max_length=10)

    class Meta:
        db_table = 'axf_mainshow'

class Foodtype(models.Model):

    typename = models.CharField(max_length=100)
    trackid = models.CharField(max_length=20)
    childtypenames = models.CharField(max_length=256)
    typesort = models.IntegerField()

    class Meta:
        db_table = 'axf_foodtype'

# 商品 模型类
# 分类 》》 子类
class Goods(models.Model):
    # 商品ID
    productid = models.CharField(max_length=10)
    # 商品图片
    productimg = models.CharField(max_length=100)
    # 商品名字
    productname = models.CharField(max_length=100)
    # 商品长名字
    productlongname = models.CharField(max_length=100)
    # 是否精选
    isxf = models.IntegerField()
    # 是否买一送一
    pmdesc = models.IntegerField()
    # 规格
    specifics = models.CharField(max_length=100)
    # 价格
    price = models.DecimalField(max_digits=6, decimal_places=1)
    # 超市价格
    marketprice = models.DecimalField(max_digits=6, decimal_places=1)
    # 分类id
    categoryid = models.IntegerField()
    # 子类id
    childcid = models.IntegerField()
    # 子类名称
    childcidname = models.CharField(max_length=100)
    # 详情页id
    dealerid = models.CharField(max_length=10)
    # 库存
    storenums = models.IntegerField()
    # 销售
    productnum = models.IntegerField()

    class Meta:
        db_table = 'axf_goods'