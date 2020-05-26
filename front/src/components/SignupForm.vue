<template>
  <form class="signup-form" @submit.prevent="userCreate" autocomplete="off">
    <label for="email">이메일을 입력해주세요 </label>
    <input class="input" type="email" v-model="email" id="email"  placeholder="ex) ssafy@ssafy.com">
    <label for="name">아이디를 입력해주세요</label>
    <input class="input" type="text" v-model="name" id="name" placeholder="ex) ssafy">
    <label for="password">비밀번호를 입력해주세요 </label>
    <input class="input" type="password" v-model="password" id="password" placeholder="ex) 1q2w3e4r!">
    <label for="password-check">비밀번호를 한번 더 입력해주세요 </label>
    <input class="input" type="password" v-model="passwordCheck" id="password-check" placeholder="ex) 1q2w3e4r!" @input="passwordChecking">
    <button class="input submit" type="submit" :disabled="signupCheck">회원가입</button>
  </form>
</template>

<script>
import axios from "@/api/api.service.js";
import router from '../router'
export default {
  name: 'SignupForm',
  data(){
    return {
      email:'',
      name: '',
      password:'',
      passwordCheck:'',
      credentials:{},
    }
  },
  methods:{
    userCreate(){
      const data = {
        username: this.name,
        password: this.password,
        email: this.email
      }
      axios.post('/api/accounts/signup/', data)
        .then(response => {
          this.credentials.username = this.name
          this.credentials.password = this.password
          axios.post('/api/token/',this.credentials)
            .then(response => {
              const token = response.data.token
              this.$session.start()
              this.$session.set('jwt', token)
              this.$store.dispatch('login', token)
              router.push('/')
            })
            .catch(error => {
              console.log(error)
            })
        })
        .catch(error => {
          console.log(error)
        })
    },
    passwordChecking() { // 비밀번호 확인해서 다르면 안내메세지 뜨게...해야하는데
      if (this.password != this.passwordCheck) console.log('asd')
    }
  },
  computed: {
    signupCheck() {
      return (this.name.length < 1 || this.password.length < 1 || this.passwordCheck.length < 1 || this.email.length < 1 || this.password !== this.passwordCheck)
    }
  }
}
</script>

<style scoped>
  .signup-form {
    width: 100%;
  }
  .signup-form label {
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