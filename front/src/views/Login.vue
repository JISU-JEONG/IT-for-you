<template>
  <div class="container">
    <div class="login-container">
      <h1>서비스 이름</h1>
      <div class="login-or-signup">
        <span>
          <p>회원이시라면</p>
          <p class="form-change-btn" :class="{'activate': showLogin}" @click="showLogin=!showLogin">로그인</p>
        </span>
        <span>
          <p>아직 회원이 아닌가요?</p>
          <p class="form-change-btn" :class="{'activate': !showLogin}" @click="showLogin=!showLogin">회원가입</p>
        </span>
      </div>
      <LoginForm v-if="showLogin"/>
      <SignupForm v-else/>
    </div>
    <div class="desc-container">
      <h1>서비스 이름</h1>
      <p>어쩌구 저쩌구 서비스 설명.</p>
      <p>어쩌구 저쩌구 서비스 설명.</p>
      <p>어쩌구 저쩌구 서비스 설명.</p>
      <hr>
      <p>어쩌구 저쩌구 서비스 설명.</p>
      <p>어쩌구 저쩌구 서비스 설명.</p>
      <p>어쩌구 저쩌구 서비스 설명.</p>
    </div>
    
    <!-- <div v-if="!isAuthenticated" v-else>
        <a @click.prevent="check" href="#">profile</a>
        <br>
        <a @click.prevent="logout" href="#">Logout</a>
    </div> -->
  </div>
</template>

<script>
import LoginForm from '@/components/LoginForm.vue'
import SignupForm from '@/components/SignupForm.vue'
import router from '../router'
import axios from 'axios'

export default {
    name: "Login",
    data() {
        return {
          showLogin: true,
          isAuthenticated: this.$session.has('jwt')
        }
    },
    components:{
        LoginForm,
        SignupForm
    },
    methods:{
        logout(){
            console.log(this.$session)
            this.$session.destroy()
            this.$store.dispatch('logout')
            // router.push('/login')
        },
        // signup(){
        //     router.push('/signup')
        // },
        check(){
            // this.$session.start()
            // const token = this.$session.get('jwt')
            // const data = {
            //     token : token,
            // }
            // axios.post('http://127.0.0.1:8000/api/accounts/user/', data)
            // .then(response => {
            //     console.log(response)
            // })
            // .catch(error => {
            //     console.log(error)
            // })
            router.push('/profile')
        },
    },
    updated() {
        this.isAuthenticated = this.$session.has('jwt')
    }
}
</script>

<style scoped>
@font-face { font-family: 'HangeulNuri-Bold'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_three@1.0/HangeulNuri-Bold.woff') format('woff'); font-weight: normal; font-style: normal; }
* {font-family: HangeulNuri-Bold; display: block;}
  .container {
    width: 100vw;
    display: flex;
    flex-direction: column-reverse;
  }
  .login-container {
    width: 100%;
    height: 100vh;
    padding: 30px;
  }
  .login-or-signup {
    display: flex;
  }
  .login-container h1 {
    font-size: 35px;
    margin-bottom: 100px;
  }
  .login-container p {
    font-size: 14px;
    color: #888;
    margin-bottom: 10px;
  }
  .login-container .form-change-btn {
    margin: 0 40px 50px 0;
    display: inline-block;
    font-size: 25px;
    font-weight: bold;
    color: #888;
    cursor: pointer;
  }
  .form-change-btn.activate {
    color: rgb(29, 29, 31);
    text-decoration: underline;
  }
  .desc-container {
    width: 100%;
    height: 100vh;
    padding: 30px;
    color: white;
    background-color: rgb(29, 29, 31);
  }
  @media (min-width:1024px) {
    .container {
      flex-direction: row;
    }
  }
</style>