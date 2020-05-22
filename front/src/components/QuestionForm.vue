<template>
  <div class="wrapper">
      <div class="input-container">
        <h2>문제 추가</h2>
        <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
          <span>
            카테고리: <select name="category" v-model="category">
              <option disabled value="">카테고리</option>
              <option>Web</option>
              <option>Server</option>
              <option>Algorithm</option>
              <option>DataBase</option>
              <option>AWS</option>
              <option>Network</option>
              <option>JAVA</option>
              <option>Python</option>
            </select>
          </span>
          <span>
            문제 유형: <button @click="changeQuestionType" class="select-btn btn">{{ questionType[questionId] }}</button>
          </span>
          <span>
            난이도: <select name="difficulty" v-model="difficulty">
              <option>1</option>
              <option>2</option>
              <option>3</option>
              <option>4</option>
              <option>5</option>
            </select>
          </span>
        </div>
        <input type="text" placeholder="문제 입력" class="input-default" v-model="questionText">
        <p class="btn" @click="showCodeBox=!showCodeBox">{{ showCodeBox ? '-코드 삭제' : '+코드 추가' }}</p>
        <textarea id="question-box" placeholder="코드 입력"  style="min-height:150px" class="input-default" v-if="showCodeBox" @keydown="setInputDefault" v-model="codeText"></textarea> <br>
        <h2>정답</h2>
        <div v-if="questionId===1">
          <input type="text" placeholder="정답 입력" class="input-default" v-model="answer">
        </div>
        <div v-if="questionId===2">
          <input type="text" placeholder="정답 입력"  class="input-default" v-model="answer">
          <h2>보기</h2>
          <input type="text" name="example" class="input-default" v-model="example[0]">
          <input type="text" name="example" class="input-default" v-model="example[1]">
          <input type="text" name="example" class="input-default" v-model="example[2]">
          <input type="text" name="example" class="input-default" v-model="example[3]">
        </div>
        <div v-if="questionId===3">
          <input type="radio" name="answer" value="O" v-model="answer">O
          <input type="radio" name="answer" value="X" v-model="answer">X
        </div>
        <div v-if="questionId===4">
          <input type="text" placeholder="정답 입력" class="input-default" v-model="answer">
        </div>
        <button id="submit-btn" class="submit-btn btn" @click="onClickSubmit">문제 등록</button>
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
            <li v-for="(e, i) in example" :key="i">{{e}}</li>
          </ol>
        </div>
      </div>
  </div>
</template>
<script>
import axios from 'axios'

  export default {
    name: 'QuestionForm',
    data() {
      return {
        questionType: ['','인터뷰', '객관식', 'O/X', '주관식'],
        questionId:1,
        category: '',
        difficulty: 1,
        showCodeBox: false,
        questionText: '',
        codeText:'',
        answer: '',
        example: ['', '', '', ''],
      }
    },
    methods: {
      onClickSubmit() {
        let question = {
          problems: {
            p_question: this.questionText,
            pc_value: this.category,
            pt_id: this.questionId,
            pd_id: this.difficulty,
          },
          // 정답 백엔드 통일시켜주세요!!!!!!!!!!!!!
        }
        if (this.codeText) question['p_code'] = this.codeText.replace(/"/gi, '\\"')
        console.log(question)
        // axios.post('http://k02b1011.p.ssafy.io:8085/', {hi:1})
        //   .then(res => console.log(res))
      },
      changeQuestionType() {
        this.questionId = (this.questionId + 1) % 3 + 1
      },
      setInputDefault() {
        console.log(this.codeText)
        if (event.keyCode === 9) {
          event.preventDefault()
          this.codeText += '  ' 
        }
      },
    },
    computed: {
      codeHTML: function() {
        return  `<pre style="margin:0;">${this.codeText}</pre>`
      }
    },
  }
</script>
<style scoped>
@font-face { font-family: 'HangeulNuri-Bold'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_three@1.0/HangeulNuri-Bold.woff') format('woff'); font-weight: normal; font-style: normal; }
* {font-family: HangeulNuri-Bold;}
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
  .submit-btn  {
    float: right;
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
  .float-right {float: right;}
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
</style>