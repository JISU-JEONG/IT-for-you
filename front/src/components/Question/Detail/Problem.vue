<template>
<body>
  <div id="subhead"></div>
  <ul id="questionsList">
    <section :class="i === 0 ? 'current' : ''" v-for="(q, i) in question" :key="i">
      코드블럭 : {{ q.problems.p_code }} 레벨 :
      {{ q.problems.pd_id }} 카데고리 : {{ q.problems.pc_id }} 유형 :
      {{ questionType[q.problems.pt_id] }}
      <li>
        <p class="problem_question">{{ q.problems.p_question }}</p>
        <span class="questionItem" v-for="a in q.answers" :key="a">
          <input :id="a" type="radio" :name="q.answers" :value="a" />
          <label :for="a">{{ a }}</label>
        </span>
      </li>
      <a class="nextButton" @click="nextQuestion(i, question.length - 1, q.correct_ans)">정답 확인</a>
    </section>
  </ul>
</body>
</template>

<script>
import * as utils from "./Problem.js";
import * as Question from "../QuestionData.js";
import axios from "axios";

export default {
  name: "Problem",

  data() {
    return {
      question: Question.data2(),
      questions: document.getElementsByTagName("section"),
      questionType: ["OX퀴즈", "객관식", "주관식", "단답형", "녹음"]
    };
  },

  computed: {
    questionData() {
      return this.$store.getters.questionData;
    },
    filters() {
      return this.$store.getters.filters;
    }
  },

  // destroyed() {
  //   unrequire("./Promise.css");
  //   console.log("destroyed");
  // },

  mounted() {
    require("./Problem.css");
    utils.drow();
  },

  methods: {
    nextQuestion(i, size, currentAnswer) {
      if (i !== size) {
        this.questions[i].className = "";
        this.questions[i + 1].className = "current";
      }

      let answer = this.questions[i].getElementsByTagName("input");
      answer.forEach(v => {
        if (v.checked) {
          if (v.value === currentAnswer) {
            alert("맞음");
          } else {
            alert("틀림");
          }
        }
      });
    }
  }
};
</script>