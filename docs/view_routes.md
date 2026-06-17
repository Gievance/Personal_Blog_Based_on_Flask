# 视图与接口文档

## 1. 文档目标

本文档用于定义博客项目下一阶段的页面路由、管理后台路由以及后续可扩展的接口规范。

设计原则：

- 视图层负责请求接收、参数校验、模板渲染与跳转
- 服务层负责查询与业务组合
- 模板层只负责展示
- 后续若增加 JSON API，也优先复用服务层逻辑

当前已有视图主要位于 [`blog/home/views.py`](blog/home/views.py:1)。

---

## 2. 当前已实现视图

### 2.1 首页

- 路径：`/`
- 方法：`GET`
- 视图函数：[`index()`](blog/home/views.py:9)
- 模板：[`home.html`](blog/home/templates/home.html:1)
- 数据来源：[`get_homepage_payload()`](blog/home/services.py:3)

#### 当前职责

- 加载首页聚合数据
- 输出站点标题
- 渲染 hero、banner、文章列表与侧边栏

---

### 2.2 文章详情页

- 路径：`/posts/<slug>`
- 方法：`GET`
- 视图函数：[`post_detail()`](blog/home/views.py:16)
- 模板：[`post_detail.html`](blog/home/templates/post_detail.html:1)

#### 当前职责

- 按 `slug` 查询文章
- 限制仅访问已发布文章
- 自动累加阅读量
- 渲染文章详情页

#### 当前问题

- 阅读数直接在详情页访问时累加，后续可能需要防刷新刷量
- 未定义相关文章和评论数据
- 未输出 SEO 元信息

---

### 2.3 新建文章页

- 路径：`/admin/posts/new`
- 方法：`GET` / `POST`
- 视图函数：[`create_post()`](blog/home/views.py:29)
- 模板：[`post_form.html`](blog/home/templates/post_form.html:1)

#### 当前职责

- 展示文章创建表单
- 接收标题、摘要、正文、分类、封面图与推荐状态
- 创建文章并跳转到详情页

#### 当前问题

- 暂无权限控制
- 暂无编辑 / 删除功能
- 暂无标签选择
- 暂无草稿状态控制
- 暂无更完整的错误反馈结构

---

## 3. 前台页面规划

### 3.1 首页模块

#### 首页

- 路径：`/`
- 方法：`GET`
- 作用：展示 hero、banner、推荐文章、最新文章、站点简介

#### 文章详情

- 路径：`/posts/<slug>`
- 方法：`GET`
- 作用：展示正文、元信息、标签、相关文章、评论

#### 分类页

- 路径：`/categories/<slug>`
- 方法：`GET`
- 作用：按分类展示文章列表

#### 标签页

- 路径：`/tags/<slug>`
- 方法：`GET`
- 作用：按标签展示文章列表

#### 归档页

- 路径：`/archive`
- 方法：`GET`
- 作用：按年月归档展示文章

#### 搜索页

- 路径：`/search`
- 方法：`GET`
- 参数：`q`
- 作用：按标题 / 摘要 / 内容搜索文章

---

## 4. 后台管理视图规划

### 4.1 文章管理

#### 文章列表页

- 路径：`/admin/posts`
- 方法：`GET`
- 作用：查看全部文章，支持筛选与分页

#### 新建文章

- 路径：`/admin/posts/new`
- 方法：`GET` / `POST`
- 当前状态：已存在基础版本 [`create_post()`](blog/home/views.py:29)

#### 编辑文章

- 路径：`/admin/posts/<int:id>/edit`
- 方法：`GET` / `POST`
- 作用：更新标题、摘要、正文、分类、封面图、标签与发布状态

#### 删除文章

- 路径：`/admin/posts/<int:id>/delete`
- 方法：`POST`
- 作用：逻辑删除或物理删除文章

#### 发布 / 下线

- 路径：`/admin/posts/<int:id>/publish`
- 方法：`POST`
- 作用：切换文章发布状态

---

### 4.2 分类管理

#### 分类列表

- 路径：`/admin/categories`
- 方法：`GET`

#### 新建分类

- 路径：`/admin/categories/new`
- 方法：`GET` / `POST`

#### 编辑分类

- 路径：`/admin/categories/<int:id>/edit`
- 方法：`GET` / `POST`

#### 删除分类

- 路径：`/admin/categories/<int:id>/delete`
- 方法：`POST`

---

### 4.3 标签管理

#### 标签列表

- 路径：`/admin/tags`
- 方法：`GET`

#### 新建标签

- 路径：`/admin/tags/new`
- 方法：`GET` / `POST`

#### 编辑标签

- 路径：`/admin/tags/<int:id>/edit`
- 方法：`GET` / `POST`

#### 删除标签

- 路径：`/admin/tags/<int:id>/delete`
- 方法：`POST`

---

### 4.4 Banner 管理

#### Banner 列表

- 路径：`/admin/banners`
- 方法：`GET`

#### 新建 Banner

- 路径：`/admin/banners/new`
- 方法：`GET` / `POST`

#### 编辑 Banner

- 路径：`/admin/banners/<int:id>/edit`
- 方法：`GET` / `POST`

#### 删除 Banner

- 路径：`/admin/banners/<int:id>/delete`
- 方法：`POST`

---

### 4.5 站点配置管理

#### 站点配置页

- 路径：`/admin/site-config`
- 方法：`GET` / `POST`
- 作用：编辑站点名、副标题、hero 文案、about 文案、logo、favicon、SEO 信息

---

## 5. 评论接口规划

### 5.1 提交评论

- 路径：`/posts/<slug>/comments`
- 方法：`POST`
- 权限：匿名或登录用户
- 作用：提交评论

#### 表单字段建议

- `nickname`
- `email`
- `content`
- `parent_id`

### 5.2 评论审核

- 路径：`/admin/comments/<int:id>/approve`
- 方法：`POST`
- 权限：Admin

### 5.3 评论删除

- 路径：`/admin/comments/<int:id>/delete`
- 方法：`POST`
- 权限：Admin

---

## 6. 权限边界规划

### 6.1 Visitor

- 可访问首页、详情页、分类页、标签页、搜索页
- 不可访问后台管理页

### 6.2 Author

- 可访问自己文章的管理页
- 可新建 / 编辑 / 下线自己文章
- 不可管理站点配置与全局分类标签（可视项目策略而定）

### 6.3 Admin

- 可访问全部后台页面
- 可管理文章、分类、标签、Banner、评论、站点配置

---

## 7. 表单与请求参数规范

### 7.1 创建文章

对应当前 [`create_post()`](blog/home/views.py:29) 以及未来扩展接口。

#### 请求字段

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| `title` | string | 是 | 文章标题 |
| `summary` | string | 是 | 摘要 |
| `content` | string | 是 | 正文 |
| `category_id` | int | 是 | 分类 ID |
| `cover_image` | string | 否 | 封面图路径 |
| `is_featured` | bool | 否 | 是否推荐 |
| `tag_ids` | list[int] | 否 | 标签 ID 列表 |
| `status` | string | 否 | 草稿 / 发布 |

#### 成功行为

- 创建文章
- 生成 slug
- 跳转详情页或后台列表页

#### 失败情况

- 标题为空
- 摘要为空
- 正文为空
- 分类不存在
- 作者不存在
- slug 冲突

---

### 7.2 编辑文章

#### 请求字段

和创建文章基本一致，但增加：

- `id`
- 旧封面替换策略
- 状态变更字段

---

### 7.3 Banner 创建 / 编辑

#### 请求字段建议

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| `title` | string | 是 | 标题 |
| `subtitle` | string | 是 | 副标题 |
| `image` | string | 是 | 图片路径 |
| `link_url` | string | 否 | 跳转链接 |
| `sort_order` | int | 否 | 排序 |
| `is_active` | bool | 否 | 是否启用 |

---

## 8. 响应与异常规范

### 8.1 页面视图

服务于模板渲染的视图应明确：

- 成功时渲染哪个模板
- 缺失数据时返回什么状态码
- 表单错误时如何 flash 提示
- 是否需要重定向

### 8.2 后续 JSON API 约定

如果后续增加异步接口，建议统一返回结构：

```json
{
  "success": true,
  "message": "操作成功",
  "data": {}
}
```

失败时：

```json
{
  "success": false,
  "message": "参数错误",
  "errors": {}
}
```

---

## 9. 服务层与视图层职责边界

### 9.1 视图层负责

- 读取请求参数
- 处理路由
- 做基础校验
- 调用服务层
- 渲染模板或重定向

### 9.2 服务层负责

- 聚合查询
- 业务判断
- 排序 / 分页 / 筛选逻辑
- DTO / ViewModel 组装

### 9.3 模板层负责

- 展示字段
- 简单条件渲染
- 不承载复杂业务逻辑

---

## 10. 下一步推荐新增视图文档拆分

后续如果视图继续增多，可以继续拆分为：

- `docs/view_routes_public.md`
- `docs/view_routes_admin.md`
- `docs/comment_api_plan.md`
- `docs/auth_flow.md`

---

## 11. 实施优先级

### 第一阶段

- 文章列表后台页
- 文章编辑页
- 分类 / 标签前台页
- Banner 管理页

### 第二阶段

- 评论提交流程
- 评论审核流程
- 搜索与分页

### 第三阶段

- 登录权限
- JSON API
- SEO 输出与订阅能力
