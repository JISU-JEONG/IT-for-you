<template>
  <div class="wrapper">
    <div class="mobile">
      <div class="cry"></div>
      <span>관리자 페이지는 pc환경에서만 지원합니다.</span>
      <router-link to="/">메인으로 돌아가기</router-link>
    </div>
    <div class="pc">
      <section>
        <h1>서비스이름</h1>
        <ul>
          <li>
            <router-link to="/admin/user">
              <i><img :src="addIcon('account')"></i>
              <span>회원 관리</span>
            </router-link>
          </li>
          <li>
            <router-link to="/admin/make">
              <i><img :src="addIcon('plus')"></i>
              <span>문제 생성</span>
            </router-link>
          </li>
          <li>
            <router-link to="/admin/edit">
              <i><img :src="addIcon('book')"></i>
              <span>문제 삭제</span>
            </router-link>
          </li>
        </ul>
      </section>
      <div class="admin-content">
        <nav>
          <span>{{routerName[this.$router.history.current.name]}}</span>
          <div class="admin-btn" @click="$router.push('/')">서비스로 돌아가기</div>
        </nav>
        <div class="content-top">
          <div>총 회원 수 {{userCount}}</div>
          <div>IT FOR YOU</div>
          <div>총 문제 수 {{questionCount}}</div>
        </div>
        <div class="content-layout">
          <router-view></router-view>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from '../api/api.service.js'
export default {
    data() {
      return {
        routerName: {User: '회원 관리', MakeQuestion: '문제 생성', EditQuestion: '문제 수정'},
        userCount: 'loading...',
        questionCount: 'loading...'
      }
    },
    methods: {
      addIcon(type){
        return require(`@/assets/icons/${type}.svg`)
      },
      getUserInfo() {
      const token = this.$session.get("jwt");
      const headers =  {
        Authorization: `JWT ${token}`
      }
      axios.get('/api/accounts/users/', {headers: headers})
        .then(res => {
          this.userCount = res.data.length
        })
      },
      loadAllQuestions() {
        const token = this.$session.get("jwt");
        const headers =  {
          Authorization: `JWT ${token}`
        }
        axios.get('/api/problems/probs/', {headers: headers})
        .then(res => {
          this.questionCount = res.data.length
        })
      },
    },
    mounted() {
      this.getUserInfo()
      this.loadAllQuestions()
    }
}
</script>
<style scoped lang='scss'>
@font-face { font-family: 'HangeulNuri-Bold'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_three@1.0/HangeulNuri-Bold.woff') format('woff'); font-weight: normal; font-style: normal; }
.wrapper .pc {
  display: none;
}
.wrapper .mobile {
  width: 100vw;
  height: 100vh;
  /* text-align: center; */
  background: linear-gradient(87deg, #2dce89 0, #2dcecc 100%);
  color: white;
  font-size: 4.5vw;
  font-weight: bold;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.wrapper .mobile span {
  height: 30px;
}
.wrapper .mobile  a {
  color: white;
}
@media (min-width: 1024px) {
  .wrapper .pc {
  display: block;
  min-width: 1300px;
}
.wrapper .mobile {
  display: none;
}
}
section {
* {font-family: HangeulNuri-Bold;}
  width: 250px;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  h1 {
    width: 100%;
    height: 100px;
    text-align: center;
    font-size: 36px;
    line-height: 100px;
  }
  ul {
    li {
      width: 100%;
      a {
        width: 100%;
        height: 48px;
        padding: 10px;
        position: relative;
        display: flex;
        text-decoration: none;
        color: rgba(0, 0, 0, 0.5);
        &:hover {
          color: rgba(0, 0, 0, 0.9);
        }
        &.router-link-active {
          color: rgba(0, 0, 0, 0.9);
        }
        &.router-link-active:before {
          content: '';
          left: 0;
          top: 6px;
          bottom: 6px;
          position: absolute;
          border-left: 3px solid black;
        }
        i {
          width: 40px;
          display: inline-block;
        }
        span {
          height: 28px;
          font-size: 20px;
          line-height: 28px;
          display: inline-block;
        }
      }
    }
  }
}
  nav {
    display: flex;
    position:absolute;
    top:0;
    left:0;
    right:0;
    padding: 20px 40px;
    justify-content: space-between;
    color: white;
    font-family: 'Cute Font', cursive;
    font-size: 25px;
    div {
      display: inline-block;
    }
  }
  .admin-content {
    min-height: 100vh;
    margin-left: 250px;
    position:relative;
    background-color: rgb(244,246,252);
  }
  .content-top {
    height: 350px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 70px 40px 100px 40px;
    background: linear-gradient(87deg, #2dce89 0, #2dcecc 100%);
    div {
      width: 300px;
      height: 120px;
      font-size: 20px;
      font-weight: 600;
      text-align: center;
      line-height: 120px;
      background-color: rgb(255,255,255);
      border-radius: 10px;
      box-shadow: 0 0 2rem 0 rgba(136,152,170,.15); 
    }
  }
  .content-layout {
    height: 650px;
    margin: -100px 40px 0;
    padding: 15px;
    background-color: rgb(255,255,255);
    border-radius: 10px;
    box-shadow: 0 0 2rem 0 rgba(136,152,170,.15); 
  }
  .admin-btn {
    cursor: pointer;
    position: relative;
  }
  .cry {
    width: 60px;
    height: 60px;
    margin-bottom: 20px;
    background-image: url('../assets/icons/cry.png');
    background-size: cover;
  }
</style>