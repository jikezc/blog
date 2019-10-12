<template>
  <div>
    <nav class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar"
                  aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <!--          <a class="navbar-brand" href="#"> 小金博客 blog</a>-->
          <router-link to="/home" class="navbar-brand">小金博客 blog</router-link>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li :class="index==0?'active':''" @click="index=0"><router-link to="/">首页</router-link></li>
            <li class="dropdown" @click="index=4">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                 aria-expanded="false">文章分类 <span class="caret"></span></a>
              <ul class="dropdown-menu">

                <li>
                  <router-link to="/article" class="categroy_name">全部文章</router-link>
                </li>
                <li v-for="item in categroy_list">
                  <router-link :to="'/article/?categroy='+item.id">{{item.name}}</router-link>
                  <!--                  <a href="/article/?categroy='+item.id" class="categroy_name">{{item.name}}</a>-->
                </li>
                <!--                <li><a href="#">Django</a></li>-->
                <!--                <li><a href="#">Flask</a></li>-->
                <!--                <li role="separator" class="divider"></li>-->
                <!--                <li class="dropdown-header">全部文章</li>-->
                <!--                <li><a href="#">Separated link</a></li>-->
                <!--                <li><a href="#">One more separated link</a></li>-->
              </ul>
            </li>
            <li :class="index==1?'active':''" @click="index=1">
              <router-link to="/about">关于作者</router-link>
            </li>
            <li :class="index==2?'active':''" @click="index=2 && note_message()"><a href="javascript:void(0)">技术交流</a></li>
<!--            <li class="dropdown" @click="index=4">-->
<!--              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"-->
<!--                 aria-expanded="false">文章分类 <span class="caret"></span></a>-->
<!--              <ul class="dropdown-menu">-->

<!--                <li>-->
<!--                  <router-link to="/article" class="categroy_name">全部文章</router-link>-->
<!--                </li>-->
<!--                <li v-for="item in categroy_list">-->
<!--                  <router-link :to="'/article/?categroy='+item.id">{{item.name}}</router-link>-->
<!--                  &lt;!&ndash;                  <a href="/article/?categroy='+item.id" class="categroy_name">{{item.name}}</a>&ndash;&gt;-->
<!--                </li>-->
<!--                &lt;!&ndash;                <li><a href="#">Django</a></li>&ndash;&gt;-->
<!--                &lt;!&ndash;                <li><a href="#">Flask</a></li>&ndash;&gt;-->
<!--                &lt;!&ndash;                <li role="separator" class="divider"></li>&ndash;&gt;-->
<!--                &lt;!&ndash;                <li class="dropdown-header">全部文章</li>&ndash;&gt;-->
<!--                &lt;!&ndash;                <li><a href="#">Separated link</a></li>&ndash;&gt;-->
<!--                &lt;!&ndash;                <li><a href="#">One more separated link</a></li>&ndash;&gt;-->
<!--              </ul>-->
<!--            </li>-->
          </ul>
          <ul class="nav navbar-nav navbar-right">
            <li :class="index==6?'active':''" @click="index=6">
              <router-link to="/messageboard">留言</router-link>
            </li>
            <li :class="index==7?'active':''" @click="index=7">
              <router-link to="/support">赞助</router-link>
            </li>
            <!--            <li><a href="../navbar-static-top/">赞助</a></li>-->
            <li :class="index==5?'active':''" @click="index=5 && note_message()"><a href="javascript:void(0)">菜单 <span class="sr-only">(current)</span></a>
            </li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>
  </div>
</template>

<script>
    export default {
        name: "Header",
        data() {
            return {
                index: 0,
                visible: false,
                categroy_list: [],
                article_url: "javascript:void(0)"
            }
        },
        created() {
            this.$axios.get(this.$settings.Host + "article/categroy/").then(response => {
                this.categroy_list = response.data
            }).catch(error => {
                console.log(error.response)
            });
        },
        mounted() {
            console.log(this.index)
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
  .categroy_name {
    color: #777777;
    font-size: 15px;
  }
</style>
