from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=30,verbose_name='出版社名')
    address = models.CharField(max_length=50,verbose_name='地址')
    city = models.CharField(max_length=20,verbose_name='城市')
    country = models.CharField(max_length=20,verbose_name='国家')
    website = models.URLField(verbose_name='出版社网址')

    class Meta:

        db_table = 'publisher'
        verbose_name = '出版社'
        verbose_name_plural = '出版社'

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50,verbose_name='书名')
    publicate_date = models.DateField(verbose_name='出版时间')
    publisher = models.ForeignKey(Publisher,verbose_name='出版社',null=True)

    class Meta:
        db_table = 'book'
        verbose_name = '书籍'
        verbose_name_plural = '书籍'
        ordering = ['-publicate_date']

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=30,verbose_name='作者名')
    age = models.IntegerField(verbose_name='年龄')
    email = models.EmailField(null=True,verbose_name='电子邮箱')
    isActive = models.BooleanField(default=True,verbose_name='是否激活')
    book = models.ManyToManyField(Book,verbose_name='书籍')
    publisher = models.ManyToManyField(Publisher,verbose_name='出版社')
    # 声明内部类来定义当前类在管理页面中的展现形式
    class Meta:
        # 修改当前表名为author
        db_table = 'author'
        verbose_name = '作者'
        verbose_name_plural = '作者'
        ordering = ['-age']

    def __str__(self):
        return self.name



class Wife(models.Model):
	name = models.CharField(max_length=30)
	age = models.IntegerField()
	#增加一个1对1的引用,引用自Author实体
	author = models.OneToOneField(Author,null=True,related_name='w')
	def __str__(self):
		return self.name

	class Meta:
		db_table='wife'
		verbose_name='夫人'
		verbose_name_plural = verbose_name
