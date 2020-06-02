<template>
  <div>
    <transition-group class="content__list">
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

<style lang="scss" scoped>
.content {
  &__list {
    position: relative;
    margin-top: 1rem;
    padding-right: 1rem;
    padding-bottom: 5rem;
    backface-visibility: hidden;
  }
}
.question {
  position: relative;
  width: calc(100% / 2 - 1rem);
  display: inline-flex;
  flex-direction: column;
  justify-content: space-between;
  margin-left: 1rem;
  margin-top: 1rem;
  padding-top: 0.75rem;
  border-radius: 6px;
  background-color: white;
  box-shadow: 0 0 0 1px #c5d0d1;
  backface-visibility: hidden;
  transform-origin: 10% 50%;
  z-index: 1;

  @media (min-width: 800px) {
    width: calc(100% / 3 - 1rem);
  }

  &__label {
    font-family: "MapoPeacefull";
    font-size: 0.8rem;
  }
  &__level {
    font-family: "MapoPeacefull";
    text-align: center;
  }

  &__info {
    padding: 0 0.75rem;
    text-align: center;
  }

  &__name {
    overflow: hidden;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;

    font-family: "CookieRunOTF-Bold";
    height: 4rem;
    margin: 0.75rem 0;
    font-size: 1rem;
    font-weight: 200;
    text-align: center;
  }

  &__details {
    display: flex;
    justify-content: space-between;
    margin-top: 1.5rem;
    padding: 0.5rem 0.75rem;
    background-color: rgba(#c5d0d1, 0.1);
    border-top: 1px solid #c5d0d1;
  }
}
</style>
