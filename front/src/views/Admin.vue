<template>
  <div class="wrapper">
    <section>
      <h1>서비스이름</h1>
      <ul>
        <li>
          <router-link to="/admin/user">
            <i></i>
            <span>회원 관리</span>
          </router-link>
        </li>
        <li>
          <router-link to="/admin/make">
            <i></i>
            <span>문제 생성</span>
          </router-link>
        </li>
        <li>
          <router-link to="/admin/edit">
            <i></i>
            <span>문제 수정</span>
          </router-link>
        </li>
      </ul>
    </section>
    <div class="admin-content">
      <nav>
        <span>{{routerName[this.$router.history.current.name]}}</span>
        <div>어떤 기능</div>
      </nav>
      <div class="content-top"></div>
      <div class="content-layout">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>
<script>
export default {
    data() {
      return {
        routerName: {User: '회원관리', MakeQuestion: '문제 생성', EditQuestion: '문제 수정'}
      }
    },
    methods: {
      test(type){
        return require(`@/assets/icons/${type}.svg`)
      },
      // color() {
      //   // let style = "{mask-image: url(" + require("@/assets/icons/account.svg") + ")}; backgroundColor:red; width:100px; height:100px}";
      //   return "{mask-image: url('" + require("@/assets/icons/account.svg") + "); width:100px; height:100px}";
      // }
    },
    mounted() {
      // console.log()
    }
}
</script>
<style scoped lang='scss'>
section {
  width: 250px;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  border: 1px solid black;
  h1 {
    width: 100%;
    height: 100px;
    text-align: center;
    font-size: 36px;
    line-height: 100px;
    border: 1px solid red;
  }
  ul {
    li {
      width: 100%;
      height: 100px;
      text-align: center;
      font-size: 48px;
      line-height: 100px;
      border: 1px solid red;
      font-family: 'Cute Font', cursive;
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
            font-size: 24px;
            line-height: 28px;
            display: inline-block;
            font-family: 'Cute Font', cursive;
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
    border: 1px solid black;
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
    padding: 100px 40px;
    background: linear-gradient(87deg, #2dce89 0, #2dcecc 100%);
  }
  .content-layout {
    height: 650px;
    margin: -100px 40px 0;
    padding: 15px;
    background-color: rgb(255,255,255);
    border-radius: 10px;
    box-shadow: 0 0 2rem 0 rgba(136,152,170,.15); 
  }


</style>