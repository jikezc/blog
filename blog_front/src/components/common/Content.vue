<template>
  <div class="container">
    <h2 class="atricle-title">{{article.title}}</h2>
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
        <span class="lead">{{article.author}}</span>
      </div>
      <div class="info-block">
        <span class="iconfont">&#xe638;</span>
        <span class="lead">发布时间：2019/09/27 16:43</span>
      </div>
      <div class="info-block">
        <span class="iconfont">&#xe633;</span>
        <span class="lead">{{article.views_count}}浏览</span>
      </div>
      <div class="info-block">
        <span class="iconfont">&#xe657;</span>
        <span class="lead">{{article.give_like_count}}点赞</span>
      </div>
    </div>
    <hr/>
    <!--    <div class="jumbotron">-->
    <!--    </div>-->
<!--    <el-card class="box-card" v-html="article.article_to_html">-->
<!--      &lt;!&ndash;      <div v-for="o in 4" :key="o" class="text item">&ndash;&gt;-->
<!--      &lt;!&ndash;        {{'列表内容 ' + o }}&ndash;&gt;-->
<!--      &lt;!&ndash;      </div>&ndash;&gt;-->

<!--    </el-card>-->

    <mavon-editor class="md"
                  :value="article.article_body"
                  :subfield="false"
                  :defaultOpen="'preview'"
                  :toolbarsFlag="false"
                  :editable="false"
    >
    </mavon-editor>

  </div>

</template>

<script>

    export default {
        name: "Content",
        components: {},
        data() {
            return {
                // value: new Data()
                article: {
                    article_body: "没有此文章"
                }
            }
        },
        created() {
            this.$axios.get(this.$settings.Host + "article/" + this.$route.query.id).then(response => {
                this.article = response.data;
                console.log(this.artile.title)
            }).catch(error => {
                console.log(error.response)
            })
        },
        methods: {}
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

  .md {
    color: #99a9bf;
  }
</style>
