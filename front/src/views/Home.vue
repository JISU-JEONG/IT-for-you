<template>
  <div class="home">
    <QuestionDetail />
    <create-question />
  </div>
</template>

<script>
import QuestionDetail from "@/components/QuestionDetail/QuestionDetail.vue";
import CreateQuestion from "@/components/CreateQuestion.vue";

export default {
  name: "Home",
  components: {
    QuestionDetail,
    CreateQuestion
  }
};
</script>
