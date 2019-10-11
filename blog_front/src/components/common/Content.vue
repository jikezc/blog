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
        <span class="lead">发布时间：{{article.create_time | format_time}}</span>
      </div>
      <div class="info-block">
        <span class="iconfont">&#xe633;</span>
        <span class="lead">{{article.views_count}}浏览</span>
      </div>
      <div class="info-block" @click="give_like()">
        <span class="iconfont" :id="already_click?'change-color':''">&#xe657;</span>
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
                views_count: 0,
                like_count: 0,
                already_click: 0,
                // value: new Data()
                article: {
                    article_body: "没有此文章"
                }
            }
        },
        created() {
            this.get_article_content();
        },
        methods: {
            get_article_content() {
                this.$axios.get(this.$settings.Host + "article/" + this.$route.query.id).then(response => {
                    this.article = response.data;
                    this.views_count = response.data.views_count;
                    this.like_count = response.data.give_like_count;
                }).catch(error => {
                    console.log(error.response)
                })
            },
            give_like() {
                this.already_click = 1;
                this.$message({
                    message: "谢谢点赞❤"
                });
                let count = this.like_count + 1;
                this.$axios.put(this.$settings.Host + "article/give_like/" + this.$route.query.id + "/",
                    {"give_like_count": count}).then(response => {
                    console.log(response.data);
                    this.get_article_content();
                }).catch(error => {
                    console.log(error.response)
                })
            },
        },
        filters: {
            format_time: function (val) {
                let time = new Date(val);
                let Y = time.getFullYear();
                let m = time.getMonth() + 1;
                let d = time.getDay();
                let H = time.getHours();
                let M = time.getMinutes();
                return `${Y}/${m < 10 ? '0' + m : m}/${d < 10 ? '0' + d : d} ${H < 10 ? '0' + H : H}:${M < 10 ? '0' + M : M}`
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

  .md {
    color: #99a9bf;
  }

  #change-color {
    color: #c12e2a;
  }
</style>
