<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <Nav msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
import Nav from "@/components/Nav.vue";

export default {
  name: "Home",
  components: {
    Nav
  }
};
</script>
