<template>
  <div class="container">
    <h2 class="atricle-title">文章标题</h2>
    <hr/>
    <el-row :gutter="20">
      <el-col :span="6">
        <div class="grid-content bg-purple"></div>
      </el-col>
      <el-col :span="6">
        <div class="grid-content bg-purple"></div>
      </el-col>
      <el-col :span="6">
        <div class="grid-content bg-purple"></div>
      </el-col>
      <el-col :span="6">
        <div class="grid-content bg-purple"></div>
      </el-col>
    </el-row>
    <div class="article-info">
      <div class="info-block">
        <span class="iconfont">&#xe64d;</span>
        <span class="lead">小金</span>
      </div>
      <div class="info-block">
        <span class="iconfont">&#xe638;</span>
        <span class="lead">发布时间：2019/09/27 16:43</span>
      </div>
      <div class="info-block">
        <span class="iconfont">&#xe633;</span>
        <span class="lead">1131浏览</span>
      </div>
      <div class="info-block">
        <span class="iconfont">&#xe657;</span>
        <span class="lead">3123点赞</span>
      </div>
    </div>
    <hr/>
    <!--    <div class="jumbotron">-->
    <!--    </div>-->
    <el-card class="box-card">
      <!--      <div v-for="o in 4" :key="o" class="text item">-->
      <!--        {{'列表内容 ' + o }}-->
      <!--      </div>-->

    </el-card>
  </div>

</template>

<script>
    export default {
        name: "Content",
        data() {
            return {
                // value: new Data()
            }
        }
    }
</script>

<style scoped>
  .container {
    /*min-height: 2000px;*/
    padding-top: 70px;
  }

  .atricle-title {
    text-align: center;
    color: #99a9bf;
  }

  .lead {
    font-size: 20px;
    color: #99a9bf;
  }

  .article-info {
    margin: 10px auto;
  }

  .info-block {
    display: inline;
    padding-right: 90px;
    padding-left: 54px;
  }

  .box-card {
    margin-top: 20px;
    margin-right: 0;
    margin-left: 0;
    height: 1000px;
  }

  @font-face {
    font-family: 'iconfont';
    src: url('../../../static/font_1439002_qj555p629qr/iconfont.eot');
    src: url('../../../static/font_1439002_qj555p629qr/iconfont.eot?#iefix') format('embedded-opentype'),
    url('../../../static/font_1439002_qj555p629qr/iconfont.woff2') format('woff2'),
    url('../../../static/font_1439002_qj555p629qr/iconfont.woff') format('woff'),
    url('../../../static/font_1439002_qj555p629qr/iconfont.ttf') format('truetype'),
    url('../../../static/font_1439002_qj555p629qr/iconfont.svg#iconfont') format('svg');
  }

  .iconfont {
    font-family: "iconfont" !important;
    color: #99a9bf;
    font-size: 20px;
    font-style: normal;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

</style>
