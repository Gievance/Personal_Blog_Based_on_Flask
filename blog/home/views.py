from flask import abort, flash, redirect, render_template, request, url_for

from blog.home.models import Article, SiteConfig, User, Category, db
from blog.home.services import get_homepage_payload
from . import home


@home.route('/')
def index():
    payload = get_homepage_payload()
    site_info = payload["site_info"]
    page_title = f"{site_info.site_name} - {site_info.site_subtitle}" if site_info else "WNBlog"
    return render_template("home.html", page_title=page_title, **payload)

@home.route('/posts/<int:pid>')
def post_detail(pid):
    post = Article.query.filter_by(id=pid, is_published=True).first()
    if not post:
        abort(404,description=f"文章 {pid} 不存在")

    try:
        post.view_count += 1
        db.session.commit()
    except Exception:
        db.session.rollback()

    site_info = SiteConfig.query.first()
    page_title = f"{post.title} - {site_info.site_name if site_info else 'WNBlog'}"
    return render_template("post_detail.html", post=post, site_info=site_info, page_title=page_title)

@home.route('/admin/posts/new', methods=['GET', 'POST'])
def create_post():
    categories = Category.query.order_by(Category.name.asc()).all()

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        summary = request.form.get('summary', '').strip()
        content = request.form.get('content', '').strip()
        category_id = request.form.get('category_id', type=int)
        cover_image = request.form.get('cover_image', '').strip()
        is_featured = bool(request.form.get('is_featured'))

        if not title or not summary or not content or not category_id:
            flash('请完整填写标题、摘要、正文和分类。', 'error')
            return render_template('post_form.html', categories=categories, page_title='新建文章')

        author = User.query.first()
        category = Category.query.get(category_id)
        if not author or not category:
            flash('作者或分类不存在，请先检查基础数据。', 'error')
            return render_template('post_form.html', categories=categories, page_title='新建文章')

        post = Article(
            title=title,
            summary=summary,
            content=content,
            cover_image=cover_image,
            is_featured=is_featured,
            author=author,
            category=category,
        )
        db.session.add(post)
        db.session.commit()
        flash('文章创建成功。', 'success')
        return redirect(url_for('home.post_detail', pid=post.id))

    return render_template('post_form.html', categories=categories, page_title='新建文章')

@home.get('/about')
def about():
    return render_template("about.html")