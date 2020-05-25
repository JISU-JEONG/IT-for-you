<template>
  <div>
    <nav>
      <span @click="openSideBar">hamburger</span>
    </nav>
    <div class="side-bar-background display-none opacity-0" @click="closeSideBar"></div>
    <div class="side-bar" :class="{'side-bar-transform': showSideBar}">
      <div class="sidde-bar-top">
        <h2>서비스 이름</h2>
        <span class="close-btn" @click="closeSideBar">X</span> <!-- 나중에 x 아이콘으로?-->
      </div>
      <div class="side-bar-content">
        <ul>
          <li><router-link to="/category">Category</router-link></li>
          <li><router-link to="/detail">Detail</router-link></li>
          <li><router-link to="/Admin">Admin</router-link></li>
          <li><router-link to="/login">login</router-link></li>
          <li><router-link to="/signup">signup</router-link></li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      showSideBar: false,
    }
  },
  methods: {
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
    border: 1px white solid;
  }
  a {
    width:100%;
    padding: 0 20px;
    display: inline-block;
    color: white;
    text-decoration: none;
  }
  .side-bar-background {
    position:fixed;
    top:0;bottom:0;left:0;right:0;
    background-color: rgba(136, 136, 136, 0.3);
    transition: all 0.2s ease-out;
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
  }
  .sidde-bar-top { 
    height: 70px;
    padding: 0 8px;
    display: flex;
    justify-content: space-between;
    align-items: center;
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
</style>
