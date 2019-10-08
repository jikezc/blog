<template>
  <div class="container">
    <h2 class="atricle-title">留言板</h2>
    <hr/>
    <div class="card-container">
      <el-card class="box-card" v-for="message in messages">
        {{message.message_content}}
      </el-card>
      <!--      <el-card class="box-card">-->
      <!--        留言内容测试-->
      <!--      </el-card>-->
    </div>
    <!--    <div class="card-container">-->
    <!--      <el-card class="box-card">-->
    <!--        留言内容测试-->
    <!--      </el-card>-->
    <!--      <el-card class="box-card">-->
    <!--        留言内容测试-->
    <!--      </el-card>-->
    <!--    </div>-->
    <hr/>
    <div class="message_input">
      <el-input
        type="textarea"
        :rows="2"
        placeholder="请输入留言的内容......"
        v-model="textarea">
      </el-input>
    </div>
    <div>
      <el-button class="message_btn" @click=" send_messages()"> 留 言</el-button>
    </div>
  </div>
</template>

<script>
    export default {
        name: "MessageContent",
        components: {},
        data() {
            return {
                textarea: '',
                messages: []
            }
        },
        watch: {
            "textarea"(to, from) {
                console.log(to)
            }
        },
        created() {
            this.get_messages()
        },
        methods: {
            get_messages() {
                this.$axios.get(this.$settings.Host + "article/messages").then(response => {
                    this.messages = response.data;
                    console.log(this.messages)
                }).catch(error => {
                    console.log(error.response)
                })
            },
            send_messages() {
                this.$axios.post(this.$settings.Host + "article/send_messages/", {"message_content": this.textarea}, {
                    responseData: "json",
                }).then(response => {
                    console.log(response.data);
                    alert("留言成功");
                    location.reload()
                }).catch(error => {
                    console.log(error.response)
                })
            }
        }
    }
</script>

<style scoped>
  .container {
    min-height: 1000px;
    padding-top: 70px;
  }

  .atricle-title {
    text-align: center;
    color: #99a9bf;
  }

  .message_input {
    margin-top: 50px;
  }

  .message_btn {
    display: block;
    margin: 20px auto;
    color: #99a9bf;
    width: 100px;
  }

  .box-card {
    display: inline-block;
    margin-left: 54px;
    width: 480px;
    height: 200px;
    font-size: 18px;
    color: #868686;
    margin-bottom: 30px;
    font-family: 微软雅黑;
  }

  .card-container {
    margin-top: 54px;
  }


</style>
