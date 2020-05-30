<template>
  <div>
    <h2>여기에 정답을 입력을 하시던가 말던가</h2>
    <div>
        <h2>여기는 녹음 파일이 텍스트로 변환된것 입니다.</h2>
        <h3>{{user_text}}</h3>
    </div>
    <div>
        <h2>이거는 저장된 녹음 파일을 다시 들어 볼껍니다.</h2>
        <!-- <audio-player :src=audio /> -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name : 'interview',
    data() {
        return {
            user_text : '',
            audio : null
        }
    },
    methods : {
        Getinterview(){
            this.$session.start()
            const token = this.$session.get('jwt')
            const data = {
                token : token
            }
            // sibal에 문제 번호를 넣어 주세요
            axios.post('http://127.0.0.1:8000/api/accounts/get_interview/2/', data)
                .then(response => {
                    const data = response.data
                    this.user_text = data.content
                    this.audio = data.file
                })
                .catch(error => {
                    console.log(error)
                })
      }
    },
    mounted() {
        this.Getinterview()
    }
}
</script>

<style>

</style>