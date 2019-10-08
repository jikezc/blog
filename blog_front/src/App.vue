<template>
  <div id="app">
    <Header></Header>
    <router-view/>
    <Footer></Footer>
  </div>
</template>

<script>
    import Header from "./components/common/Header";
    import Footer from "./components/common/Footer";
    export default {
        name: 'App',
        components: {
            Header,
            Footer
        }
    }
</script>

<style>
  /*ul, li {*/
  /*  list-style: none;*/
  /*}*/
</style>
