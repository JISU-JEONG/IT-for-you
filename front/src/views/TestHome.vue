<template>
  <div>
    <nav>
      hamburger
    </nav>
    <div class="side-bar">
    </div>
    <div class="container">

    </div>
    <router-link to="/category">Category</router-link>
    <router-link to="/detail">Detail</router-link>
    <router-link to="/Admin">Admin</router-link>
    <router-link to="/login">login</router-link>
    <router-link to="/signup">signup</router-link>
  </div>
</template>

<script>
export default {
  name: "Home"
};
</script>

<style scoped>
  /* nav */
  nav {
    height: 44px;
    position:fixed;
    top: 0;
    left: 0;
    right: 0;
    color: white;
    background-color: rgb(29, 29, 31);
  }
  .side-bar{
    width: 300px;
    height: 100vh;
    background-color: rgba(214, 214, 214, 0.356);
    z-index: 200000000;
  }
</style>
