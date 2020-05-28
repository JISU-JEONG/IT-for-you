<template>
  <div>
    <nav>
      <div class="hamburger-btn" @click="openSideBar">
        <div class="hamburger hamburger-top"></div>
        <div class="hamburger hamburger-mid"></div>
        <div class="hamburger hamburger-bot"></div>
      </div>
      <p>서비스 이름</p>
      {{isAuthenticated}}
      <p v-if="isAuthenticated" style="color:white">로그인상태</p>
    </nav>
    <div class="side-bar-background display-none opacity-0" @click="closeSideBar"></div>
    <div class="side-bar" :class="{'side-bar-transform': showSideBar}">
      <div class="sidde-bar-top">
        <h2>서비스 이름</h2>
        <span class="close-btn" @click="closeSideBar"></span>
      </div>
      <div class="side-bar-content">
        <ul @click="onClickEvent">
          <li><router-link to="/category">category</router-link></li>
          <li><router-link to="/detail">Detail</router-link></li>
          <li><router-link to="/testmic">TestMIC</router-link></li>
          <li><router-link to="/Admin">Admin</router-link></li>
          <li><router-link to="/login">login</router-link></li>
          <li><a @click="logout">로그아웃</a></li>
        </ul>
      </div>
    </div>
    <div class="router-wrapper">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      showSideBar: false,
      isAuthenticated: this.$session.has('jwt') 
    }
  },
  methods: {
    onClickEvent() {
      if (event.target.nodeName === 'A') {
        this.closeSideBar()
      }
    },
    openSideBar() {
      const sideBarBackground = document.querySelector('.side-bar-background')
      sideBarBackground.classList.remove('display-none')
      setTimeout(function() {
        sideBarBackground.classList.remove('opacity-0')
      }, 20)
      this.showSideBar = !this.showSideBar
    },
    closeSideBar() {
      const sideBarBackground = document.querySelector('.side-bar-background')  
      sideBarBackground.classList.add('opacity-0')
      sideBarBackground.addEventListener('transitionend', function() {
        sideBarBackground.classList.add('display-none')
      }, {
      capture: false,
      once: true,
      passive: false
      })
      this.showSideBar = !this.showSideBar
    },
    onCLickLink(path) {
      this.$router.push(`/testhome/${path}`)
      this.closeSideBar()
    },
    logout() {
      this.$session.clear()
      this.$store.dispatch('logout')
      this.$router.push('/login')
    }
  }
};
</script>

<style scoped>
  /* nav */
  nav {
    height: 44px;
    line-height: 44px;
    padding-left: 10px;
    text-align: center;
    position:fixed;
    top: 0;
    left: 0;
    right: 0;
    color: white;
    background-color: rgb(29, 29, 31);
  }
  ul,li {
    width: 100%;
    list-style: none;
  }
  li {
    height: 50px;
    line-height: 50px;
  }
  a {
    width:100%;
    padding: 0 20px;
    display: inline-block;
    font-size: 20px;
    color: rgb(162, 161, 161);
    text-decoration: none;
    cursor: pointer;
  }
  a.router-link-active {
    color: white
  }
  .hamburger-btn {
    width: 20px;
    height: 15px;
    display: inline-block;
    position: absolute;
    left: 10px;
    top:50%;
    transform: translateY(-50%);
    cursor: pointer;
  }
  .hamburger {
    width: 100%;
    height: 10%;
    background-color: #FAFAFA;
    border-radius: 2px;
    position: absolute;
    right:0;
    transition: all 0.1s linear;
  }
  .hamburger-top {
    top: 0;
  }
  .hamburger-mid {
    top: 50%;
    transform: translateY(-50%);
  }
  .hamburger-bot {
    bottom: 0;
  }
  .hamburger-btn:hover .hamburger-top{
    width: 70%;
    transform: rotate(45deg) translateX(20%) translateY(30%);
  }
  .hamburger-btn:hover .hamburger-bot{
    width: 70%;
    transform: rotate(-45deg) translateX(20%)  translateY(-30%);
  }
  .side-bar-background {
    position:fixed;
    top:0;bottom:0;left:0;right:0;
    background-color: rgba(136, 136, 136, 0.3);
    transition: all 0.2s ease-out;
    z-index: 2;
  }
  .side-bar{
    position:fixed;
    top:0;
    left:0;
    bottom:0;
    width: 300px;
    color: white;
    opacity: 1 !important;
    background-color: rgb(29, 29, 31);
    box-shadow: 0 0 2rem 0 rgba(136,152,170,.15); 
    transform: translateX(-300px);
    transition: all 0.2s ease-out;
    z-index: 3;
  }
  .sidde-bar-top { 
    height: 70px;
    padding: 0 8px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .close-btn {
    width: 28px;
    height: 28px;
    cursor: pointer;
    background-image: url('../assets/icons/close.png');
    background-repeat: no-repeat;
    background-size: cover;
  }
  .display-none{
    display: none;
  }
  .opacity-0 {
    opacity: 0;
  }
  .side-bar-transform {
    transform: translateX(0);
  }
  .router-wrapper {
    padding-top: 44px;
    min-width: 100vw;
    min-height: 100vh;
  }

  @media (min-width:1024px) {
    nav {
      height: 52px;
      line-height: 52px;
    }
    .hamburger-btn {
      width: 30px;
      height: 20px;
    }
    .hamburger {
      height: 14%;
    }
    .hamburger-btn:hover .hamburger-top{
      transform: rotate(45deg) translateX(20%) translateY(-60%);
    }
    .hamburger-btn:hover .hamburger-bot{
      transform: rotate(-45deg) translateX(20%) translateY(60%);
    }
    .router-wrapper {
      padding-top: 52px;
    }
  }
</style>
