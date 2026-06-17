# 博客项目下一步完善计划

## 1. 目标说明

当前项目已经具备以下基础能力：

- 首页展示
- 文章详情页展示
- 文章创建页面基础表单
- 白天 / 黑夜主题切换
- Banner 与站点配置基础展示
- 初始化种子数据

下一步应从“可持续开发”的角度继续完善，重点不只是补功能，还要同步补齐：

- 需求说明文档
- 数据模型设计文档
- 视图与接口文档
- 状态流转与权限边界文档
- 测试与初始化策略文档

本计划聚焦两件事：

1. 明确下一阶段要补充哪些功能与技术结构
2. 基于这些功能继续检查目前容易遗漏的设计点

---

## 2. 下一阶段建议追加的功能

### 2.1 文章系统完善

建议优先补齐文章模块的完整生命周期。

#### 建议追加功能

- 文章编辑
- 文章删除
- 文章草稿保存
- 文章发布 / 下线切换
- 文章列表管理页
- 文章按分类筛选
- 文章按标签筛选
- 文章分页
- 相关文章推荐
- 热门文章排序
- 搜索文章标题 / 摘要

#### 价值

这一阶段会把当前“展示型博客”推进到“可维护内容系统”。

---

### 2.2 分类与标签系统完善

当前模型中已有分类与标签关系，但业务流程还不完整。

#### 建议追加功能

- 分类管理页
- 标签管理页
- 分类创建 / 编辑 / 删除
- 标签创建 / 编辑 / 删除
- 分类详情页
- 标签详情页
- 分类文章归档页
- 标签文章归档页

#### 价值

让内容组织不再只停留在数据库层，而是具备页面层与管理层能力。

---

### 2.3 Banner 与站点配置系统

当前 Banner 更偏静态数据，建议正式建成“站点运营配置”模块。

#### 建议追加功能

- Banner 数据库读取
- Banner 管理页
- Banner 排序
- Banner 上下线状态
- Banner 跳转链接
- Banner 文案编辑
- Banner 图片替换
- SiteConfig 后台编辑页

#### 建议追加字段

Banner 建议补：

- `sort_order`
- `is_active`
- `link_url`
- `link_target`
- `description`

SiteConfig 建议补：

- `seo_title`
- `seo_keywords`
- `seo_description`
- `site_logo`
- `favicon`
- `contact_email`
- `github_url`
- `bilibili_url`

---

### 2.4 评论系统

如果要让博客具备互动能力，评论系统是下一步的重要模块。

#### 建议追加功能

- 文章评论列表
- 发表评论
- 评论审核
- 评论删除
- 回复评论
- 嵌套评论或二级评论
- 评论开关控制

#### 建议分阶段实现

第一阶段：

- 匿名评论或简化评论
- 评论审核状态

第二阶段：

- 登录后评论
- 回复链路
- 反垃圾限制

---

### 2.5 用户与权限系统

当前已有用户模型，但权限系统尚未正式建立。

#### 建议追加功能

- 登录
- 登出
- 管理员身份
- 作者身份
- 普通访客权限隔离
- 后台访问控制
- 作者只能管理自己的文章
- 管理员可以管理分类、标签、站点配置

#### 最小权限分层建议

- Visitor：只读
- Author：管理自己文章
- Admin：管理全站内容和配置

---

### 2.6 SEO 与内容运营能力

博客项目后续如果要长期使用，建议尽早补齐 SEO 与归档能力。

#### 建议追加功能

- SEO title / description 输出
- Open Graph 元信息
- sitemap.xml
- robots.txt
- 归档页
- 年 / 月归档页
- RSS 订阅

---

## 3. 建议补充的数据模型文档

下一步应在 `docs/` 中继续新增或拆分模型文档，明确每个实体职责、字段来源、关系与状态约束。

### 3.1 Article 模型文档

建议单独文档说明：

- 字段定义
- 字段用途
- 哪些字段由用户输入
- 哪些字段由系统维护
- 状态流转规则
- 发布与草稿语义
- 列表页 / 详情页 / 后台页分别依赖哪些字段

#### 建议新增字段

- `published_at`
- `deleted_at`（如果考虑软删除）
- `seo_title`
- `seo_description`
- `allow_comment`
- `status`（如果后续不再只用 `is_published`）

---

### 3.2 Banner 模型文档

建议明确：

- 图片字段保存相对路径还是完整 URL
- Banner 是否支持跳转
- 是否支持多端尺寸
- 是否支持排序和启用状态
- 是否有展示时间范围

#### 建议新增字段

- `sort_order`
- `is_active`
- `link_url`
- `start_at`
- `end_at`

---

### 3.3 Comment 模型文档

建议定义：

- 评论归属文章
- 评论作者名称 / 邮箱 / 用户 ID
- 评论审核状态
- 父评论 ID
- 回复层级限制

#### 建议字段

- `article_id`
- `user_id`
- `nickname`
- `email`
- `content`
- `status`
- `parent_id`
- `ip_address`

---

### 3.4 User 模型文档

建议补充：

- 角色字段
- 登录认证字段
- 用户头像
- 最后登录时间
- 是否禁用

#### 建议字段

- `password_hash`
- `role`
- `avatar`
- `is_active`
- `last_login_at`

---

## 4. 建议补充的视图与接口文档

下一步不应只补页面，还应把“页面入口 + 数据入口 + 表单提交入口”一并文档化。

建议在 `docs/` 下新增一份接口说明文档，至少覆盖以下内容。

### 4.1 前台页面路由

#### 首页模块

- `/`
- `/posts/<slug>`
- `/categories/<slug>`
- `/tags/<slug>`
- `/archive`
- `/search`

#### 评论提交

- `/posts/<slug>/comments`

---

### 4.2 后台管理路由

#### 文章管理

- `/admin/posts`
- `/admin/posts/new`
- `/admin/posts/<id>/edit`
- `/admin/posts/<id>/delete`
- `/admin/posts/<id>/publish`

#### 分类管理

- `/admin/categories`
- `/admin/categories/new`
- `/admin/categories/<id>/edit`

#### 标签管理

- `/admin/tags`
- `/admin/tags/new`
- `/admin/tags/<id>/edit`

#### Banner 管理

- `/admin/banners`
- `/admin/banners/new`
- `/admin/banners/<id>/edit`

#### 站点配置

- `/admin/site-config`

---

### 4.3 接口文档建议格式

每个接口建议描述：

- 路由地址
- 请求方法
- 请求参数
- 返回模板 / JSON
- 权限要求
- 成功状态
- 异常情况

例如：

#### 创建文章

- 路径：`/admin/posts/new`
- 方法：`GET` / `POST`
- 需要权限：Author / Admin
- 表单字段：`title`、`summary`、`content`、`category_id`、`cover_image`、`is_featured`
- 异常：分类不存在、作者不存在、字段为空

---

## 5. 建议补充的服务层文档

当前项目已经有服务层雏形，下一步应继续约束服务层职责。

### 建议说明内容

- 服务层只负责业务逻辑与查询拼装
- 视图层只负责请求处理与模板渲染
- 模板层只做展示，不做复杂业务判断

### 建议新增服务函数规划

#### 首页

- `get_homepage_payload()`
- `get_featured_banners()`
- `get_site_config()`

#### 文章

- `get_published_post_by_slug()`
- `get_latest_posts()`
- `get_featured_posts()`
- `create_post()`
- `update_post()`
- `delete_post()`

#### 分类 / 标签

- `get_posts_by_category()`
- `get_posts_by_tag()`

#### 评论

- `create_comment()`
- `approve_comment()`

---

## 6. 下一阶段容易遗漏的地方

这一部分非常关键，建议在正式继续开发前先逐项确认。

### 6.1 发布状态语义不完整

当前 `Article` 只有 `is_published`，但没有：

- 发布时间
- 草稿更新时间
- 下线原因
- 定时发布能力

建议后续明确文章状态设计：

- draft
- published
- archived
- deleted

---

### 6.2 图片资源规范未完全统一

当前已经开始使用本地静态图片，但还缺少统一规则。

建议补充文档说明：

- Banner 图存放目录
- 文章封面目录
- Logo / favicon 目录
- 文件命名规范
- 是否允许外链图片
- 上传后是否重命名

---

### 6.3 数据初始化策略未分层

目前 `init_db.py` 偏向一次性初始化，但后续最好拆成：

- 基础数据初始化
- 演示数据初始化
- 测试数据初始化

建议文档中说明：

- 哪些是系统必须数据
- 哪些是开发环境演示数据
- 哪些是测试专用数据

---

### 6.4 缺少统一错误处理页面

后续建议补：

- 404 页面
- 403 页面
- 500 页面
- 表单错误展示规范

---

### 6.5 缺少表单校验策略文档

当前表单校验主要写在视图函数中，后续建议文档化：

- 必填字段规则
- 文本长度限制
- slug 唯一性规则
- 图片地址合法性规则
- 分类 / 标签存在性校验

---

### 6.6 缺少测试规划文档

建议后续新增测试计划文档，至少覆盖：

- 首页渲染测试
- 文章详情测试
- 新建文章测试
- 未发布文章不可访问测试
- 分类筛选测试
- 评论创建测试
- 主题切换脚本的基础可用性验证

---

## 7. 推荐的 docs 文档拆分方案

建议后续在 `docs/` 下逐步建立如下文档：

- `docs/next_stage_plan.md`
- `docs/data_models.md`
- `docs/view_routes.md`
- `docs/admin_module_plan.md`
- `docs/comment_system_plan.md`
- `docs/testing_plan.md`
- `docs/static_asset_guidelines.md`
- `docs/seed_data_strategy.md`

---

## 8. 推荐开发顺序

建议下一阶段按下面顺序推进：

### 第一优先级

- 文章管理页
- 文章编辑 / 删除
- 分类 / 标签页面
- Banner 数据正式化
- SiteConfig 后台编辑

### 第二优先级

- 评论系统
- 搜索
- 分页
- 归档页
- SEO 输出

### 第三优先级

- 登录权限
- 作者后台
- 软删除
- RSS
- sitemap

---

## 9. 最终建议

下一步不要只“继续写页面”，而是按照“文档先行 + 模型补齐 + 接口明确 + 功能落地”的方式推进。

推荐你接下来在 `docs/` 中继续补齐三类文档：

1. 数据模型文档
2. 视图与接口文档
3. 测试与初始化策略文档

等这些文档基本清楚之后，再进入下一轮代码实现，会比直接堆功能更稳，也更容易避免返工。