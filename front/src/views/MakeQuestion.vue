<template>
  <div style="width:100%; height: 100%;">
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
</style>