<template>
  <div class="footer">
    <ul>
      <li>
        <router-link to="/about">关于作者</router-link>
      </li>
      <li @click="note_message()">
        <router-link to="">技术交流</router-link>
      </li>
      <li>声明</li>
      <!--        <li></li>-->
      <!--        <li></li>-->
      <!--        <li></li>-->
    </ul>
    <p><a href="http://www.beian.miit.gov.cn/">Copyright © cgtblog.cn版权所有 | 粤ICP备19054175号</a></p>
  </div>
</template>

<script>
    export default {
        name: "Footer",
        data() {
            return {}
        },
        created() {
        },
        methods: {
            note_message() {
                this.$message({
                    message: "暂未提供此功能"
                })
            }
        }
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
    width: 236px;
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

  a {
    color: #777777;
    text-decoration: none;
  }
</style>
