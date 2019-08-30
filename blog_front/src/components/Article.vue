<template>
  <div>
    <Header></Header>
    <ArticleList></ArticleList>
    <Footer></Footer>
  </div>
</template>

<script>
  import Header from "./common/Header"
  import Footer from "./common/Footer";
  import Banner from "./common/Banner";
  import ArticleList from "./common/ArticleList";

  export default {
    name: "Article",
    components: {
      ArticleList,
      Banner,
      Footer,
      Header
    },
  }
</script>

<style scoped>

</style>
