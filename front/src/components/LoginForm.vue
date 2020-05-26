<template>
  <!-- <div class="container"> -->
    <form @submit.prevent="login" class="login-form" autocomplete="off">
      <label for="username">아이디를 입력해주세요 </label>
      <input class="input" for="text" v-model="credentials.username"
      id="username" placeholder="ex) safy"><br>
      <label for="password">비밀번호를 입력해주세요 </label>
      <input class="input" type="password" v-model="credentials.password"
      id="password" placeholder="ex)1q2w3e4r!"><br>
      <button class="input submit" type="submit" :disabled="credentials.username.length < 1 || credentials.password.length < 1">로그인</button>
    </form>
  <!-- </div> -->
</template>

<script>
import axios from 'axios'
import router from '../router'

export default {
    name : "LoginForm",
    data(){
        return {
            credentials:{
              username: '',
              password: ''
            }
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
  /* .container {
    max-width: 500px;
  } */
  .login-form {
    width: 100%;
  }
  .login-form label {
    display: inline-block;
    font-size: 16px;
    margin-bottom: 5px;
    color: rbg(29, 29, 31);
  }
  .input {
    width: 100%;
    height: 50px;
    border: 2px solid black;
    border-radius: 5px;
    outline: none;
    margin-bottom: 20px;
    padding: 5px;
    font-size: 16px;
  }
  .input:placeholder-shown {
    border: none;
  }
  .submit {
    font-size: 20px;
    font-weight: bold;
    color: white;
    background-color: rgb(29, 29, 31);
    cursor: pointer;
  }
  .submit:disabled {
    border: none;
    color: #888;
    background-color: #dddddd;
  }
</style>