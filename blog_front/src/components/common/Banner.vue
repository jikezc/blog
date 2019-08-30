<template>
  <div class="container">
    <div id="target"></div>
    <div class="carousel-picture">
      <el-carousel :interval="5000" arrow="always" height="600px">
        <el-carousel-item v-for="item in 4" :key="item">
          <img src="../../../static/image/carousel1.jpg" alt="" width="100%">
        </el-carousel-item>
      </el-carousel>
    </div>
    <div class="inner cover">
      <h1 class="cover-heading">Welcome to My Blog page.</h1>
      <p class="lead">Cover is a one-page template for building simple and beautiful home pages. Download, edit the
        text, and add your own fullscreen background photo to make it your own.</p>
      <p class="lead">
        <a href="javascript:void(0)" class="btn btn-lg btn-default" @click="go_content">Watch more</a>
      </p>
    </div>
    <hr class="featurette-divider">
    <div>
      <div class="row featurette">
        <div class="col-md-7">
          <h2 class="featurette-heading">Git代码管理
            <!--            <span class="text-muted">It'll blow your mind.</span>-->
          </h2>
          <p class="lead">Git是一个开源的分布式版本控制系统，可以有效、高速地处理从很小到非常大的项目版本管理。Git是 Linus Torvalds 为了帮助管理 Linux
            内核开发而开发的一个开放源码的版本控制软件。</p>
        </div>
        <div class="col-md-5">
          <img class="featurette-image img-responsive center-block" src="../../../static/image/timg.jpeg"
               alt="Generic placeholder image">
        </div>
      </div>

      <hr class="featurette-divider">

      <div class="row featurette">
        <div class="col-md-7 col-md-push-5">
          <h2 class="featurette-heading">Oh yeah, it's that good. <span class="text-muted">See for yourself.</span></h2>
          <p class="lead">Donec ullamcorper nulla non metus auctor fringilla. Vestibulum id ligula porta felis euismod
            semper. Praesent commodo cursus magna, vel scelerisque nisl consectetur. Fusce dapibus, tellus ac cursus
            commodo.</p>
        </div>
        <div class="col-md-5 col-md-pull-7">
          <img class="featurette-image img-responsive center-block" src="../../../static/image/timg.jpeg"
               alt="Generic placeholder image">
        </div>
      </div>

      <hr class="featurette-divider">

      <div class="row featurette">
        <div class="col-md-7">
          <h2 class="featurette-heading">And lastly, this one. <span class="text-muted">Checkmate.</span></h2>
          <p class="lead">Donec ullamcorper nulla non metus auctor fringilla. Vestibulum id ligula porta felis euismod
            semper. Praesent commodo cursus magna, vel scelerisque nisl consectetur. Fusce dapibus, tellus ac cursus
            commodo.</p>
        </div>
        <div class="col-md-5">
          <img class="featurette-image img-responsive center-block" src="../../../static/image/timg.jpeg"
               alt="Generic placeholder image">
        </div>
      </div>

      <hr class="featurette-divider">
    </div>
    <img src="../../../static/image/back_top.png" alt="" id="to-top-btn" @click="back_top">
    <!--    <button ></button>-->
  </div> <!-- /container -->
</template>

<script>
  export default {
    name: "Banner",
    data() {
      return {}
    },
    mounted(){
      window.addEventListener('scroll', this.scrollToTop)
    },
    methods: {
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
            console.log(scroll_top);
            window.scroll(0,scroll_top);
            if (scroll_top<0){
              clearInterval(timer);
            }
          }, 10);
        }

      },
      go_content(){
        let scroll_now = 0;
        let timer = setInterval(function(){
          scroll_now += 10;
          console.log(scroll_now);
          window.scroll(0,scroll_now);
          if (scroll_now >= 900){
            clearInterval(timer);
          }

        })

      }
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
</style>
