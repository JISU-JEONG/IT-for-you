<template>
  <div class="home">
    <router-link class="router" to="/testhome">TestHome</router-link>
    <router-link class="router" to="/category">Category</router-link>
    <router-link class="router" to="/detail">Detail</router-link>
    <router-link class="router" to="/Admin">Admin</router-link>
    <router-link class="router" to="/login">login</router-link>
    <router-link class="router" to="/signup">signup</router-link>
  </div>
</template>

<script>
export default {
  name: "Home"
};
</script>

<style scoped>
.home {
  width: 100%;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
.home .router {
  margin: 20px;
  padding: 20px;
}
</style>
