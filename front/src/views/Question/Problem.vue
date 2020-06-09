<template>
  <div>
    <Detail class="problem" />
  </div>
</template>

<script>
import Problem from "@/components/Question/Problem.vue";

export default {
  name: "Problem",
  components: {
    Problem
  }
};
</script>

<style scoped>
.problem {
  margin-top: 100px;
}
</style>
