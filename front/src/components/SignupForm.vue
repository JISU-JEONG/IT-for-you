<template>
  <!-- <div class="container"> -->
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
  <!-- </div> -->
</template>

<script>
import axios from 'axios'
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
    },
    computed: {
      signupCheck() {
        return (this.name.length < 1 || this.password.length < 1 || this.passwordCheck.length < 1 || this.email.length < 1 || this.password !== this.passwordCheck)
      }
    }
}
</script>

<style scoped>
  /* .container {
    max-width: 500px;
    height: 100vh;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  } */
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
  /* .input {
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
  } */
</style>