<template>
  <div>
    <transition-group>
      <div
        class="card-content"
        v-for="question in list"
        :key="question.problems.p_id"
      >
        <div class="card">
          <!-- 카드 헤더 -->
          <div class="card-header">
            <span>{{ questionType[question.problems.pt_id] }} </span>
            <span>{{ questionCategory[question.problems.pc_id] }}</span>
            <span>{{ level[question.problems.pd_id] }}</span>
            <span>X</span>
          </div>

          <!--  카드 바디 -->
          <div class="card-body">
            <!--  카드 바디 헤더 -->
            <div class="card-body-header">
              {{ question.problems.p_question }}
            </div>
            {{question.problems.p_code}}
            <!--  카드 바디 본문 -->
            <div class="card-body-body-right">
              <del>{{ question.u_answer }}</del>
            </div>
            <div class="card-body-body-wrong">
              {{ question.p_answer }}
            </div>

            <!--  카드 바디 푸터 -->
            <hr />
            <div class="card-body-footer">
              {{ question.problems.p_commentary }}
            </div>
          </div>
        </div>
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
    },
    questionType: {
      type: Array
    },
    questionCategory: {
      type: Array
    },
    level: {
      type: Array
    }
  },
  beforeMount(){
    console.log(this.list)
  }
};
</script>

<style scoped>
.card-content {
  width: 100%;
  padding: 30px;
}

@media (min-width: 612px) {
  .card-content {
    width: 100%;
    padding: 30px 50px;
  }
}

.card {
  width: 100%;
  padding: 10px;
  border-radius: 15px;
  display: inline-block;
  position: relative;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  overflow: hidden;
}

.card-header {
  width: 100%;
  font-weight: bold;
  text-align: center;
  font-weight: bold;
  line-height: 20px;
  padding: 15px;
  display: flex;
  justify-content: space-between;
}

.card-body-header {
  font-weight: bold;
  line-height: 25px;
  font-size: 20px;
  padding: 10px;
}

hr {
  background-color: #9fa5a8;
  height: 1px;
  border: 1px;
}

.card-body-body-right {
  font-weight: bold;
  line-height: 20px;
  font-size: 17px;
  padding: 10px;
  color: gray;
}

.card-body-body-wrong {
  font-weight: bold;
  line-height: 20px;
  font-size: 17px;
  padding: 10px;
  color: red;
}

.card-body-footer {
  font-weight: bold;
  line-height: 20px;
  font-size: 15px;
  padding: 10px;
}
</style>
