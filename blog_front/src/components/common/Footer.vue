<template>
  <div class="footer">
    <ul>
      <li>关于作者</li>
      <li>联系方式</li>
      <li>声明</li>
      <!--        <li></li>-->
      <!--        <li></li>-->
      <!--        <li></li>-->
    </ul>
    <p>Copyright © cgtblog.cn版权所有 | 粤ICP备19054175号</p>
  </div>
</template>

<script>
    export default {
        name: "Footer"
    }
</script>

<style scoped>
  .footer {
    width: 100%;
    height: 128px;
    /*background: #25292e;*/
    /*color: #fff;*/
    background-color: #f8f8f8;
    color: #777777;
    margin-top: 40px;
  }

  .footer ul {
    margin: 0 auto 16px;
    padding-top: 38px;
    width: 810px;
  }

  .footer ul li {
    float: left;
    width: 112px;
    margin: 0 10px;
    text-align: center;
    font-size: 14px;
    cursor: pointer;
  }

  .footer ul::after {
    content: "";
    display: block;
    clear: both;
  }

  .footer p {
    text-align: center;
    font-size: 12px;
    font-family: "Helvetica Neue";
  }

  ul, li {
    list-style: none;
  }
</style>
