<template>
  <div class="container">
    <div id="target"></div>
    <div class="carousel-picture">
      <el-carousel :interval="2000" arrow="always" height="600px">
        <el-carousel-item v-for="item in slideshow_list">
          <img :src="item.image" alt="" width="100%">
        </el-carousel-item>
      </el-carousel>
    </div>
    <div class="inner cover">
      <h1 class="cover-heading">Welcome to My Blog page.</h1>
      <p class="lead">The night gave me black eyes, but I used them to find light</p>
      <p class="lead">
        <a href="javascript:void(0)" class="btn btn-lg btn-default" @click="go_content">Watch more</a>
      </p>
    </div>
    <hr class="featurette-divider">

    <div v-for="article in three_articles_list">
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
    </div>

<!--    <div>-->
<!--      <div class="row featurette">-->
<!--        <div class="col-md-7">-->
<!--          <h2 class="featurette-heading">Git代码管理-->
<!--            &lt;!&ndash;            <span class="text-muted">It'll blow your mind.</span>&ndash;&gt;-->
<!--          </h2>-->
<!--          <p class="lead">Git是一个开源的分布式版本控制系统，可以有效、高速地处理从很小到非常大的项目版本管理。Git是 Linus Torvalds 为了帮助管理 Linux-->
<!--            内核开发而开发的一个开放源码的版本控制软件。</p>-->
<!--        </div>-->
<!--        <div class="col-md-5">-->
<!--          <img class="featurette-image img-responsive center-block" src="../../../static/image/timg.jpeg"-->
<!--               alt="Generic placeholder image">-->
<!--        </div>-->
<!--      </div>-->

<!--      <hr class="featurette-divider">-->

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

<!--      <hr class="featurette-divider">-->
<!--    </div>-->
    <img src="../../../static/image/back_top.png" alt="" id="to-top-btn" @click="back_top">
    <!--    <button ></button>-->
  </div> <!-- /container -->
</template>

<script>
    export default {
        name: "Banner",
        data() {
            return {
                slideshow_list: [],
                three_articles_list: [],
            }
        },
        created() {
            this.get_slideshow();
            this.get_three_articles();
        },
        mounted() {
            window.addEventListener('scroll', this.scrollToTop)
        },
        methods: {
            // 获取轮播图
            get_slideshow() {
                this.$axios.get(this.$settings.Host + "slideshow/").then(response => {
                    this.slideshow_list = response.data;
                }).catch(error => {
                    console.log(error.response);
                })
            },
            // back_top() {
            //   target.scrollIntoView();
            // },
            scrollToTop(el) {
                let topBtn = document.getElementById('to-top-btn');
                let scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop;
                let browserHeight = 400;
                if (scrollTop > browserHeight) {
                    topBtn.style.display = 'block';
                } else {
                    topBtn.style.display = 'none';
                }
            },
            back_top() {
                let scroll_top = 0;
                if (document.documentElement && document.documentElement.scrollTop) {
                    scroll_top = document.documentElement.scrollTop;
                } else if (document.body) {
                    scroll_top = document.body.scrollTop;
                }
                if (scroll_top > 0) {
                    let timer = setInterval(function () {
                        scroll_top -= 100;
                        window.scroll(0, scroll_top);
                        if (scroll_top < 0) {
                            clearInterval(timer);
                        }
                    }, 10);
                }

            },
            go_content() {
                let scroll_now = 0;
                let timer = setInterval(function () {
                    scroll_now += 10;
                    window.scroll(0, scroll_now);
                    if (scroll_now >= 900) {
                        clearInterval(timer);
                    }

                })

            },
            // 获取导航条高度
            // get_scrollTop() {
            //   var scroll_top = 0;
            //   if (document.documentElement && document.documentElement.scrollTop) {
            //     scroll_top = document.documentElement.scrollTop;
            //   } else if (document.body) {
            //     scroll_top = document.body.scrollTop;
            //   }
            //   console.log(scroll_top);
            //   return scroll_top;
            // }
            // 获取最新添加的三篇文章在首页展示
            get_three_articles() {
                this.$axios.get(this.$settings.Host + "article/three").then(response => {
                    console.log(response.data);
                    this.three_articles_list = response.data;
                }).catch(error => {
                    this.$message({
                        message: "查询文章列表错误"
                    })
                })
            }
        }
    }
</script>

<style scoped>
  .container {
    min-height: 2000px;
    padding-top: 70px;
  }


  /*.el-carousel__item h3 {*/
  /*  color: #475669;*/
  /*  font-size: 18px;*/
  /*  opacity: 0.75;*/
  /*  line-height: 300px;*/
  /*  margin: 0;*/
  /*}*/
  .el-carousel__container {
    height: 500px;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
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

  #to-top-btn {
    position: fixed;
    right: 30px;
    bottom: 30px;
  }

  a {
    color: #333333;
    text-decoration: none;
  }
</style>
