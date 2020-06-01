<template>
  <div class="main-content">
    <div
      :class="i === 0 ? 'now' : ''"
      v-for="(q, i) in questionList"
      :key="q.p_id"
    >
      <div class="questionInfo">
        <span>{{ q.category.pc_value }}</span>
        <span>{{ questionType[q.pt_id - 1].pt_value }}</span>
        <span>{{ q.pd_id }}</span>
      </div>
      <div class="question">{{ q.p_question }}</div>
      <div v-highlight v-if="q.p_code !== null" class="codeDIV">
        <pre>
          <code>
            {{q.p_code}}
          </code>
        </pre>
      </div>

      <!-- 인터뷰 -->
      <div v-if="q.pt_id === 1">인터뷰</div>

      <!-- 객관식, O/X -->
      <div v-if="q.pt_id === 2 || q.pt_id === 3">
        <div v-for="a in q.answers" :key="a.a_id" @click="selected()">
          <div
            :id="a.a_correct"
            :name="`problem${q.p_id}`"
            class="questionAnswer"
          >
            {{ a.a_value }}
          </div>
        </div>
      </div>
      <!-- 단답식 -->
      <div v-if="q.pt_id === 4">
        <span>
          <input
            v-model="shortAnswer"
            :name="`problem${q.p_id}`"
            class="questionAnswer"
            type="text"
          />
        </span>
      </div>

      <div
        class="currentButton"
        v-if="buttonFlag"
        @click="checkProblem(`problem${q.p_id}`, q.pt_id, q.answers, q.p_id)"
      >
        <span>정답 확인</span>
      </div>
      <div class="current" v-if="!buttonFlag">{{ correctAnswer }}</div>
      <div class="commentary" v-if="!buttonFlag">
        해설 : {{ q.p_commentary }}
      </div>
      <div
        class="currentButton"
        v-if="!buttonFlag"
        @click="nextProblem(i, questionList.length - 1)"
      >
        <span>다음 문제</span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "@/api/api.service.js";
import "@/utils/prism.css";

export default {
  name: "Category",
  data() {
    return {
      buttonFlag: true,
      correctAnswer: null,
      oldAnswer: null,
      shortAnswer: null
    };
  },
  methods: {
    selected() {
      if (this.oldAnswer !== null) {
        this.oldAnswer.classList.remove("active");
      }
      event.target.classList.add("active");
      this.oldAnswer = event.target;
    },
    checkProblem(problemNumberClass, type, Answer, problemNumber) {
      let WrongAnswer = null; // 맞았는지 틀렸는지 판단

      // 인터뷰
      if (type === 1) {
        console.log("인터뷰");
      }

      // 객관식, O/X
      else if (type === 2 || type === 3) {
        if (this.oldAnswer === null) {
          alert("보기를 선택해주세요.");
          return;
        }
        const div = document.getElementsByName(problemNumberClass);
        if (this.oldAnswer.id === "true") {
          console.log("맞음");
        } else {
          WrongAnswer = div[[...div].findIndex(v => v.id === "true")].innerHTML;
          // "틀림 : " +
          // div[
          //   [...div].findIndex(v => {
          //     return v.id === "true";
          //   })
          // ].innerHTML;

          console.log("틀림 : " + WrongAnswer);
        }
        this.oldAnswer = null;
        this.shortAnswer = null;
      }
      // 단답형
      else if (type === 4) {
        if (this.shortAnswer === null) {
          alert("답변을 입력해주세요.");
          return;
        }

        const AnswerFlag = Answer.some(({ a_value }) => {
          return a_value.toLowerCase() === this.shortAnswer.toLowerCase();
        });

        WrongAnswer = AnswerFlag === true ? null : Answer[0].a_value;
        this.oldAnswer = null;
        this.shortAnswer = null;
        console.log("틀림 : " + WrongAnswer);
      }

      if (WrongAnswer !== null) {
        const user_id = this.$store.state["auth"]["userInfo"]["id"];
        console.log(user_id);
        console.log(WrongAnswer);

        axios
          .post(`/api/xnotes/mynote/${user_id}/`, {
            prob: problemNumber,
            u_answer: WrongAnswer.trim()
          })
          .then(({ data }) => {
            console.log(data);
          });
      }
      this.buttonFlag = !this.buttonFlag;
    },
    nextProblem(i, size) {
      if (i !== size) {
        const div = document.querySelectorAll(".main-content > div");
        div[i].className = "";
        div[i + 1].className = "now";
        this.buttonFlag = !this.buttonFlag;
      }
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

.main-content > div.now {
  display: block;
}

.questionInfo {
  font-family: "Recipekorea";
  font-size: 1.5rem;
  display: flex;
  justify-content: space-between;
}

.questionAnswer,
.current,
.question,
.commentary,
.currentButton span {
  font-family: "BMDOHYEON";
}

.questionAnswer {
  border: 5px black solid;
  width: 100%;
}

.question {
  font-size: 2rem;
}

.currentButton {
  display: flex;
  justify-content: center;
}

.currentButton span {
  border: 5px black solid;
  border-radius: 50px;
  font-size: 1.5rem;
  padding: 15px;
  margin: 50px;
}

div {
  margin-top: 20px;
  margin-bottom: 20px;
}

.codeDIV {
  overflow-x: scroll;
}

pre {
  white-space: pre;
}

.active {
  background: gray;
}

@font-face {
  font-family: "Recipekorea";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/Recipekorea.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: "Openas";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_nine_@1.1/Openas.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: "BMDOHYEON";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/BMDOHYEON.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
</style>
