<template>
  <div class="home">
    <Quiz />
    <create-question />
  </div>
</template>

<script>
import Quiz from "@/components/Quiz.vue";
import CreateQuestion from "@/components/CreateQuestion.vue";

export default {
  name: "Home",
  components: {
    Quiz
    CreateQuestion
  }
};
</script>
