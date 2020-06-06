<template>
  <div>
    <transition-group class="content__list">
      <div
        class="card-content"
        v-for="(question, i) in list"
        :key="question.problems.p_id"
      >
        <div class="card">
          <!-- 카드 헤더 -->
          <div class="card-header">
            <span>{{ questionType[question.problems.pt_id] }} </span>
            <span>{{ questionCategory[question.problems.pc_id] }}</span>
            <span>{{ level[question.problems.pd_id] }}</span>
          </div>

          <hr />
          <!--  카드 바디 -->
          <div class="card-body">
            <!--  카드 바디 헤더 -->
            <div class="card-body-header">
              {{ question.problems.p_question }}
            </div>

            <div
              class="card-body-header-code"
              v-if="question.problems.p_code !== null"
            >
              {{ question.problems.p_code }}
            </div>

            <!--  카드 바디 본문 -->
            <div class="card-trigger">
              <span>
                <figure @click="getUserAnswer(i)">
                  <img src="../../assets/icons/wrong.png" />
                  <figcaption>오답</figcaption>
                </figure>
              </span>

              <span>
                <figure @click="getAnswer(i)">
                  <img src="../../assets/icons/current.png" />
                  <figcaption>정답</figcaption>
                </figure>
              </span>
              <span>
                <figure @click="getTip(i)">
                  <img src="../../assets/icons/tip.png" />
                  <figcaption>해설</figcaption>
                </figure>
              </span>
            </div>
            <div :style="questionContent[i]" class="question-content">
              <div class="card-body-body-right" v-if="userAnswerFlag[i]">
                <del>{{ question.u_answer }}</del>
              </div>

              <div class="card-body-body-wrong" v-if="answerFlag[i]">
                {{ question.p_answer }}
              </div>

              <!--  카드 바디 푸터 -->
              <div class="card-body-footer" v-if="tipFlag[i]">
                {{ question.problems.p_commentary }}
              </div>
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
  data() {
    return {
      tipFlag: [...this.list].fill(false),
      userAnswerFlag: [...this.list].fill(false),
      answerFlag: [...this.list].fill(false),
      questionContent: [...this.list].fill("height:50px")
    };
  },
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
  methods: {
    getTip(i) {
      this.$set(this.tipFlag, i, !this.tipFlag[i]);
      const div2 = document.querySelectorAll(".question-content")[i];
      console.log(div2.style);
      div2.style.transform = "translateY(0%)";

      // setTimeout(() => {
      //   console.log(div2.style);
      //   div2.style.height = div.clientHeight;
      //   console.log(div.clientHeight);
      // }, 100);
      // this.$nextTick(() => {
      //   this.questionContent[i] = `height: ${div.clientHeight}}px`;
      // });
    },
    getUserAnswer(i) {
      this.$set(this.userAnswerFlag, i, !this.userAnswerFlag[i]);
      const div2 = document.querySelectorAll(".question-content")[i];
      console.log(div2.style);
      div2.style.transform = "translateY(0%)";
    },
    getAnswer(i) {
      this.$set(this.answerFlag, i, !this.answerFlag[i]);
      const div2 = document.querySelectorAll(".question-content")[i];
      console.log(div2.style);
      div2.style.transform = "translateY(0%)";
    }
  },
  beforeMount() {
    console.log(this.questionContent);
  }
};
</script>

<style lang="scss" scoped>
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
  height: 100%;
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

.card-body-header-code {
  border: 2px solid black;
  padding: 12px;
  border-radius: 5px;
  background-color: rgb(235, 235, 235);
}

hr {
  background-color: #9fa5a8;
  height: 1px;
  border: 1px;
}

.card-body-body-right,
.card-body-body-wrong,
.card-body-footer {
  line-height: 20px;
  font-size: 17px;
  padding: 10px;
  font-weight: bold;
  top: 30px;
}

.card-body-body-right {
  color: gray;
}

.card-body-body-wrong {
  color: red;
}

.question-content {
  transform: translateY(-10em);
  z-index: -1;
  transition: all 2s;
}

.card-trigger {
  font-weight: bold;
  display: flex;
  justify-content: space-between;
  margin: 10px;
  padding: 15px;
  border-radius: 15px;
  transition: 2s;
}

img {
  width: 50px;
  height: 50px;
}

figure {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
}
figcaption {
  margin-top: 15px;
}
</style>
