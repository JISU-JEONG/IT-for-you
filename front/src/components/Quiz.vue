<template>
  <body>
    <div id="subhead">
      <p>
        모든 코드는 내가 짠다 :
        <a href="mailto:kempfjj@gmail.com">김태우</a>
      </p>
    </div>

    <ul id="questionsList">
      <section
        :class="i === 0 ? 'current' : ''"
        v-for="(q, i) in quiz"
        :key="i"
      >
        {{ q.level }}<br />
        {{ q.type }}배
        <li>
          <p>
            {{ q.question }}
          </p>
          <span class="questionItem" v-for="a in q.answer" :key="a">
            <input :id="a" type="radio" :name="q.answer" :value="a" /><label
              :for="a"
              >{{ a }}</label
            >
          </span>
        </li>
        <a
          href="#"
          :id="i === quiz.length - 1 ? 'submitAnswers' : ''"
          :class="i === quiz.length - 1 ? 'finalButton' : 'nextButton'"
          >Next Question &gt;</a
        >
      </section>
    </ul>
  </body>
</template>

<script>
export default {
  name: "Quiz",
  data() {
    return {
      quiz: [
        {
          question: "Vue.js의 라이프 사이클이 아닌 것은?",
          answer: ["computed", "created", "mounted", "beforemount"],
          type: "web",
          level: 1
        },
        {
          question: "2번째 문제",
          answer: ["a", "b", "c", "d"],
          type: "test",
          level: 2
        }
      ]
    };
  },
  methods: {
    // getClassName(i, size) {
    //   if (i === 0) {
    //     return "current";
    //   } else if (i === size) {
    //     return "";
    //   }
    // }
  },
  mounted() {
    require("@/utils/quiz.js");
    require("@/assets/style/quiz.css");
  }
};
</script>
