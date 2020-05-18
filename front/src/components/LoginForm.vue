<template>
  <div>
      <form @submit.prevent="login">
        <label for="username">ID: </label>
        <input for="text" v-model="credentials.username"
        id="username"><br>
        <label for="password">PWD: </label>
        <input type="password" v-model="credentials.password"
        id="password"><br>
        <input type="submit" value="로그인">
      </form>
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

<style>

</style>