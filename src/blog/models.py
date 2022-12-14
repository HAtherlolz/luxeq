from tortoise import fields
from tortoise.models import Model


class Article(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=50, index=True)
    image = fields.CharField(max_length=500, null=True, blank=True)
    writer = fields.CharField(max_length=50)
    category = fields.ForeignKeyField("models.Category", related_name="article", on_delete=fields.SET_NULL, null=True)
    time_of_read = fields.SmallIntField()
    date_created = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Block(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=50)
    article = fields.ForeignKeyField("models.Article", related_name="block", on_delete=fields.CASCADE)

    def __str__(self):
        return self.title


class Paragraph(Model):
    id = fields.IntField(pk=True)
    paragraph = fields.TextField()
    block = fields.ForeignKeyField("models.Block", related_name="paragraph", on_delete=fields.CASCADE)

    def __str__(self):
        return self.paragraph[:10]
