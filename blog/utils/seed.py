from blog.home.models import Category, Article, SiteConfig, Tag, User, db


def seed_demo_data():
    if Article.query.first():
        return

    admin = User(
        username="woson",
        display_name="Woson",
        email="woson@example.com",
        bio="专注于 Flask、动漫风前端和个人创作型项目。",
    )

    design = Category(name="前端设计", description="界面、动效与视觉表达")
    backend = Category(name="Flask", description="Flask 项目结构与后端实践")
    notice = Category(name="公告", description="站点公告与阶段记录")

    tag_design = Tag(name="前端设计")
    tag_flask = Tag(name="Flask")
    tag_notice = Tag(name="公告")
    tag_theme = Tag(name="主题切换")

    posts = [
        Article(
            title="高达00式首页视觉：如何把科技感写进博客",
            summary="通过冷色渐变、玻璃拟态与 HUD 线框建立首页识别度，让内容展示与动漫世界观风格形成统一表达。",
            content="""<p>本篇文章介绍如何通过冷色渐变、半透明面板、滚动横幅与微交互动效，为个人博客建立强辨识度的未来科技感首页。</p><p>在实现上，推荐将基础布局抽离到基模板，将主题变量统一托管在样式层，再通过视图层逐步替换掉硬编码内容。</p>""",
            cover_image="https://images.unsplash.com/photo-1542051841857-5f90071e7989?auto=format&fit=crop&w=1200&q=80",
            is_featured=True,
            view_count=1200,
            author=admin,
            category=design,
            tags=[tag_design, tag_theme],
        ),
        Article(
            title="Flask 博客首页组件组织方式",
            summary="采用头图、文章流与侧栏三段结构，既保持极简，也方便后续把文章、作者和统计信息替换成模板变量。",
            content="""<p>首页可以拆为 Hero、文章列表、侧栏、页脚四层结构。页面专属数据由视图层传入，公共信息由上下文统一注入。</p><p>这样既适合早期快速开发，也便于后续接入数据库与后台管理。</p>""",
            cover_image="https://images.unsplash.com/photo-1520975693416-35a6bbba3d50?auto=format&fit=crop&w=1200&q=80",
            is_featured=True,
            view_count=886,
            author=admin,
            category=backend,
            tags=[tag_flask],
        ),
        Article(
            title="站点公告：新版动漫风首页已上线",
            summary="保留必要博客组件并加入动画光效，使模板既能直接展示，也能作为后续博客首页开发的基础骨架。",
            content="""<p>新版首页已经上线，当前重点工作转向应用工厂、数据模型和文章阅读链路的实现。</p><p>后续将继续补充后台入口、评论模块与站点设置能力。</p>""",
            cover_image="https://images.unsplash.com/photo-1541877944-ac82a091518a?auto=format&fit=crop&w=1200&q=80",
            is_featured=False,
            view_count=640,
            author=admin,
            category=notice,
            tags=[tag_notice],
        ),
    ]

    site_config = SiteConfig(
        site_name="WNBlog",
        site_subtitle="动漫感与技术感结合的个人博客",
        site_description="围绕 Flask、前端设计与个人创作过程沉淀内容。",
        footer_text="Powered by Flask · Designed for day & night themes",
        hero_title="机动战士高达00风格博客首页",
        hero_subtitle="通过未来面板、滚动横幅与主题切换效果，展示文章、项目记录与站点公告。",
        about_text="本站以动漫视觉语言为灵感，记录技术实现、设计思路与个人项目实践。",
    )

    db.session.add(admin)
    db.session.add_all([design, backend, notice, tag_design, tag_flask, tag_notice, tag_theme, site_config])
    db.session.add_all(posts)
    db.session.commit()
