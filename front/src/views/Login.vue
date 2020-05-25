<template>
  <div class="login">
      <div v-if="!isAuthenticated">
        <LoginForm />
      </div>
      <div v-else>
          <a @click.prevent="check" href="#">profile</a>
          <br>
          <a @click.prevent="logout" href="#">Logout</a>
      </div>
  </div>
</template>

<script>
import LoginForm from '@/components/LoginForm.vue'
import router from '../router'
import axios from 'axios'

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
        },
        // signup(){
        //     router.push('/signup')
        // },
        check(){
            // this.$session.start()
            // const token = this.$session.get('jwt')
            // const data = {
            //     token : token,
            // }
            // axios.post('http://127.0.0.1:8000/api/accounts/user/', data)
            // .then(response => {
            //     console.log(response)
            // })
            // .catch(error => {
            //     console.log(error)
            // })
            router.push('/profile')
        },
    },
    updated() {
        this.isAuthenticated = this.$session.has('jwt')
    }
}
</script>

<style scoped>
  .login {
    width: 100vw;
    height: 100vh;
  }

</style>