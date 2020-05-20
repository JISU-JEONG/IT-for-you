<template>
  <div>
    <form class="user-form" @submit.prevent="userCreate">
        <!-- <label for="user_id">id: </label>
        <input 
        v-model = "user_id"
        type="text" id="user_id"><hr> -->
        <label for="password" id="password">password: </label>
        <input type="password"
        v-model="password" id="password"><hr>
        <label for="name">name: </label>
        <input type="text"
        v-model="name" id="name"><hr>
        <label for="email">email: </label>
        <input type="text"
        v-model="email" id="email">
         <input type = "submit" value = "submit"/>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import router from '../router'
export default {
    name: 'UserForm',
    data(){
        return {
            // user_id:'',
            name: '',
            password:'',
            email:'',
            credentials:{}
        }
    },
    methods:{
        userCreate(){
            console.log('들어옴')
            const data = {
                username: this.name,
                password: this.password,
                // id: this.user_id,
                email: this.email
            }
            console.log(data)
            // request.POST인 경우는 반드시 FormData!
            // const formData = new FormData()
            // formData.append('title', title)
            // formData.append('user', 1)
            axios.post('http://127.0.0.1:8000/api/accounts/user/', data)
                 // this.options는 computed 변수
                .then(response => {
                    console.log(this.name)
                    console.log(this.password)
                    this.credentials.username = this.name
                    this.credentials.password = this.password
                    console.log(this.credentials)
                    axios.post('http://127.0.0.1:8000/api-token-auth/',this.credentials)
                        .then(response => {
                            console.log(response)
                            console.log(response.data.token)
                            const token = response.data.token
                            this.$session.start()
                            this.$session.set('jwt', token)

                            this.$store.dispatch('login', token)
                            // home으로 가기
                            router.push('/login')
                        })
                        .catch(error => {
                            console.log(error)
                        })
                })
                .catch(error => {
                console.log(error)
                })
        }
    }
}
</script>

<style>

</style>