<template>
  <div clas="make-question-wrapper">
    <h1>?? ????</h1>
    <QuestionForm />
  </div>
</template>
<script>
  import QuestionForm from "@/components/QuestionForm.vue";

export default {
  name: 'MakeQuestion',
  components: {
    QuestionForm,
  },
  data() {
    return {

    }
  },
  
    
}
</script>
<style scoped>
  h1 {color: white}
  .make-question-wrapper {
    height: 100%;
  }
</style>