<template>
  <div class="container">
    <h2 class="atricle-title">联系方式</h2>
    <hr>
    <div class="intro">
      <p><span>QQ：</span><span>1019691608</span></p>
      <p><span>WeChat：</span><span>cg08010818</span></p>
      <p><span>Email:</span><span>1019691608@qq.com</span></p>
      <p><span>Phone：</span><span>13128648140</span></p>
    </div>
    <hr>
  </div>

</template>

<script>
    export default {
        name: "About"
    }
</script>

<style scoped>
  .container {
    min-height: 800px;
    padding-top: 70px;
  }

  .atricle-title {
    text-align: center;
    color: #99a9bf;
  }
  .intro {
    min-height: 400px;
    /*text-align: center;*/
  }

  h4 {
    font-size: 24px;
  }

  p {
    font-size: 18px;
  }

  span {
    margin-left: 10px;
    padding-left: 10px;
  }
</style>
