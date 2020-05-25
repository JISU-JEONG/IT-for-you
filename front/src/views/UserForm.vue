<template>
  <div class="container">
    <form class="signup-form" @submit.prevent="userCreate" >
        <!-- <label for="email">email: </label> -->
        <input class="input" type="text"
        v-model="email" id="email"  placeholder="이메일">
        <!-- <label for="name">name: </label> -->
        <input class="input" type="text"
        v-model="name" id="name" placeholder="닉네임">
        <!-- <label for="password" id="password">password: </label> -->
        <input class="input" type="password"
        v-model="password" id="password" placeholder="비밀번호">
        <input class="input" type="password"
        v-model="passwordCheck" id="password-check" placeholder="비밀번호 확인" @input="passwordChecking">
        <input class="input submit" type = "submit" value = "회원가입" />
    </form>
    <router-link to="/login">로그인</router-link>
    <router-link to="/">메인으로</router-link>
  </div>
</template>

<script>
import axios from 'axios'
import router from '../router'
export default {
    name: 'UserForm',
    data(){
        return {
            name: '',
            password:'',
            passwordCheck:'',
            email:'',
            credentials:{}
        }
    },
    methods:{
        userCreate(){
            console.log('들어옴')
            const data = {
                username: this.name,
                password: this.password,
                // id: this.user_id,
                email: this.email
            }
            console.log(data)

            axios.post('http://127.0.0.1:8000/api/accounts/signup/', data)
                 // this.options는 computed 변수
                .then(response => {
                    console.log(this.name)
                    console.log(this.password)
                    this.credentials.username = this.name
                    this.credentials.password = this.password
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
                            router.push('/login')
                        })
                        .catch(error => {
                            console.log(error)
                        })
                })
                .catch(error => {
                console.log(error)
                })
        },
        passwordChecking() {
          if (this.password != this.passwordCheck) console.log('asd')
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
  .signup-form {
    width: 100%;
    text-align: center;
  }
  .submit {
    border: 2px solid #888;
    cursor: pointer;
  }
  .container a {
    font-size: 16px;
    font-weight: bold;
    color: rgb(29, 29, 31);
    text-decoration: none;
  }
  .wrong-password {
    border: 2px solid red;
  }
  .correct-password {
    border: 2px solid green;
  }
</style>