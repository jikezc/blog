<template>
  <div>
<!--    <Header></Header>-->
    <Content></Content>
<!--    <Footer></Footer>-->
  </div>

</template>

<script>
    import Header from "./common/Header";
    import Footer from "./common/Footer";
    import Content from "./common/Content";

    export default {
        name: "ArticleDetail",
        components: {
            Content,
            Header,
            Footer
        }
    }
</script>

<style scoped>

</style>
