<template>
  <div class="container">
    <h2 class="atricle-title">个人简介</h2>
    <hr>
    <div class="intro">
      <h4>陈桂涛</h4>
      <p>昵称：小金</p>
      <p>来自广东普宁，现居深圳，计算机网络技术专业，2019年毕业</p>
      <p>涉及方面：python开发，Linux自动化</p>
      <p>爱技术、爱编程、爱生活、喜欢养动物植物</p>
      <p>黑夜给了我黑色的眼睛，我却用它寻找光明</p>



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
    text-align: center;
  }

  h4 {
    font-size: 24px;
  }

  p {
    font-size: 18px;
  }
</style>
