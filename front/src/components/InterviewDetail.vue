<template>
  <div class="interview-detail-container">
    <div class="interview-nav" @click="closeInterview"> 닫기 </div>
    {{p_info.p_id}}
    {{p_info.p_question}}
    {{p_info.p_commentary}}
    {{p_info.p_code}}
    {{p_info.myinter_check}}
  </div>
</template>
<script>
  export default {
    data() {
      return {
      }
    },
    props: {
      p_info: Object,
      // p_id: Number,
      // p_question: String,
      // p_commentary: String,
      // p_code: String,
      // myinter_check: Boolean
    },
    methods: {
      closeInterview() {
        console.log('click')
        this.$emit('close-interview')
      }
    }
  }
</script>
<style scoped>
  * {
    box-sizing: border-box;
  }
.interview-detail-container {
  width: 100%;
  height: 100%;
  position: absolute;
  top:0;
  left:0;
  background-color: white;
}
.interview-nav {
  width: 100%;
  height: 20px;
  background-color: red;
}
</style>