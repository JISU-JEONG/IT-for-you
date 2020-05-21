<template>
  <div>
    <Problem class="problem" />
  </div>
</template>

<script>
import Problem from "@/components/Question/Detail/Problem.vue";

export default {
  name: "Detail",
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