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
      <div class="desc-background-color">
        <div class="logo">
          <h1>서비스 이름</h1>
        </div>
        <h2>환영합니다.</h2>
        <p>기술면접준비<br>우리와 함께</p>
        <hr>
        <ul>
          <li>
            <strong>대단한 서비스.</strong>
            <p>우리 서비스는 이런 기능들이 있다</p>
          </li>
          <li>
            <strong>대단한 서비스.</strong>
            <p>우리 서비스는 이런 기능들이 있다</p>
          </li>
          <li>
            <strong>대단한 서비스.</strong>
            <p>우리 서비스는 이런 기능들이 있다</p>
          </li>
        </ul>
      </div>
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
        addProblem(){
            this.$session.start()
            const token = this.$session.get('jwt')
            const data = {
                token : token
            }
            // sibal에 문제 번호를 넣어 주세요
            axios.post('http://127.0.0.1:8000/api/accounts/add_problem/{sibal}/', data)
                .then(response => {
                    console.log(response)
                })
                .catch(error => {
                    console.log(error)
                })
      }
    },
    updated() {
        this.isAuthenticated = this.$session.has('jwt')
    }
}
</script>

<style scoped>
@font-face { font-family: 'HangeulNuri-Bold'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_three@1.0/HangeulNuri-Bold.woff') format('woff'); font-weight: normal; font-style: normal; }
* {font-family: HangeulNuri-Bold; display: block; box-sizing: border-box;}
  ul, li {list-style: none;}
  .container {
    width: 100vw;
    display: flex;
    flex-direction: column-reverse;
  }
  .login-container {
    width: 100%;
    height: 100vh;
    padding: 35px;
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
  .form-change-btn:hover {
    color: rgb(29, 29, 31);
  }
  .form-change-btn.activate {
    color: rgb(29, 29, 31);
    text-decoration: underline;
  }
  .desc-container {
    width: 100%;
    height: 100vh;
    padding: 35px;
    color: rgb(210, 210, 210);
    position: relative;
    background-color: rgb(29, 29, 31);
    background-image: url('https://i.pinimg.com/564x/6b/27/d8/6b27d8dbc23961c9edcc91295b1012b4.jpg');
    background-repeat: no-repeat;
    background-size: cover;
  }
  .desc-background-color {
    width:100%;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
    padding: 35px;
    background-color: rgba(29, 29, 31, 0.7);
  }
  .desc-background-color h2 {
    font-size: 25px;
    margin-bottom: 13px;
  }
  .desc-background-color p {
    line-height: 40px;
    margin-bottom: 30px;
  }
  .desc-background-color ul {
    width: 100%;
    margin-top: 30px;
  }
  .desc-background-color li {
    width: 100%;
    height: 50px;
    line-height: 30px;
    margin-bottom: 20px;
  }
  .desc-background-color strong {
    color:white;
  }
  .logo {
    margin-bottom: 150px; 
  }
  .logo>h1 {
    font-size: 35px;
  }



  @media (min-width:1024px) {
    .container {
      flex-direction: row;
    }
    .logo h1 {
      visibility: hidden;
    }
    .login-container, .desc-container, .desc-background-color {
      padding: 70px;
    }
  }
</style>