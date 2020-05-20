<template>
  <div>
    <h1>문제 등록하기</h1>
    <hr>
    <div style="display: flex;">
      <div class="input-container">
        <h2>문제</h2>
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
        문제 유형: <button @click="changeQuestionType" class="change-type-btn">{{ questionType[questionId] }}</button> <br>
        <textarea cols="50" rows="5" v-model="questionText"></textarea> <br>
        <p class="add-code-btn" @click="showCodeBox=!showCodeBox">{{ showCodeBox ? '-코드 삭제' : '+코드 추가' }}</p>
        <textarea id="question-box" cols="50" rows="10" v-if="showCodeBox" @keydown="setInputDefault" v-model="codeText"></textarea> <br>
        <h2>정답</h2>
        <div v-if="questionId===1">
          <input type="text" name="" id="" v-model="answer">
        </div>
        <div v-if="questionId===2">
          <input type="text" name="" id="" v-model="answer">
          <h2>보기</h2>
          <input type="text" name="example" id="" v-model="example[0]">
          <input type="text" name="example" id="" v-model="example[1]">
          <input type="text" name="example" id="" v-model="example[2]">
          <input type="text" name="example" id="" v-model="example[3]">
        </div>
        <div v-if="questionId===3">
          <input type="radio" name="answer" value="O" v-model="answer">O
          <input type="radio" name="answer" value="X" v-model="answer">X
        </div>
        <button id="btn">문제 등록</button>
      </div>
      <div class="question-container"> 
        <h2>문제</h2>
        <p>카테고리: {{category}} || 문제유형: {{ questionType[questionId] }}</p>
        <p>{{questionText}}</p>
        <div class="code-box" v-html="codeHTML" v-if="showCodeBox"></div>
        <h2>정답</h2>
        <p>{{answer}}</p>
        <div v-if="questionId===2">
          <h2>보기</h2>
          <ol>
            <li v-for="e in example" :key="e">{{e}}</li>
          </ol>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    name: 'QuestionForm',
    data() {
      return {
        questionType: ['','주관식', '객관식', 'O/X'],
        questionId:1,
        category: '',
        showCodeBox: false,
        questionText: '',
        codeText:'',
        answer: '',
        example: ['', '', '', ''],
      }
    },
    methods: {
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
  .change-type-btn {
    cursor: pointer;
  }
  .add-code-btn {
    cursor: pointer;
  }
  .input-container {
    width: 50%;
    display: inline-block;
    text-align: center;
    border: 1px black solid;
  }
  .question-container {
    width: 50%;
    display: inline-block;
    text-align: center;
    border: 1px red solid;
  }
  .code-box {
    margin: 5%;
    padding: 12px;
    border-radius: 5px;
    background-color: rgb(235, 235, 235);
    text-align: initial;
    font-size: 20px;
    font-weight: 600;
  }
</style>