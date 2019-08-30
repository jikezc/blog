<template>
  <div class="home">
    <Header></Header>
    <Banner></Banner>
    <Footer></Footer>
  </div>
</template>

<script>
  import Header from "./common/Header"
  import Banner from "./common/Banner";
  import Footer from "./common/Footer"
  import "../assets/js/canvas"
  export default {
      name: "Home",
      data(){
        return {}
      },
      methods:{

      },
      components:{
        Banner,
        Header,
        Footer
      }
  }

</script>

<style scoped>

</style>
