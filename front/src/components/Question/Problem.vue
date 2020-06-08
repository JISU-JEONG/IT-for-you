<template>
  <div class="main-content">
    <div class="progress-bar">
      <div class="progress"></div>
    </div>
    <div class="checking-container">
      <div class="checking" v-for="i in questionList.length" :key="i">
        <div class="checking-inner" :data-checking="i">{{ i }}</div>
      </div>
    </div>
    <div
      class="question-box"
      :class="i === 0 ? 'now' : ''"
      v-for="(q, i) in questionList"
      :key="q.p_id"
    >
      <div class="questionInfo">
        <!-- 카테고리, 유형, 난이도, 문제 찜하기-->
        <span class="info-badge color-info">{{ q.category.pc_value }}</span>
        <span class="info-badge color-info">{{
          questionType[q.pt_id - 1].pt_value
        }}</span>
        <span class="info-badge color-info">난이도 - {{ q.pd_id }}</span>
        <span
          class="info-badge float-right"
          :class="{
            'color-secondary': !q.myprob_check,
            'color-warning': q.myprob_check
          }"
          id="like-btn"
          @click="onClickMyNote(q.p_id, i)"
          >문제 저장하기</span
        >
      </div>
      <div class="question">{{ i + 1 }}. {{ q.p_question }}</div>
      <!-- 문제 -->
      <div
        v-highlight
        v-if="q.p_code !== 'NULL' && q.p_code !== null"
        class="codeDIV"
      >
        <!-- 코드 -->
        <pre>
          <code style="white-space: pre-line;">
            {{q.p_code}}
          </code>
        </pre>
      </div>
      <!-- 객관식 -->
      <div v-if="q.pt_id === 2" class="answer-container">
        <div v-for="a in q.answers" :key="a.a_id">
          <input
            type="radio"
            class="input"
            :id="a.a_id"
            v-model="userAnswer"
            :value="a.a_value"
            :disabled="!buttonFlag"
          />
          <label :for="a.a_id" class="label no_highlights">{{
            a.a_value
          }}</label>
        </div>
      </div>
      <!-- O / X -->
      <div v-if="q.pt_id === 3" class="answer-container ox-container">
        <input
          type="radio"
          class="input"
          id="O"
          v-model="userAnswer"
          value="O"
          :disabled="!buttonFlag"
        />
        <label for="O" class="label no_highlights">O</label>
        <input
          type="radio"
          class="input"
          id="X"
          v-model="userAnswer"
          value="X"
          :disabled="!buttonFlag"
        />
        <label for="X" class="label no_highlights">X</label>
      </div>
      <!-- 단답식 -->
      <div v-if="q.pt_id === 4" class="answer-container">
        <input
          v-model="userAnswer"
          placeholder="답을 입력해주세요"
          class="short-answer"
          type="text"
          :disabled="!buttonFlag"
        />
      </div>
      <!-- 정답 체크 -->
      <button
        class="btn check-btn no_highlights"
        v-if="buttonFlag"
        @click="checkProblem(i, q.pt_id, q.answers, q.p_id)"
        :disabled="!userAnswer"
      >
        정답 확인
      </button>

      <div class="current" v-if="!buttonFlag && q.pt_id === 4">
        정답 : {{ answerList[i].join(", ") }}
      </div>
      <div class="commentary" v-if="!buttonFlag">
        해설 : {{ q.p_commentary }}
      </div>
      <!-- 다음 문제로 -->
      <button
        class="btn no_highlights"
        v-if="!buttonFlag && i !== questionList.length - 1"
        @click="nextProblem(i, questionList.length - 1)"
      >
        다음 문제
      </button>
      <!-- 오답노트로-->
      <button
        class="btn wrongnote-btn no_highlights"
        v-if="!buttonFlag && i === questionList.length - 1"
        @click="goToWrongNote"
      >
        오답 노트로 이동
      </button>
    </div>
  </div>
</template>

<script>
import axios from "@/api/api.service.js";
import "@/utils/prism.css";

export default {
  name: "Category",
  components: {},
  data() {
    return {
      buttonFlag: true,
      correctAnswer: null,
      oldAnswer: null,
      shortAnswer: null,
      userAnswer: "",
      correctLabel: "" // 오답일 때 정답 체크해 주기 위한 것.
    };
  },
  methods: {
    progressInit() {
      // progress bar 처음 한칸 설정
      const progress = document.querySelector(".progress");
      progress.style.width = `${(1 / this.questionList.length) * 100}%`;
    },
    selected() {
      if (this.buttonFlag === false) {
        return;
      }
      if (this.oldAnswer !== null) {
        this.oldAnswer.classList.remove("active");
      }
      event.target.classList.add("active");
      this.oldAnswer = event.target;
    },
    checkProblem(index, type, Answer, problemNumber) {
      const mainContent = document.querySelector(".main-content");
      const checking = document.querySelectorAll(".checking-inner")[index];

      let correct = false;

      if (type === 2 || type === 3) {
        this.correctLabel = [
          ...document.querySelectorAll(".now .label")
        ].filter(q => q.innerText === this.answerList[index][0])[0];

        if (this.answerList[index][0] === this.userAnswer) {
          correct = true;
          checking.classList.add("checking-correct");
          mainContent.classList.add("correct");
        } else {
          correct = false;
          checking.classList.add("checking-wrong");
          mainContent.classList.add("wrong");
          this.correctLabel.classList.add("correct-label");
          this.wrongAnswer(this.userAnswer, problemNumber); // 오답노트 추가
        }
      } else if (type === 4) {
        const AnswerFlag = this.answerList[index].some(answer => {
          return answer.toLowerCase() === this.userAnswer.toLowerCase().trim();
        });
        if (AnswerFlag) {
          correct = true;
          checking.classList.add("checking-correct");
          mainContent.classList.add("correct");
        } else {
          correct = false;
          checking.classList.add("checking-wrong");
          mainContent.classList.add("wrong");
          this.wrongAnswer(this.userAnswer, problemNumber); // 오답노트 추가
        }
      }

      const token = this.$session.get("jwt");
      const user_id = this.$store.state["auth"]["userInfo"]["id"];

      axios
        .post(
          "/api/accounts/userprob/",
          {
            user: user_id,
            prob: problemNumber,
            correct: correct
          },
          {
            headers: {
              Authorization: `JWT ${token}` // JWT 다음에 공백있음.
            }
          }
        )
        .then(({ data }) => {
          console.log(data);
        });

      this.buttonFlag = !this.buttonFlag;
    },
    wrongAnswer(userAnswer, problemNumber) {
      console.log(userAnswer);
      console.log(problemNumber);
      const user_id = this.$store.state["auth"]["userInfo"]["id"];
      axios
        .post(`/api/xnotes/mynote/${user_id}/`, {
          prob: problemNumber,
          u_answer: userAnswer
        })
        .then(({ data }) => {
          console.log(data);
        });
    },
    nextProblem(i, size) {
      const mainContent = document.querySelector(".main-content");
      if (i !== size) {
        const div = document.querySelectorAll(".question-box");
        div[i].classList.remove("now");
        div[i + 1].classList.add("now");
        this.buttonFlag = !this.buttonFlag;
        this.userAnswer = "";

        if (mainContent.classList.contains("wrong")) {
          mainContent.classList.remove("wrong");
        }
        if (mainContent.classList.contains("correct")) {
          mainContent.classList.remove("correct");
        }
        if (this.correctLabel) {
          this.correctLabel.remove("correct-label");
          this.correctLabel = "";
        }
        // progress bar 색 채우기
        const progress = document.querySelector(".progress");
        progress.style.width = `${((i + 2) / (size + 1)) * 100}%`;
      }
    },
    goToWrongNote() {
      this.$router.push("/wrongNote");
    },
    onClickMyNote(p_id, index) {
      const user_id = this.$store.state["auth"]["userInfo"]["id"];
      const question = this.questionList[index];
      if (!question.myprob_check) {
        axios
          .post(`/api/myprobs/myprob/${user_id}/`, {
            prob: p_id
          })
          .then(res => {
            question.myprob_check = true;
          })
          .catch(err => {
            console.error(err);
          });
      }
    }
  },
  computed: {
    questionList() {
      return this.$store.getters.questionList;
    },
    questionType() {
      return this.$store.getters.questionType;
    },
    answerList() {
      return this.$store.getters.answerList;
    }
  },
  mounted() {
    this.progressInit();
    console.log("init", this.questionList);
    console.log("answer", this.answerList);
  }
};
</script>

<style scoped>
* {
  box-sizing: border-box;
}
.no_highlights {
  -webkit-tap-highlight-color: transparent;
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.input {
  display: none;
}
.label {
  width: 100%;
  padding: 12px 8px;
  margin-bottom: 16px;
  display: inline-block;
  position: relative;
  border-radius: 5px;
  box-shadow: 0 0 8px lightgray;
  cursor: pointer;
  overflow: hidden;
}
.label::before {
  width: 0;
  height: 100%;
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  background-color: rgba(33, 149, 243, 0.25);
  transform: translate(-50%, -50%);
  transition: all 0.5s;
}
.wrong .label::before {
  background-color: rgba(136, 136, 136, 0.2);
}
.wrong .correct-label {
  background-color: rgba(0, 128, 0, 0.2);
}
.correct .label::before {
  background-color: rgba(0, 128, 0, 0.2);
}
.input:checked + .label::before {
  width: 100%;
}
/* .input:checked+.label {
  color: #0D47A1; 선택된거 글씨색도 바꾸고 싶었으나..
} */
.ox-container {
  display: flex;
  justify-content: space-around;
}
.ox-container .label {
  width: 120px;
  height: 120px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 40px;
  font-weight: bold;
  color: #888;
}
.short-answer {
  width: 100%;
  padding: 8px;
  margin-bottom: 16px;
  display: inline-block;
  border: 1px solid black;
  border-radius: 5px;
  outline: none;
  font-size: 18px;
}
.short-answer:placeholder-shown {
  border: 1px solid transparent;
  border-bottom-color: #888;
  border-radius: 0;
}
.wrong .short-answer:disabled {
  border: 2px solid #f44336;
  background-color: rgba(244, 67, 54, 0.3);
  color: #b71c1c;
  font-weight: 600;
}
.correct .short-answer:disabled {
  border: 2px solid #4caf50;
  background-color: rgba(7, 175, 79, 0.3);
  color: #1b5e20;
  font-weight: 600;
}
.btn {
  width: 100%;
  height: 52px;
  border: 1px solid rgb(29, 29, 31);
  border-radius: 5px;
  padding: 8px;
  font-size: 18px;
  margin-top: 12px;
  color: white;
  background-color: rgb(29, 29, 31);
  display: inline-block;
  transition: all 0.3s linear;
  cursor: pointer;
}
.wrongnote-btn {
  background-color: #f44336;
  border: 1px solid #f44336;
}
.check-btn:disabled {
  color: #9e9e9e;
  border: 1px solid #9e9e9e;
  background-color: transparent;
}
.progress-bar {
  width: 100%;
  height: 8px;
  box-shadow: 0 0 4px rgb(59, 59, 59);
  /* box-shadow: 0 0 2rem 0 rgba(136, 152, 170, 0.534); */
  position: relative;
}
.progress {
  width: 0;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  transition: width 0.5s linear;
  background-color: #30a9de;
}
.checking-container {
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  border: 1px solid block;
}
.checking {
  width: 10%;
  position: relative;
}
.checking::after {
  content: "";
  display: block;
  padding-bottom: 100%;
}
.checking-inner {
  width: 100%;
  height: 100%;
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: inset 0 0 2px #9e9e9e;
}
.checking-correct {
  background-color: rgba(76, 175, 79, 0.3);
  box-shadow: inset 0 0 2px #4caf50;
}
.checking-correct::before {
  position: absolute;
  content: "O";
  font-size: 24px;

  color: rgba(76, 175, 79, 0.9);
}
.checking-wrong {
  background-color: rgba(244, 67, 54, 0.3);
  box-shadow: inset 0 0 2px #f44336;
}
.checking-wrong::before {
  position: absolute;
  content: "X";
  font-size: 24px;
  color: rgba(244, 67, 54, 0.9);
}

.main-content {
  width: 100%;
  height: 100%;
  max-width: 500px;
  margin: 0 auto;
  position: relative;
}

.question {
  padding: 0;
  margin: 0;
}

.question-box {
  display: none;
  padding: 20px;
}

.question-box.now {
  display: block;
}
.questionInfo {
  width: 100%;
  height: 40px;
}
.info-badge {
  padding: 6px;
  margin-right: 6px;
  font-size: 15px;
  border-radius: 5px;
  color: white;
  font-family: Openas;
  float: left;
}
#like-btn {
  cursor: pointer;
}
.color-info {
  background-color: #17a2b8;
}
.color-warning {
  background-color: #ffc107;
}
.color-secondary {
  background-color: #6c757d;
}
.float-right {
  float: right;
}
.commentary {
  margin-top: 12px;
}

.questionAnswer,
.current,
.question,
.btn,
.commentary,
.currentButton span {
  font-family: ChosunSm;
}

.question {
  font-size: 1.3rem;
  line-height: 2rem;
  margin-bottom: 20px;
}

.currentButton {
  display: flex;
  justify-content: center;
}

.currentButton {
  border: 5px black solid;
  border-radius: 50px;
  font-size: 1.5rem;
  padding: 15px;
  margin: 50px auto;
}
.answer-container {
  /* marg */
}

.codeDIV {
  overflow-x: scroll;
  margin-bottom: 20px;
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
@font-face {
  font-family: "ChosunSm";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@1.1/ChosunSm.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
</style>
