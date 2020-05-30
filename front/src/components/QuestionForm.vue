<template>
  <div class="wrapper">
    <div class="input-container">
      <h2>문제 추가</h2>
      <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
        <span>
          카테고리:
          <select name="category" v-model="category">
            <option disabled value>카테고리</option>
            <option>Web</option>
            <option>Server</option>
            <option>Algorithm</option>
            <option>DataBase</option>
            <option>OS</option>
            <option>Network</option>
            <option>JAVA</option>
            <option>Python</option>
            <option>AI</option>
          </select>
        </span>
        <span>
          문제 유형:
          <button @click="changeQuestionType" class="select-btn btn">{{ questionType[questionId] }}</button>
        </span>
        <span>
          난이도:
          <select name="difficulty" v-model="difficulty">
            <option>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
            <option>5</option>
          </select>
        </span>
      </div>
      <input type="text" placeholder="문제 입력" class="input-default" v-model="questionText" />
      <p class="btn" @click="showCodeBox=!showCodeBox">{{ showCodeBox ? '-코드 삭제' : '+코드 추가' }}</p>
      <textarea
        id="question-box"
        placeholder="코드 입력"
        style="min-height:150px"
        class="input-default"
        v-if="showCodeBox"
        @keydown="setInputDefault"
        v-model="codeText"
      ></textarea>
      <br />
      <h2>정답</h2>
      <div v-if="questionId===1">
        <input type="text" placeholder="정답 입력" class="input-default" v-model="answer" />
      </div>
      <div v-if="questionId===2">
        <input type="text" placeholder="정답 입력" class="input-default" v-model="answer" />
        <h2>보기</h2>
        <input type="text" name="examples" class="input-default" v-model="examples[0]" />
        <input type="text" name="examples" class="input-default" v-model="examples[1]" />
        <input type="text" name="examples" class="input-default" v-model="examples[2]" />
        <input type="text" name="examples" class="input-default" v-model="examples[3]" />
      </div>
      <div v-if="questionId===3" @click="onClickOX">
        <label class="ox-label o ox-deactivate" for="answer-o">O</label>
        <input class="ox-input" type="radio" name="answer" id="answer-o" value="O" v-model="answer" />
        <label class="ox-label x ox-deactivate" for="answer-x">X</label>
        <input class="ox-input" type="radio" name="answer" id="answer-x" value="X" v-model="answer" />
      </div>
      <div v-if="questionId===4">
        <input type="text" placeholder="정답 입력" class="input-default" v-model="answer" />
      </div>
      <h2>해설</h2>
        <input type="text" placeholder="해설 입력" class="input-default" v-model="해설" />
      <div class="float-right">
        <span class="success-message">문제가 등록되었습니다.</span>
        <button id="submit-btn" class="submit-btn btn" @click="onClickSubmit">문제 등록</button>
      </div>
    </div>
    <div class="question-container">
      <h2>문제 미리보기</h2>
      <p>카테고리: {{category}} || 문제유형: {{ questionType[questionId] }} || 난이도:{{difficulty}}</p>
      <p>{{questionText}}</p>
      <div class="code-box" v-html="codeHTML" v-if="showCodeBox"></div>
      <h2>정답</h2>
      <p>{{answer}}</p>
      <div v-if="questionId===2">
        <h2>보기</h2>
        <ol>
          <li v-for="(e, i) in examples" :key="i">{{e}}</li>
        </ol>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "@/api/api.service.js";

export default {
  name: "QuestionForm",
  data() {
    return {
      questionType: ["", "인터뷰", "객관식", "O/X", "주관식"],
      questionId: 1,
      category: "",
      difficulty: 1,
      questionText: "",
      showCodeBox: false,
      codeText: "",
      answer: "",
      examples: ["", "", "", ""],
      recentOXButton:'',
      해설: ''
    };
  },
  methods: {
    setDataDefault() {
      (this.questionId = 1),
        (this.category = ""),
        (this.difficulty = 1),
        (this.questionText = ""),
        (this.showCodeBox = false),
        (this.codeText = ""),
        (this.answer = ""),
        (this.examples = ["", "", "", ""]);
    },
    onClickSubmit() { // 문제 등록
      if (!this.category || !this.questionText || !this.answer)
        return alert(
          "잘못된 입력입니다.(카테고리 미선택. 문제, 답변 미입력 등..)"
        );
      let question = {
        problems: {
          p_question: this.questionText,
          pc_value: this.category,
          pt_id: this.questionId,
          pd_id: this.difficulty
        },
        answer: this.answer
      };
      if (this.showCodeBox) question["problems"]["p_code"] = this.codeText;
      if (this.questionId == 2) question["examples"] = this.examples;
      axios
        .post("/api/problems/create_prob/", question)
        .then(res => {
          let successMessage = document.querySelector(".success-message");
          successMessage.classList.add("ani-show");
          setTimeout(() => {
            successMessage.classList.remove("ani-show");
          }, 1000);
          this.setDataDefault();
        });
    },
    changeQuestionType() {
      this.questionId = ((this.questionId + 1) % 5) || 1;
    },
    setInputDefault() { // 코드 입력창 tab 설정
      if (event.keyCode === 9) {
        event.preventDefault();
        this.codeText += "  ";
      }
    },
    onClickOX() { // OX 클릭시 class 변경
      if (event.target.nodeName === 'LABEL' && this.recentOXButton !== event.target) {
        if (this.recentOXButton) {
          this.recentOXButton.classList.add('ox-deactivate')
        }
        event.target.classList.remove('ox-deactivate')
        this.recentOXButton = event.target
      }
    }
  },
  computed: {
    codeHTML: function() {
      return `<pre style="margin:0;">${this.codeText}</pre>`;
    }
  }
};
</script>
<style scoped>
@font-face {
  font-family: "HangeulNuri-Bold";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_three@1.0/HangeulNuri-Bold.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
* {
  font-family: HangeulNuri-Bold;
}
h1 {
  text-align: center;
}
textarea {
  font-size: 20px;
}
pre {
  margin: 0;
}
ol {
  text-align: inherit;
}
li {
  list-style: none;
}
.wrapper {
  display: flex;
  height: 100%;
}
.btn {
  cursor: pointer;
}
.select-btn {
  width: 80px;
  height: 25px;
  font-weight: 300px;
  border: none;
  box-shadow: 0 0 2px 0 rgba(62, 65, 68, 0.9);
  background-color: white;
  border-radius: 5px;
  outline: none;
}
.submit-btn {
  width: 80px;
  height: 35px;
  font-weight: 300px;
  border: none;
  box-shadow: 0 0 2px 0 rgba(62, 65, 68, 0.9);
  background-color: white;
  border-radius: 5px;
  outline: none;
}
.success-message {
  color: green;
  margin-right: 10px;
  opacity: 0;
}
.ani-show {
  animation: show 1s;
}
@keyframes show {
  0% {
    opacity: 0;
  }
  25% {
    opacity: 1;
  }
  75% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}
.float-right {
  float: right;
}
.input-container {
  width: 50%;
  height: 100%;
  display: inline-block;
  text-align: center;
}
.question-container {
  width: 50%;
  height: 100%;
  display: inline-block;
  text-align: center;
}
.code-box {
  margin: 5%;
  padding: 12px;
  border-radius: 5px;
  background-color: rgb(235, 235, 235);
  text-align: initial;
  font-size: 20px;
  font-weight: 500;
}
.input-default {
  width: 100%;
  height: 40px;
  outline: none;
  padding: 0 8px;
  margin: 4px 0;
}
.ox-label {
  width: 100px;
  height: 100px;
  line-height: 100px;
  display: inline-block;
  font-size: 25px;
  cursor: pointer;
  border-radius: 5px;
  margin: 10px 20px;
}
.ox-input {
  display: none;
}
.o {
  color: #4CAF50;
  background-color: #E8F5E9;
  border: 2px solid #A5D6A7;
}
.x {
  color: #F44336;
  background-color: #FFEBEE;
  border: 2px solid #EF9A9A;
}
.ox-deactivate {
  color: black;
  background-color: white;
  border: 2px solid #888;
}
</style>