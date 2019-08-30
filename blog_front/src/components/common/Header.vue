<template>
  <div>
    <nav class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">小金博客 blog</a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="#">首页</a></li>
            <li><a href="#about">关于</a></li>
            <li><a href="#contact">联系方式</a></li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">文章分类 <span class="caret"></span></a>
              <ul class="dropdown-menu">
                <li><a href="#">Python</a></li>
                <li><a href="#">Django</a></li>
                <li><a href="#">Flask</a></li>
                <li role="separator" class="divider"></li>
                <li class="dropdown-header">Nav header</li>
                <li><a href="#">Separated link</a></li>
                <li><a href="#">One more separated link</a></li>
              </ul>
            </li>
          </ul>
          <ul class="nav navbar-nav navbar-right">
            <li><a href="../navbar/">留言</a></li>
            <li><router-link to="support/">赞助</router-link></li>
<!--            <li><a href="../navbar-static-top/">赞助</a></li>-->
            <li class="active"><a href="./">菜单 <span class="sr-only">(current)</span></a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>
  </div>
</template>

<script>
  export default {
    name: "Header",
    data() {
      return {}
    },
    created() {
    },
    methods: {},
  }
</script>

<style scoped>

</style>
