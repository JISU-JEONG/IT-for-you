<template>
<body>
  <div id="subhead"></div>
  <ul id="questionsList">
    <section :class="i === 0 ? 'current' : ''" v-for="(q, i) in questionList" :key="i">
      <p class="problem_question">{{ q.p_question }}</p>

      <div v-highlight v-if="q.p_code !== null">
        <pre class="language-javascript">
          <code>
            {{q.p_code}}
          </code>
        </pre>
      </div>
      <div v-if="q.pt_id !== 4">
        <span class="questionItem" v-for="a in q.answers" :key="a.a_id">
          <input :id="a.a_id" type="radio" :name="q.p_id" :value="a.a_value" />
          <label :for="a.a_id">{{ a.a_value }}</label>
        </span>
      </div>
      <div v-else>
        <br />
        <input class="questionItem" type="text" v-model="shortAnswer" />
      </div>
      <a
        class="nextButton"
        @click="
            nextQuestion(
              i,
              questionList.length - 1,
              q.currentAnswer,
              q.currentIndex,
              q.pt_id === 4
            )
          "
      >정답 확인</a>
    </section>
  </ul>
</body>
</template>

<script>
import * as utils from "./Problem.js";
import "@/utils/prism.css";
import axios from "@/api/api.service.js";

export default {
  name: "Problem",

  data() {
    return {
      questions: document.getElementsByTagName("section"),
      index: 0,
      shortAnswer: ""
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
    nextQuestion(i, size, currentAnswer, currentIndex, flag) {
      let answer = this.questions[i].getElementsByTagName("input");
      // let button = document.getElementsByClassName("nextButton");
      let problems = document.getElementsByClassName("questionItem");

      if (!flag) {
        answer.forEach((v, i) => {
          if (v.checked) {
            if (v.value === currentAnswer[0]) {
              problems[this.index + i].setAttribute(
                "style",
                "background:#99f19e"
              );
            } else {
              problems[this.index + i].setAttribute(
                "style",
                "background:#ff4e50"
              );
              problems[currentIndex].setAttribute(
                "style",
                "background:#99f19e"
              );
            }
          }
        });
        this.index += answer.length;
      } else {
        const res = currentAnswer.some(v => {
          return v.toLowerCase() === this.shortAnswer.toLowerCase();
        });

        if (res) {
          alert("맞음");
        } else {
          alert("틀림");
        }
      }
      setTimeout(() => {
        this.shortAnswer = "";
        if (i !== size) {
          this.questions[i].className = "";
          this.questions[i + 1].className = "current";
        }
      }, 3000);
    }
  }
};
</script>
