<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <Nav msg="Welcome to Your Vue.js App" />
    <create-question />
  </div>
</template>

<script>
import Nav from "@/components/Nav.vue";
import CreateQuestion from "@/components/CreateQuestion.vue";

export default {
  name: "Home",
  components: {
    Nav,
    CreateQuestion
  }
};
</script>
