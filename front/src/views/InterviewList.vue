<template>
  <div class="main-container">
    <div class="card" v-for="interview in interviews" :key="interview.id">
      <div class="info">
        <p>{{interview.question}}</p>
        <div class="badge">{{interview.company}}</div>
      </div>
      <div class="btn"><span>go next</span></div>
    </div>
  </div>
</template>
<script>
  export default {
    data() {
      return {
        interviews: [
          {
            id: 1,
            cate: 'Javascript',
            question: 'var, let, const의 차이점에 대해 말해보세요',
            company: '네이버'
          },
          {
            id: 2,
            cate: 'Javascript',
            question: 'var, let, const의 차이점에 대해 말해보세요',
            company: '네이버'
          },
          {
            id: 3,
            cate: 'Javascript',
            question: 'var, let, const의 차이점에 대해 말해보세요',
            company: '네이버'
          },
          {
            id: 4,
            cate: 'Javascript',
            question: 'var, let, const의 차이점에 대해 말해보세요',
            company: '네이버'
          },
          {
            id: 5,
            cate: 'Javascript',
            question: 'var, let, const의 차이점에 대해 말해보세요',
            company: '네이버'
          },
          {
            id: 6,
            cate: 'Javascript',
            question: 'var, let, const의 차이점에 대해 말해보세요',
            company: '네이버'
          },
          {
            id: 7,
            cate: 'Javascript',
            question: 'var, let, const의 차이점에 대해 말해보세요',
            company: '네이버'
          },
          {
            id: 8,
            cate: 'Javascript',
            question: 'var, let, const의 차이점에 대해 말해보세요',
            company: '네이버'
          },
        ]
      }
    }
  }
</script>
<style scoped>
  * { box-sizing: border-box;}
.main-container {
  width: 100%;
  max-width: 500px;
  height: 100%;
  margin: 0 auto;
}
.card {
  width: 90%;
  height: 100px; /* 필요한가?*/
  display: flex;
  margin: 20px auto 0;
  font-size: 20px;
  background-color: white;
  border-radius: 5px;
  box-shadow: 0 0 2rem 0 rgba(136, 152, 170, 0.15);
}
.info {
  display: inline-block;
  width: 70%;
  height: 100%;
  padding: 8px;
}
.info p {
  font-size: 16px;
}
.badge {
  display: inline-block;
  font-size: 14px;
  padding: 3px 6px;
  color: white;
  border-radius: 5px;
  background-color: #009688
;
}
.btn {
  display: inline-block;
  width: 30%;
  height: 100%;
  padding: 16px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.btn span {
  font-size: 16px;
}
</style>