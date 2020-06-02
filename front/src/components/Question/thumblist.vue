<template>
  <div>
    <transition-group name="question" class="content__list">
      <div
        class="question"
        v-for="question in list"
        :key="question.problems.p_id"
      >
        <div class="question__info">
          <h2 class="question__name">{{ question.problems.p_question }}</h2>
          <blockquote class="question__slogan">
            {{ questionType[question.problems.pt_id] }}
          </blockquote>
        </div>

        <ul class="question__details">
          <label class="question__label">난이도</label>
          <p class="question__level">{{ level[question.problems.pd_id] }}</p>
        </ul>
      </div>
    </transition-group>
  </div>
</template>

<script>
export default {
  name: "thumblist",
  props: {
    list: {
      type: Array
    },
    questionType: {
      type: Array
    },
    level: {
      type: Array
    }
  }
};
</script>
