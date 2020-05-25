<template>
  <div class="container">
      <form @submit.prevent="login" class="login-form">
        <!-- <label for="username">ID: </label> -->
        <input class="input" for="text" v-model="credentials.username"
        id="username" placeholder="아이디"><br>
        <!-- <label for="password">PWD: </label> -->
        <input class="input" type="password" v-model="credentials.password"
        id="password" placeholder="비밀번호"><br>
        <input class="input submit" type="submit" value="로그인">
      </form>
      <router-link to="/signup">회원가입</router-link>
      <router-link to="/">메인으로</router-link>
  </div>
</template>

<script>
import axios from 'axios'
import router from '../router'

export default {
    name : "LoginForm",
    data(){
        return {
            credentials:{}
        }
    },
    methods:{
        login(){
            console.log(this.credentials)
            axios.post('http://127.0.0.1:8000/api-token-auth/',this.credentials)
                .then(response => {
                    console.log(response)
                    console.log(response.data.token)
                    const token = response.data.token
                    this.$session.start()
                    this.$session.set('jwt', token)

                    this.$store.dispatch('login', token)
                    // home으로 가기
                    // router.push('/')
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }

}
</script>

<style scoped>
  .container {
    max-width: 500px;
    height: 100vh;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  .container a {
    font-size: 16px;
    font-weight: bold;
    color: rgb(29, 29, 31);
    text-decoration: none;
  }
  .login-form {
    width: 100%;
    text-align: center;
  }
  .input {
    width: 80%;
    height: 50px;
    border: 2px solid black;
    border-radius: 5px;
    outline: none;
    margin-bottom: 10px;
    padding: 5px;
    font-size: 16px;
  }
  .input:placeholder-shown {
    border: 2px solid #888;
  }
  .submit {
    border: 2px solid #888;
    cursor: pointer;
  }
</style>