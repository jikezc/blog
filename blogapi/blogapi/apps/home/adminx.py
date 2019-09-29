import xadmin
from xadmin import views
# 轮播图
from .models import Slideshow

class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "小金博客blog"  # 设置站点标题
    site_footer = "小金"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠


class SlideshowModelAdmin(object):
    """轮播图后台管理类"""
    list_display=["name","sort","is_show"]


xadmin.site.register(Slideshow, SlideshowModelAdmin)
xadmin.site.register(views.CommAdminView, GlobalSettings)
