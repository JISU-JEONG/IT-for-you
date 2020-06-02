<template>
  <div>
    <transition-group name="question" tag="ul" class="content__list">
      <div
        class="list-content"
        v-for="question in list"
        :key="question.problems.p_id"
      >
        {{ question }}
      </div>
    </transition-group>
  </div>
</template>

<script>
export default {
  name: "list",
  props: {
    list: {
      type: Array
    }
  }
};
</script>

<style scoped>
.list-content {
  margin: 30px;
}
</style>
