<template>
  <div class="main-container">
    <p>이곳은 인터뷰 풀어본 문젱비니다.</p>
    {{user_id}}
  </div>
</template>
<script>
  import axios from '@/api/api.service.js'
  export default {
    data() {
      return {

      }
    },
    methods: {
      getMyInterview() {
        axios.get(`/api/interprobs/myinters/${this.user_id}/`)
          .then(res => {
            console.log(res)
          })
          .catch(err => {
            console.error(err)
          })

      }
    },
    computed: {
      user_id() {
        return this.$store.getters.user
      }
    },
    mounted() {
      this.getMyInterview()
    }
  }
</script>
<style scoped>

</style>