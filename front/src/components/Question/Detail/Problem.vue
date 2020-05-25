<template>
  <body>
    <div id="subhead"></div>
    <ul id="questionsList">
      <section
        :class="i === 0 ? 'current' : ''"
        v-for="(q, i) in this.$store.getters.questionList"
        :key="i"
      >
        <p class="problem_question">{{ q.p_question }}</p>

        <div v-highlight v-if="q.p_code !== null">
          <pre class="language-javascript">
              <code>
                {{q.p_code}}
              </code>
            </pre>
        </div>
        <span class="questionItem" v-for="a in q.answers" :key="a.a_id">
          <input
            :id="a.a_value"
            type="radio"
            :name="q.answers"
            :value="a.a_value"
          />
          <label :for="a.a_value">{{ a.a_value }}</label>
        </span>
        <a
          class="nextButton"
          @click="nextQuestion(i, questionList.length - 1, q.correctAnswer)"
          >정답 확인</a
        >
      </section>
    </ul>
  </body>
</template>

<script>
import * as utils from "./Problem.js";
import * as Question from "../QuestionData.js";
import "@/utils/prism.css";
import axios from "@/api/api.service.js";

export default {
  name: "Problem",

  data() {
    return {
      questions: document.getElementsByTagName("section"),
      wrongAnswer: 0
      // questionType: ["OX퀴즈", "객관식", "주관식", "단답형", "녹음"]
      // questionData: this.$store.getter.questionData
    };
  },

  computed: {
    questionList() {
      return this.$store.getters.questionList;
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

  beforeMount() {
    console.log(this.$store.getters.questionList);
  },

  methods: {
    nextQuestion(i, size, currentAnswer) {
      console.log(currentAnswer);
      let answer = this.questions[i].getElementsByTagName("input");
      let problems = document.getElementsByClassName("questionItem");
      let button = document.getElementsByClassName("nextButton");

      answer.forEach((v, i) => {
        if (v.checked) {
          if (v.value === currentAnswer.value) {
            problems[currentAnswer.index].setAttribute(
              "style",
              "background:#99f19e"
            );
            // alert("맞음");
          } else {
            problems[this.wrongAnswer + i].setAttribute(
              "style",
              "background:#ff4e50"
            );
            problems[currentAnswer.index].setAttribute(
              "style",
              "background:#99f19e"
            );
            // alert("틀림");
          }
        }
      });
      this.wrongAnswer += answer.length;
      setTimeout(() => {
        if (i !== size) {
          this.questions[i].className = "";
          this.questions[i + 1].className = "current";
        }
      }, 3000);
    }
  }
};
</script>
