<template>
  <div class="container">
    <div class="login-container" id="login-section">
      <h1>IT FOR YOU</h1>
      <div class="login-or-signup">
        <span>
          <p>회원이시라면</p>
          <p
            class="form-change-btn"
            :class="{ activate: showLogin }"
            @click="showLogin = true"
          >
            로그인
          </p>
        </span>
        <span>
          <p>아직 회원이 아닌가요?</p>
          <p
            class="form-change-btn"
            :class="{ activate: !showLogin }"
            @click="showLogin = false"
          >
            회원가입
          </p>
        </span>
      </div>
      <LoginForm v-if="showLogin" />
      <SignupForm v-else />
    </div>
    <div class="desc-container">
      <div class="desc-background-color">
        <div class="logo">
          <h1>IT FOR YOU</h1>
        </div>
        <h2>환영합니다.</h2>
        <p>기술면접준비<br />우리와 함께</p>
        <hr />
        <ul>
          <li>
            <strong>문제풀이</strong>
            <p>다양한 주제별 문제와 해설 제공</p>
          </li>
          <li>
            <strong>면접 대비</strong>
            <p>나만의 녹음 스크립트로 면접준비</p>
          </li>
          <li>
            <strong>오답노트와 찜한문제</strong>
            <p>틀린문제와 내가 원하는 문제를 한눈에</p>
          </li>
        </ul>
      </div>
      <a class="arrow-bottom no_highlights" href="#login-section"></a>
    </div>
  </div>
</template>

<script>
import LoginForm from "@/components/Login/LoginForm.vue";
import SignupForm from "@/components/Login/SignupForm.vue";
import axios from "axios";

export default {
  name: "Login",
  data() {
    return {
      showLogin: true
    };
  },
  components: {
    LoginForm,
    SignupForm
  },
  methods: {
    logout() {
      this.$session.destroy();
      this.$store.dispatch("logout");
      this.$router.push("/login");
    }
  }
};
</script>

<style scoped>
@font-face {
  font-family: "HangeulNuri-Bold";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_three@1.0/HangeulNuri-Bold.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
* {
  font-family: HangeulNuri-Bold;
  display: block;
  box-sizing: border-box;
}
.no_highlights {
  -webkit-tap-highlight-color: transparent;
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
ul,
li {
  list-style: none;
}
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
  background-image: url("https://i.pinimg.com/564x/6b/27/d8/6b27d8dbc23961c9edcc91295b1012b4.jpg");
  background-repeat: no-repeat;
  background-size: cover;
}
.desc-background-color {
  width: 100%;
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
  color: white;
}
.logo {
  margin-bottom: 150px;
}
.logo > h1 {
  font-size: 35px;
}
.arrow-bottom {
  width: 0;
  height: 0;
  border: 15px solid white;
  border-color: white transparent transparent;
  position: absolute;
  bottom: 40px;
  left: 50%;
  transform: translateX(-50%);
  animation: moving 1s linear infinite;
}
@keyframes moving {
  0% {
    bottom: 40px;
  }
  50% {
    bottom: 30px;
  }
  100% {
    bottom: 40px;
  }
}

@media (min-width: 1024px) {
  .container {
    flex-direction: row;
  }
  .logo h1 {
    visibility: hidden;
  }
  .login-container,
  .desc-container,
  .desc-background-color {
    padding: 70px;
  }
  .arrow-bottom {
    display: none;
  }
}
</style>
