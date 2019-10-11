from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    """文章列表分页器"""
    # page_query_param = ""   # 地址上表示页码的变量名，默认是page
    page_size = 6  # 每页显示的数据量，没有设置页码，则不进行分页
    page_size_query_param = "size"  # 允许客户端通过指定的参数名来设置每一页数据量的大小，默认是size
    max_page_size = 6  # 限制每一页最大展示的数据量
