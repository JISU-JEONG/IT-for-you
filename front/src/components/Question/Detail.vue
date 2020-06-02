<template>
  <div class="main-content">
    <div
      :class="i === 0 ? 'now' : ''"
      v-for="(q, i) in questionList"
      :key="q.p_id"
    >
      <div class="questionInfo">
        <span class="info-badge color-info">{{ q.category.pc_value }}</span>
        <span class="info-badge color-info">{{
          questionType[q.pt_id - 1].pt_value
        }}</span>
        <span class="info-badge color-info">난이도 - {{ q.pd_id }}</span>
        <span class="info-badge float-right" :class="{'color-secondary':!q.myprob_check , 'color-warning':q.myprob_check }" id="like-btn" @click="onClickMyNote(q.p_id)">문제 저장하기</span>
      </div>
      <div class="question">{{ i }}. {{ q.p_question }}</div>
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
      <div v-if="q.pt_id === 2 || q.pt_id === 3" class="answer-container">
        <div
          v-for="a in q.answers"
          :key="a.a_id"
          @click="selected()"
          :id="a.a_correct"
          :name="`problem${q.p_id}`"
          class="questionAnswer"
        >
          {{ a.a_value }}
        </div>
      </div>
      <!-- 단답식 -->
      <div v-if="q.pt_id === 4" class="answer-container">
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

        WrongAnswer = AnswerFlag === true ? Answer[0].a_value : null;
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
    },
    onClickMyNote(p_id) {
      const user_id = this.$store.state["auth"]["userInfo"]["id"];
      axios.post(`/api/myprobs/myprob/${user_id}/`, {
          "prob": p_id
        })
        .catch(err => {
          console.error(err)
        })
    }
  },
  computed: {
    questionList() {
      return this.$store.getters.questionList;
    },
    questionType() {
      return this.$store.getters.questionType;
    }
  },
  mounted() {
    console.log(this.questionList)
  }
};
</script>

<style scoped>
* {
  box-sizing: border-box;
}

.main-content {
  width: 100%;
  margin: 0 auto;
}

.main-content > div {
  display: none;
  padding: 20px;
}

.main-content > div.now {
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

.questionAnswer,
.current,
.question,
.commentary,
.currentButton span {
  font-family: ChosunSm;
}

.questionAnswer {
  border: 2px black solid;
  width: 100%;
  margin-bottom: 20px;
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

.currentButton span {
  border: 5px black solid;
  border-radius: 50px;
  font-size: 1.5rem;
  padding: 15px;
  margin: 50px;
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
