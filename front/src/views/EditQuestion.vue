<template>
  <div>
    <h2>ㅇㅁㄴㅇ</h2>
    <button @click="loadQuestion">문제 조회</button>
  </div>
</template>
<script>
import axios from 'axios'
export default {
    data() {
      return {
      }
    },
    methods: {
      loadQuestion() {
        axios.get('http://k02b1011.p.ssafy.io/api/problems/create_prob/')
        console.log('asd')
      }
    }
}
</script>
<style scoped>
  h1 {color: white}
</style>