<template>
  <div class="login">
      <div v-if="!isAuthenticated">
        <h2>로그인</h2>
        <LoginForm />
      </div>
      <div v-else>
          <a @click.prevent="logout" href="#">Logout</a>
      </div>
  </div>
</template>

<script>
import LoginForm from '@/components/LoginForm.vue'
import router from '../router'

export default {
    name: "Login",
    data() {
        return {
            isAuthenticated: this.$session.has('jwt')
        }
    },
    components:{
        LoginForm
    },
    methods:{
        logout(){
            console.log(this.$session)
            this.$session.destroy()
            this.$store.dispatch('logout')
            // router.push('/login')
        }

    },
    updated() {
        this.isAuthenticated = this.$session.has('jwt')
    }
}
</script>

<style>

</style>