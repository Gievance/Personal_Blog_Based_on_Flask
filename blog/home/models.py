from blog import db
import slugify
from datetime import datetime
from slugify import slugify

post_tags = db.Table(
    "post_tags",
    db.Column("post_id", db.Integer, db.ForeignKey("article.id"), primary_key=True),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"), primary_key=True),
)

class TimestampMixin:
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)

class Tag(TimestampMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    slug = db.Column(db.String(120), unique=True, nullable=False)

    posts = db.relationship("Article", secondary=post_tags, back_populates="tags", lazy="dynamic")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.slug and self.name:
            self.slug = slugify(self.name)

class Article(TimestampMixin,db.Model):
    """
        id：文章主键 ID，数据库里唯一标识一篇文章，一般用于详情查询、编辑、删除。
        title：文章标题，给用户直接看到的标题文本，比如“Flask 博客首页如何设计”。
        slug：文章 URL 标识，通常由标题生成，适合放进链接里，例如 /post/flask-blog-homepage-design，要求唯一。
        summary：文章摘要，用于首页列表、卡片预览、搜索结果简介，属于正文前的简短说明。
        content：文章正文，保存完整内容，是文章最核心的文本数据。
        cover_image：文章封面图地址，通常是图片 URL 或静态资源路径，用于首页卡片或详情页头图展示。
        is_published：是否已发布。True 表示对外可见，False 表示草稿或未上线。
        is_featured：是否推荐/置顶。常用于首页精选、轮播、重点展示。
        view_count：浏览次数，记录文章被查看了多少次，常用于热门文章排序。
        author_id：作者 ID，外键字段，指向用户表里的作者记录。
        category_id：分类 ID，外键字段，表示这篇文章属于哪个分类，比如“技术”或“动漫”。
        author：作者对象关系，不只是作者 ID，而是能直接拿到对应的 class User 实例。
        category：分类对象关系，能直接拿到对应的 class Category 实例。
        tags：标签集合关系，一篇文章可以对应多个 class Tag，例如“Flask”“Python”“前端”。
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(220), unique=True, nullable=False)
    summary = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    cover_image = db.Column(db.String(500), default="", nullable=False)
    is_published = db.Column(db.Boolean, default=True, nullable=False)
    is_featured = db.Column(db.Boolean, default=False, nullable=False)
    view_count = db.Column(db.Integer, default=0, nullable=False)

    author_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)

    author = db.relationship("User", back_populates="posts")
    category = db.relationship("Category", back_populates="posts")
    tags = db.relationship("Tag", secondary=post_tags, back_populates="posts", lazy="joined")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.slug and self.title:
            self.slug = slugify(self.title)


class User(TimestampMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    display_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    bio = db.Column(db.Text, default="", nullable=False)
    user_avatar = db.Column(db.String(100),default="", nullable=True)

    posts = db.relationship("Article", back_populates="author", lazy=True)


class Category(TimestampMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    slug = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.Text, default="", nullable=False)

    posts = db.relationship("Article", back_populates="category", lazy=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.slug and self.name:
            self.slug = slugify(self.name)


class SiteConfig(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # 页面名称 site_name + site_subtitle
    site_name = db.Column(db.String(120), nullable=False, default="WNBlog")
    site_subtitle = db.Column(db.String(200), nullable=False, default="面向动漫与技术创作的个人博客")
    #
    site_description = db.Column(db.Text, nullable=False, default="记录技术、创作和项目实践。")
    header_text = db.Column(db.String(20),nullable=False,default="This is WNBlog!!")
    footer_text = db.Column(db.String(200), nullable=False, default="Powered by Flask")
    hero_title = db.Column(db.String(200), nullable=False, default="WNBlog")
    hero_subtitle = db.Column(db.Text, nullable=False, default="基于Flask实现的个人博客主页")
    about_text = db.Column(db.Text, nullable=False, default="本站聚焦技术、动漫与个人创作记录。")

