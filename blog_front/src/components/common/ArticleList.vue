<template>
  <div class="container">
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
    </div>
  </div>
</template>

<script>
  export default {
    name: "ArticleList"
  }
</script>

<style scoped>
  .container {
    min-height: 2000px;
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
</style>
