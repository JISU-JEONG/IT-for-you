<template>
  <div>
    <h2>여기에 정답을 입력을 하시던가 말던가</h2>
    <div>
        <h2>여기는 녹음 파일이 텍스트로 변환된것 입니다.</h2>
        <h3>{{text}}</h3>
    </div>
    <div>
        <h2>이거는 저장된 녹음 파일을 다시 들어 볼껍니다.</h2>
        <h2>{{path}}</h2>
        <vue-audio :file="path" />
    </div>
  </div>
</template>

<script>

import axios from "../api/api.service.js"
import VueAudio from 'vue-audio';

export default {
    name : 'interview',
    data() {
        return {
            mp3: 'interview.mp3',
            text : '',
            path : '',
            selected:{}
        }
    },
    components: {
     'vue-audio': VueAudio
    },
    methods : {
        Getinterview(){
            this.$session.start()
            const token = this.$session.get('jwt')
            const data = {
                token : token
            }
            // sibal에 문제 번호를 넣어 주세요
            axios.post('/api/accounts/get_interview/2/', data)
                .then(response => {
                    const data = response.data
                    this.text = data.content
                    this.path = data.path
                    console.log(data)
                })
                .catch(error => {
                    console.log(error)
                })
      }
    },
    mounted() {
        this.Getinterview()
        
    },
}
</script>

<style>

</style>