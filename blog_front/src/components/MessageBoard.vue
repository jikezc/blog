<template>
  <div>
<!--    <Header></Header>-->
    <MessageContent></MessageContent>
<!--    <Footer></Footer>-->
  </div>
</template>

<script>
    import Header from "./common/Header";
    import Footer from "./common/Footer";
    import MessageContent from "./common/MessageContent";
    export default {
        name: "Message",
        components: {
            Header,
            Footer,
            MessageContent
        }
    }
</script>

<style scoped>

</style>
