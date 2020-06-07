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
            <span>{{ questionType[question.problems.pt_id] }}</span>
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

            <div class="question-content">
              <div class="card-body-body-wrong" v-if="userAnswerFlag[i]">
                <del>{{ question.u_answer }}</del>
              </div>

              <div class="card-body-body-right" v-if="answerFlag[i]">
                {{ question.p_answer }}
              </div>

              <!--  카드 바디 푸터 -->
              <div class="card-body-footer" v-if="tipFlag[i]">
                {{ question.problems.p_commentary }}
              </div>
              <div class="tip">{{ question.problems.p_commentary }}</div>
              <div class="userAnswer">{{ question.u_answer }}</div>
              <div class="answer">{{ question.p_answer }}</div>
            </div>
          </div>
        </div>
      </div>
    </transition-group>
  </div>
</template>

<script>
import axios from "@/api/api.service.js";

export default {
  name: "myNote",
  data() {
    return {
      tipFlag: null,
      userAnswerFlag: null,
      answerFlag: null,
      tmpheight: null
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
  watch: {
    list() {
      this.tipFlag = [...this.list].fill(false);
      this.userAnswerFlag = [...this.list].fill(false);
      this.answerFlag = [...this.list].fill(false);
      this.tmpheight = [...this.list].fill(false);

      const div = document.querySelectorAll(".question-content");
      div.forEach(v => {
        v.style.height = 0;
      });
      console.log("바뀜");
    }
  },
  methods: {
    getStyle(name, num, i) {
      const div3 = document.querySelector(name);
      div3.style.opacity = num;
    },

    getTip(i) {
      this.$set(this.tipFlag, i, !this.tipFlag[i]);
      const div = document.querySelectorAll(".question-content")[i];
      const div2 = document.querySelectorAll(".tip")[i];
      if (this.tipFlag[i] === true) {
        this.tmpheight[i] += div2.clientHeight;
        div.style.height = `${this.tmpheight[i]}px`;
        this.$nextTick(() => {
          this.getStyle(".card-body-footer", 1, i);
        });
      } else {
        this.tmpheight[i] -= div2.clientHeight;
        div.style.height = `${this.tmpheight[i]}px`;
      }
    },
    getAnswer(i) {
      this.$set(this.answerFlag, i, !this.answerFlag[i]);
      const div = document.querySelectorAll(".question-content")[i];
      const div2 = document.querySelectorAll(".answer")[i];
      if (this.answerFlag[i] === true) {
        this.tmpheight[i] += div2.clientHeight;
        div.style.height = `${this.tmpheight[i]}px`;
        this.$nextTick(() => {
          this.getStyle(".card-body-body-right", 1, i);
        });
      } else {
        this.tmpheight[i] -= div2.clientHeight;
        div.style.height = `${this.tmpheight[i]}px`;
      }
    }
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

.card-body-body-right,
.card-body-footer {
  line-height: 20px;
  font-size: 17px;
  padding: 10px;
  opacity: 0;
  transition: all 2s;
  font-weight: bold;
}

.question-content {
  height: 0px;
  transition: all 0.5s;
}

.card-trigger {
  font-weight: bold;
  display: flex;
  justify-content: space-between;
  margin: 10px;
  padding: 15px;
  border-radius: 15px;
}

.tip,
.answer,
.userAnswer {
  line-height: 20px;
  font-size: 17px;
  padding: 10px;
  position: absolute;
  visibility: hidden;
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
