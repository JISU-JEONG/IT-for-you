<template>
<body>
  <div id="subhead">
    <p>
      모든 코드는 내가 짠다 :
      <a href="#">김태우</a>
    </p>
  </div>

  <ul id="questionsList">
    <section :class="i === 0 ? 'current' : ''" v-for="(q, i) in Question" :key="i">
      레벨 : {{ q.level }}
      <br />
      타입 : {{ q.type }}
      <li>
        <p>{{ q.question }}</p>
        <span class="questionItem" v-for="a in q.answer" :key="a">
          <input :id="a" type="radio" :name="q.answer" :value="a" />
          <label :for="a">{{ a }}</label>
        </span>
      </li>
      <a
        href="#"
        :id="i === Question.length - 1 ? 'submitAnswers' : ''"
        :class="i === Question.length - 1 ? 'finalButton' : 'nextButton'"
      >Next Question &gt;</a>
    </section>
  </ul>
</body>
</template>

<script>
import * as Question from "./Question.js";
export default {
  name: "Question",
  data() {
    return {
      Question: Question.data()
    };
  },
  mounted() {
    require("./QuestionDetail.css");
    require("./QuestionDetail.js");
  }
};
</script>
