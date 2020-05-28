<template>
  <div class="main-content">
    <div :class="i===0 ? 'now' : ''" v-for="(q, i) in questionList" :key="q.p_id">
      <div class="questionInfo">
        <span>{{q.category.pc_value}}</span>
        <span>{{questionType[q.pt_id-1].pt_value}}</span>
        <span>{{q.pd_id}}</span>
      </div>
      <div class="question">{{q.p_question}}</div>
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
        <div v-for="a in q.answers" :key="a.a_id" @click="selected()">
          <div :id="a.a_correct" :name="`problem${q.p_id}`" class="questionAnswer">{{a.a_value}}</div>
        </div>
      </div>
      <!-- 단답식 -->
      <div v-if="q.pt_id === 4">
        <span>
          <input :name="`problem${q.p_id}`" class="questionAnswer" type="text" />
        </span>
      </div>

      <div
        class="currentButton"
        v-if="buttonFlag"
        @click="checkProblem(`problem${q.p_id}`, q.pt_id)"
      >
        <span>정답 확인</span>
      </div>
      <div class="current" v-if="!buttonFlag">{{correctAnswer}}</div>
      <div class="commentary" v-if="!buttonFlag">해설 : {{q.p_commentary}}</div>
      <div class="currentButton" v-if="!buttonFlag" @click="nextProblem(i, questionList.length -1)">
        <span>다음 문제</span>
      </div>
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
      correctAnswer: null,
      oldAnswer: null
    };
  },
  methods: {
    selected(problemNumber) {
      if (this.oldAnswer !== null) {
        this.oldAnswer.classList.remove("active");
      }
      event.target.classList.add("active");
      this.oldAnswer = event.target;
    },
    checkProblem(problemNumber, type) {
      // 객관식, O/X
      if (type === 2 || type === 3) {
        const div = document.getElementsByName(problemNumber);

        if (this.oldAnswer.id === "true") {
          alert("맞음");
        } else {
          const res =
            "틀림 : " +
            div[
              [...div].findIndex(v => {
                return v.id === "true";
              })
            ].innerHTML;

          alert(res);
        }
      }
      // 단답형
      //   else if (type === 4) {
      //     const div = document.querySelector(problemNumber);
      //     let answer = null;
      //     const correctCheck = this.questionList[i].answers.some(
      //       ({ a_value }) => {
      //         return a_value.toLowerCase() === div.value.toLowerCase();
      //       }
      //     );

      //     this.correctAnswer =
      //       correctCheck === true
      //         ? "맞음"
      //         : "틀림(" + this.questionList[i].answers[0].a_value + ")";
      //   }
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