<template>
  <div class="main-content">
    <div :class="i===0 ? 'current' : ''" v-for="(q, i) in questionList" :key="q.p_id">
      <div class="questionInfo">
        <span>{{q.category.pc_value}}</span>
        <span>{{questionType[q.pt_id-1].pt_value}}</span>
        <span>{{q.pd_id}}</span>
      </div>
      <div>{{q.p_question}}</div>
      <div v-highlight v-if="q.p_code !== null">
        <pre class="language-javascript">
          <code>
            {{q.p_code}}
          </code>
        </pre>
      </div>

      <!-- 인터뷰 -->
      <div v-if="q.pt_id === 1">인터뷰</div>

      <!-- 객관식, O/X -->
      <div v-if="q.pt_id === 2 || q.pt_id === 3">
        <div v-for="a in q.answers" :key="a.a_id">
          <span>
            <input
              type="radio"
              :class="`problem${q.p_id}`"
              :name="q.p_id"
              :value="a.a_value"
              :id="a.a_correct"
            />
            <label :for="a.a_value">{{ a.a_value }}</label>
          </span>
        </div>
      </div>

      <!-- 단답식 -->
      <div v-if="q.pt_id === 4">
        <span>
          <input :class="`problem${q.p_id}`" type="text" />
        </span>
      </div>

      <div v-if="buttonFlag" @click="checkProblem(i, `.problem${q.p_id}`, q.pt_id)">정답 확인</div>
      <div v-if="!buttonFlag">{{correctAnswer}}</div>
      <div v-if="!buttonFlag">해설 : {{q.p_commentary}}</div>
      <div v-if="!buttonFlag" @click="nextProblem(i)">다음 문제</div>
    </div>
  </div>
</template>

<script>
import axios from "@/api/api.service.js";

export default {
  name: "Category",
  data() {
    return {
      buttonFlag: true,
      correctAnswer: null
    };
  },
  methods: {
    checkProblem(i, problemNumber, type) {
      // 객관식, O/X
      if (type === 2 || type === 3) {
        const div = document.querySelectorAll(problemNumber);
        div.forEach(({ id, checked }, i) => {
          if (id) {
            if (checked) {
              this.correctAnswer = "맞음";
            } else {
              this.correctAnswer = "틀림 : (" + div[i].value + ")";
            }
          }
        });
      }
      // 단답형
      else if (type === 4) {
        const div = document.querySelector(problemNumber);
        let answer = null;
        const correctCheck = this.questionList[i].answers.some(
          ({ a_value }) => {
            return a_value.toLowerCase() === div.value.toLowerCase();
          }
        );

        this.correctAnswer =
          correctCheck === true
            ? "맞음"
            : "틀림(" + this.questionList[i].answers[0].a_value + ")";
      }
      this.buttonFlag = !this.buttonFlag;
    },
    nextProblem(i) {
      const div = document.querySelectorAll(".main-content > div");
      div[i].className = "";
      div[i + 1].className = "current";
      this.buttonFlag = !this.buttonFlag;
    }
  },
  computed: {
    questionList() {
      return this.$store.getters.questionList;
    },
    questionType() {
      return this.$store.getters.questionType;
    }
  }
};
</script>

<style scoped>
* {
  box-sizing: border-box;
}

.main-content {
  width: 100vw;
  height: 100vh;
  margin: 0 auto;
}

.main-content > div {
  display: none;
  margin: 30px;
}

.main-content > div.current {
  display: block;
}

.questionInfo {
  display: flex;
  justify-content: space-between;
}

div {
  margin-top: 20px;
  margin-bottom: 20px;
}

.active {
  width: 100px;
}
</style>