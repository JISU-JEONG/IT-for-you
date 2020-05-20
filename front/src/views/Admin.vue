<template>
  <div class="wrapper">
    <section>
      <h1>서비스이름</h1>
      <ul>
        <li><router-link to="/admin/user"><i></i><span>회원 관리</span></router-link></li>
        <li><router-link to="/admin/make"><i></i><span>문제 생성</span></router-link></li>
        <li><router-link to="/admin/edit"><i></i><span>문제 수정</span></router-link></li>
      </ul>
    </section>
    <div class="admin-content">
      <router-view></router-view>
    </div>
  </div>
</template>
<script>
export default {
    data() {
      return {
      }
    },
    methods: {
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
        height: 45px;
        a {
          width: 100%;
          height: 100%;
          padding: 10px;
          position: relative;
          display: inline-block;
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
        }
      }
    }
  }
  .admin-content {
    height: 1500px;
    min-height: 100vh;  
    margin-left: 250px;
    padding: 40px;
    position:relative;
    &:before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 400px;
      background: linear-gradient(87deg, #2dce89 0, #2dcecc 100%);
      z-index: -1;
    }
  }
</style>