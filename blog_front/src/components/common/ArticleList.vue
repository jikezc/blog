<template>
  <div class="container">
    <div v-for="article in article_list">
      <div class="row featurette">
        <div class="col-md-7">
          <router-link :to="'/articledetail/?id='+article.id">
            <h2 class="featurette-heading">

              {{article.title}}

              <!--            <span class="text-muted">It'll blow your mind.</span>-->
            </h2>
          </router-link>
          <p class="lead">{{article.about_aritcle}}</p>
        </div>
        <!--        @click="go_to_url()-->
        <div class="col-md-5">
          <router-link :to="'/articledetail/?id='+article.id">
            <img class="featurette-image img-responsive center-block" :src="article.article_picture"
                 alt="Generic placeholder image">
          </router-link>
        </div>
      </div>

      <hr class="featurette-divider">

      <!--      <div class="row featurette">-->
      <!--        <div class="col-md-7 col-md-push-5">-->
      <!--          <h2 class="featurette-heading">Oh yeah, it's that good. <span class="text-muted">See for yourself.</span></h2>-->
      <!--          <p class="lead">Donec ullamcorper nulla non metus auctor fringilla. Vestibulum id ligula porta felis euismod-->
      <!--            semper. Praesent commodo cursus magna, vel scelerisque nisl consectetur. Fusce dapibus, tellus ac cursus-->
      <!--            commodo.</p>-->
      <!--        </div>-->
      <!--        <div class="col-md-5 col-md-pull-7">-->
      <!--          <img class="featurette-image img-responsive center-block" src="../../../static/image/timg.jpeg"-->
      <!--               alt="Generic placeholder image">-->
      <!--        </div>-->
      <!--      </div>-->

      <!--      <hr class="featurette-divider">-->

      <!--      <div class="row featurette">-->
      <!--        <div class="col-md-7">-->
      <!--          <h2 class="featurette-heading">And lastly, this one. <span class="text-muted">Checkmate.</span></h2>-->
      <!--          <p class="lead">Donec ullamcorper nulla non metus auctor fringilla. Vestibulum id ligula porta felis euismod-->
      <!--            semper. Praesent commodo cursus magna, vel scelerisque nisl consectetur. Fusce dapibus, tellus ac cursus-->
      <!--            commodo.</p>-->
      <!--        </div>-->
      <!--        <div class="col-md-5">-->
      <!--          <img class="featurette-image img-responsive center-block" src="../../../static/image/timg.jpeg"-->
      <!--               alt="Generic placeholder image">-->
      <!--        </div>-->
      <!--      </div>-->
    </div>
    <!--    分页器-->
    <div class="pagination-box">
      <el-pagination
        background
        layout="prev, pager, next"
        :current-page.sync="filter.page"
        :page-size="filter.page_size"
        :total="article_total"
        @current-change="handleCurrentChange"
        @size-change="handleSizeChange">
      </el-pagination>
    </div>
  </div>
</template>

<script>
    export default {
        name: "ArticleList",
        components: {},
        data() {
            return {
                article_total: 0,
                article_list: [],
                filter: {
                    article_categroy: 0,
                    page_size: 6,
                    page: 1,
                }
            }
        },
        watch: {
            // 监听地址烂发生变化
            "$route.query.categroy"(to, from) {
                // console.log(to);
                this.filter.page = 1;
                this.get_article_list();
            },
            "filter.page_size"(to, from) {
                this.get_article_list();
            },
            "filter.page"(to, from) {
                this.get_article_list();
            }
            /*            "page"(to, from) {
                            // console.log(to)
                            this.get_article_list();
                        }*/
        },
        created() {
            // 获取文章
            this.get_article_list();
        },
        methods: {
            // 跳转到文章详情页
            // go_to_url() {
            //     window.location.href = '/articledetail';
            // },
            // 获取文章列表
            get_article_list() {
                let filters = {};
                this.filter.article_categroy = this.$route.query.categroy;
                // 判断是否需要按照文章分类获取文章列表
                if (this.filter.article_categroy > 0) {
                    filters.article_categroy = this.filter.article_categroy;
                }
                if (this.filter.page > 1) {
                    filters.page = this.filter.page
                } else {
                    filters.page = 1
                }
                this.$axios.get(this.$settings.Host + "article/", {params: filters}).then(response => {
                    this.article_list = response.data.results;
                    this.article_total = response.data.count;
                }).catch(error => {
                    console.log(error.response);
                    this.$message({
                        message: "获取文章信息有误"
                    })
                });
                // 旧版本按照分类获取文章，代码复杂，且实现分页难以修改
                // this.categroy_page = this.$route.query.categroy;
                // console.log(this.categroy_page);
                // if (!this.categroy_page) {
                //     this.categroy_page = 0;
                //     this.$axios.get(this.$settings.Host + "article/").then(response => {
                //         this.article_list = response.data.results;
                //         this.total = response.data.count
                //     }).catch(error => {
                //         console.log(error.response);
                //     })
                // } else {
                //     this.$axios.get(this.$settings.Host + "article/?article_categroy=" + this.categroy_page).then(response => {
                //         this.article_list = response.data.results;
                //         this.total = response.data.count
                //     }).catch(error => {
                //         console.log(error.response);
                //     })
                // }
            },
            // 每页数据量发生变化时执行的方法
            handleSizeChange(val) {
                this.filter.page = 1;
                this.filter.page_size = val;
            },
            // 页码发生变化时执行的方法
            handleCurrentChange(val) {
                this.filter.page = val;
            }
        }
    }
</script>

<style scoped>
  a {
    color: #333333;
    text-decoration: none;
  }

  .container {
    padding-top: 70px;
  }

  .featurette-divider {
    margin: 80px 0; /* Space out the Bootstrap <hr> more */
  }

  /* Thin out the marketing headings */
  .featurette-heading {
    font-weight: 300;
    line-height: 1;
    letter-spacing: -1px;
    margin-top: 119px;
  }

  .featurette-heading:hover {
    text-decoration: none;
  }

  .featurette-image {
    height: 400px;
    width: 400px;
    margin: auto auto;
  }

  .inner {
    padding: 30px;
    text-align: center;
    margin-top: 10px;
  }

  .cover {
    padding: 0 20px;
  }

  .cover .btn-lg {
    padding: 10px 20px;
    font-weight: bold;
  }

  .cover-heading {
    text-align: center;
  }

  .pagination-box {
    display: inline;
    text-align: center;
  }
</style>
