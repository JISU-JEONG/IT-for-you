<template>
  <div>
    <nav>
      <div class="hamburger-btn no_highlights" @click="openSideBar">
        <div class="hamburger hamburger-top"></div>
        <div class="hamburger hamburger-mid"></div>
        <div class="hamburger hamburger-bot"></div>
      </div>
      <p class="title">
        <span @click="home()" style="cursor: pointer; padding: 0 8px;"
          >IT For You</span
        >
      </p>
    </nav>
    <div
      class="side-bar-background display-none opacity-0"
      @click="closeSideBar"
    ></div>
    <div class="side-bar" :class="{ 'side-bar-transform': showSideBar }">
      <div class="sidde-bar-top">
        <h2 class="title" @click="home()" style="cursor: pointer;">
          IT For You
        </h2>
        <span class="close-btn" @click="closeSideBar"></span>
      </div>
      <div class="sidde-bar-profile">
        <span class="avata"></span>
        <div>
          <span class="username">{{ user.username }}</span>
          <span class="email">{{ user.email }}</span>
        </div>
      </div>

      <div class="side-bar-nav no_highlights" @click="onClickEvent">
        <li v-if="user.is_superuser">
          <router-link to="/admin">관리자페이지</router-link>
        </li>
        <li>
          <router-link to="/category">문제풀기</router-link>
        </li>
        <li>
          <router-link to="/interview">면접대비</router-link>
        </li>
        <li>
          <router-link to="/wrongNote">오답노트</router-link>
        </li>
        <li>
          <router-link to="/IT_Note">저장한 문제</router-link>
        </li>
        <li>
          <router-link to="/interview/mynote">저장한 면접</router-link>
        </li>
      </div>
      <div class="side-bar-logout no_highlights">
        <li @click="logout">
          <a>로그아웃</a>
        </li>
      </div>
    </div>
    <div class="router-wrapper">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import axios from "@/api/api.service.js";

export default {
  name: "Home",
  data() {
    return {
      showSideBar: false,
      isAuthenticated: this.$session.has("jwt")
    };
  },

  computed: {
    user() {
      return this.$store.getters.getUserInfo;
    }
  },
  methods: {
    home() {
      if (this.$router.history.current.name !== "IT_For_You") {
        this.$router.push("/");
      }
    },
    onClickEvent() {
      if (event.target.nodeName === "A") {
        this.closeSideBar();
      }
    },
    openSideBar() {
      const sideBarBackground = document.querySelector(".side-bar-background");
      sideBarBackground.classList.remove("display-none");
      setTimeout(function() {
        sideBarBackground.classList.remove("opacity-0");
      }, 20);
      this.showSideBar = !this.showSideBar;
    },
    closeSideBar() {
      const sideBarBackground = document.querySelector(".side-bar-background");
      if (sideBarBackground !== null) {
        sideBarBackground.classList.add("opacity-0");
        sideBarBackground.addEventListener(
          "transitionend",
          function() {
            sideBarBackground.classList.add("display-none");
          },
          {
            capture: false,
            once: true,
            passive: false
          }
        );
        this.showSideBar = !this.showSideBar;
      }
    },
    onCLickLink(path) {
      this.$router.push(`/testhome/${path}`);
      this.closeSideBar();
    },
    logout() {
      console.log('logout')
      this.$session.clear();
      this.$store.dispatch("logout");
      this.$router.push("/login");
    }
    // getUser() {
    //   // axios 요청시마다 헤더를 추가해서 보내야 함!
    //   const token = this.$session.get("jwt");
    //   const options = {
    //     headers: {
    //       Authorization: `JWT ${token}` // JWT 다음에 공백있음.
    //     }
    //   };
    //   axios
    //     .post("/api/accounts/user/", {}, options)
    //     .then(({ data }) => {
    //       console.log(data);
    //       this.user = data;
    //     })
    //     .catch(error => {
    //       console.log(error);
    //     });
    // }
  },
  beforeMount() {
    // console.log(this.$session);
    // this.$store.dispatch("getUser");
    // this.getUser();
  }
};
</script>

<style scoped>
.title {
  font-family: "godoMaum";
  font-size: 2.5em;
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
nav {
  width: 100vw;
  height: 44px;
  line-height: 44px;
  padding-left: 10px;
  text-align: center;
  position: fixed;
  top: 0;
  color: white;
  background-color: rgb(29, 29, 31);
  z-index: 2;
}
ul,
li {
  font-family: "Recipekorea";
  width: 100%;
  list-style: none;
}
li {
  height: 50px;
  line-height: 50px;
  margin: 10px 0;
}

.hamburger-btn {
  width: 20px;
  height: 15px;
  display: inline-block;
  position: absolute;
  left: 10px;
  top: 50%;
  transform: translateY(-50%);
  cursor: pointer;
}
.hamburger {
  width: 100%;
  height: 10%;
  background-color: #fafafa;
  border-radius: 2px;
  position: absolute;
  right: 0;
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
.hamburger-btn:hover .hamburger-top {
  width: 70%;
  transform: rotate(45deg) translateX(20%) translateY(30%);
}
.hamburger-btn:hover .hamburger-bot {
  width: 70%;
  transform: rotate(-45deg) translateX(20%) translateY(-30%);
}
.side-bar-background {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(136, 136, 136, 0.3);
  transition: all 0.2s ease-out;
  z-index: 2;
}
.side-bar {
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  height: 100vh;
  width: 300px;
  color: white;
  opacity: 1 !important;
  background-color: rgb(29, 29, 31);
  box-shadow: 0 0 2rem 0 rgba(136, 152, 170, 0.15);
  transform: translateX(-300px);
  transition: all 0.2s ease-out;
  z-index: 3;
}

.sidde-bar-top {
  height: 80px;
  padding: 0 8px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.sidde-bar-profile {
  height: 100px;
  /* background-color: darkslategray; */
  background-color: #4d4d4d;
  padding: 15px;
  display: flex;
  align-items: center;
}
.side-bar-nav {
  display: inline-block;
  padding-top: 20px;
  width: 100%;
}
.side-bar-nav a {
  width: 100%;
  padding: 0 20px;
  display: inline-block;
  font-size: 20px;
  color: rgb(162, 161, 161);
  text-decoration: none;
  cursor: pointer;
}
.side-bar-nav a.router-link-active {
  color: white;
}
.side-bar-nav a:hover {
  color: white;
}
.side-bar-logout {
  position: absolute;
  bottom: 10px;
  width: 100%;
  cursor: pointer;
}
.side-bar-logout a {
  margin-left: 20px;
}
.sidde-bar-profile .avata {
  display: inline-block;
  border: 1px solid white;
  border-radius: 80px;
  margin-right: 20px;
  width: 70px;
  height: 70px;
  background: url("https://image.flaticon.com/icons/svg/3011/3011536.svg");
  background-size: contain;
}

.sidde-bar-profile .username {
  font-family: "Recipekorea";
  font-size: 1.5rem;
  display: flex;
  align-items: center;
  height: 100%;
}

.close-btn {
  width: 28px;
  height: 28px;
  cursor: pointer;
  background-image: url("../../assets/icons/close.png");
  background-repeat: no-repeat;
  background-size: cover;
}
.display-none {
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
  height: 100vh;
  /* min-width: 100vw; */
  min-height: 100vh;
}

@media (min-width: 1024px) {
  nav {
    height: 52px;
    line-height: 52px;
    z-index: 2;
  }
  .hamburger-btn {
    width: 30px;
    height: 20px;
  }
  .hamburger {
    height: 14%;
  }
  .hamburger-btn:hover .hamburger-top {
    transform: rotate(45deg) translateX(20%) translateY(-60%);
  }
  .hamburger-btn:hover .hamburger-bot {
    transform: rotate(-45deg) translateX(20%) translateY(60%);
  }
  .router-wrapper {
    padding-top: 52px;
  }
}

@font-face {
  font-family: "Recipekorea";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/Recipekorea.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: "godoMaum";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/godoMaum.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
</style>
