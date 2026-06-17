from blog.home.models import Category, Article, SiteConfig,User
from random import randint
def get_homepage_payload():
    site_info = SiteConfig.query.first()
    featured_posts = (
        Article.query.filter_by(is_published=True, is_featured=True)
        .order_by(Article.created_at.desc())
        .limit(3)
        .all()
    )
    latest_posts = (
        Article.query.filter_by(is_published=True)
        .order_by(Article.created_at.desc())
        .limit(6)
        .all()
    )
    categories_count = Category.query.count()
    total_views = Article.query.with_entities(Article.view_count).all()

    hero = {
        "title": site_info.hero_title if site_info else "个人博客首页",
        "subtitle": site_info.hero_subtitle if site_info else "欢迎来到我的博客。",
        "meta": ["CELESTIAL BEING", "GN-DRIVE", "BLOG HOME"],
    }
    stats = {
        "posts": Article.query.filter_by(is_published=True).count(),
        "categories": categories_count,
        "views": sum(item[0] for item in total_views),
    }
    sidebar = {
        "about_text": site_info.about_text if site_info else "这里展示博客简介。",
        "timeline": [
            {"period": "2026-06", "text": "首页模板完成，支持白天与黑夜外置主题。"},
            {"period": "2026-05", "text": "完成博客首页信息结构拆分与视觉草案。"},
        ],
    }

    titles = [
        "写下所见，记录所想，奔赴所爱",
        "在快速变化的世界里，保持持续表达",
        "愿每一次仰望，都能照见更远的自己",
    ]
    banners = [
        {
            "title": titles[randint(0,len(titles)-1)],
            "subtitle": "技术、创作与热爱，最终都会留下自己的痕迹",
            "image": "4a5aa17b2c522b9d90d78356c5b512b8.jpg",
        },
        {
            "title": titles[randint(0,len(titles)-1)],
            "subtitle": "输出不是喧哗，而是对成长最诚实的整理",
            "image": "8c10b1a3730b90066ae3ec4fdd67c980.jpeg",
        },
        {
            "title": titles[randint(0,len(titles)-1)],
            "subtitle": "博客不是终点，而是一条不断延展的个人轨道",
            "image": "d18699f07c874b2726825ec8267c52e7.jpg",
        },
    ]
    try:
        author_info = User.query.filter_by(username="woson").first()
    except Exception:
        print("未获取到作者信息")

    return {
        "site_info": site_info,
        "hero": hero,
        "stats": stats,
        "featured_posts": featured_posts,
        "latest_posts": latest_posts,
        "sidebar": sidebar,
        "banners": banners,
        "author_info": author_info,
    }
