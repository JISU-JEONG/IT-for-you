<template>
  <div class="interview-detail-container">
    <div class="interview-nav">
      <button v-if="script" class="save-interview-btn" @click="submitInterview">Save this interview</button>
      <span class="back-btn"  @click="closeInterview"><span class="arrow-left"></span></span>
    </div>
    <div class="interview-content">
      <transition name="fade">
        <div class="content question" v-if="toggleInterview" key="question" >
          Question : {{p_info.p_question}} company : {{p_info.p_code}} check : {{p_info.myinter_check}} 
          <button class="toggle-btn" @click="toggleInterview = !toggleInterview">{{toggleInterview ? 'show commentary' : 'show question'}}</button>
        </div>
        <div class="content commentary" v-else key="commentary">
          Commentary : {{p_info.p_commentary}}
          <button class="toggle-btn" @click="toggleInterview = !toggleInterview">{{toggleInterview ? 'show commentary' : 'show question'}}</button>
        </div>
      </transition>
    </div>
    <div class="script-content">
      <div class="empty" v-if="!script">
        You can do something
      </div>
      <div class="my-script" v-if="script && !showEdit">
        <span v-if="!script">You can make your script</span>
        <span v-else>{{script}}</span>
        <button class="btn edit" @click="edit">edit</button>
      </div>
      <textarea v-if="showEdit" type="textarea" class="edit-my-script" v-model="editScript"></textarea>
      <button v-if="showEdit" class="btn save" @click="save">save</button>
      <button v-if="showEdit" class="btn cancle" @click="cancle">cancle</button>
    </div>
    <audio-recorder
    :upload-url="uploadurl"
    filename="interview" 
    format="wav"
    :attempts="1"
    :time="2"
    :before-recording="callback"
    :pause-recording="callback"
    :after-recording="callback"
    :select-record="callback"
    :before-upload="callback"
    :successful-upload="callback"
    :failed-upload="callback"
    :bit-rate="192"/>
  </div>
</template>
<script>
  import axios from "@/api/api.service.js"
  import { API_URL } from "@/api/config";
  export default {
    data() {
      return {
        toggleInterview: true, // ??, ?? ???? ??
        showEdit: false, // ?? ?? ? ??????
        editScript: '',
        uploadurl : API_URL+"/api/interprobs/record/",
        headers: {
          'X-Custom-Header': 'some data'
        }
      }
    },
    props: {
      p_info: Object,
    },
    methods: {
      closeInterview() {
        this.$store.commit('setInterviewResult', '')
        this.$emit('close-interview')
      },
      callback (msg) {
        console.debug('Event: ', msg)
      },
      submitInterview() {
        const token = this.$session.get("jwt");
        const headers =  {
          Authorization: `JWT ${token}`
        }
        const data = this.$store.state.question.data
        const questionData = {
          prob: this.p_info.p_id,
          content: this.script
        }
        const jsonstringfy = JSON.stringify(questionData)
        data.append('body', jsonstringfy)
        console.log(data)
        axios.post('/api/interprobs/record/', data, { headers: headers })
          .then(res => {
            console.log(res)
            
          })
          .catch(err => console.error(err))
        
      },
      edit() {
        this.editScript = this.script
        this.showEdit = true
      },
      save() {
        this.$store.commit('setInterviewResult', this.editScript)
        this.showEdit = false
      },
      cancle() {
        this.showEdit = false
      }
    },
    computed: {
      script() {
        return this.$store.getters.interviewResult
      }      
    },
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
  height: 40px;
  line-height: 40px;
  box-shadow: 0 0 2px lightgray;
}
.save-interview-btn {
  background-color: #1B5E20;
  color: white;
  padding: 4px 8px;
  margin-left: 10px;
  font-size: 16px;
  border: 1px solid #1B5E20;
  border-radius: 2px;
  cursor: pointer;
}
.back-btn{
  width: 60px;
  height: 40px;
  display: inline-block;
  padding: 2px 12px;
  cursor: pointer;
  float:right;
}
.arrow-left {
  width: 36px;
  height: 36px;
  display: inline-block;
  background-image: url('../assets/icons/arrow-down.png');
  background-repeat: no-repeat;
  background-size: cover;
}
.interview-content {
  height: 25%;
  width: 100%;
  padding: 10px;
  position: relative;
  overflow: hidden;
  box-shadow: 0 0 2px lightgray;
}
.content {
  width: 100%;
  height: 100%;
  padding: 10px 10px 25px 10px;
  position:absolute;
  top: 0;
  left: 0;
  /* overflow: scroll; */
}
.toggle-btn {
  position:absolute;
  right: 4px;
  bottom: 4px;
  padding: 4px 8px;
  font-size: 14px;
  font-weight: 500;
  border: none;
  color: #9E9E9E;
  background-color: transparent;
  text-decoration: underline;
  outline: none;
}
.script-content {
  height: 28%;
  margin: 12px 10px 0 10px;
  position: relative;
}
.my-script {
  width: 100%;
  height: 100%;
  position: absolute;
  top:0;
  left:0;
  padding: 12px;
  box-shadow: 0 0 8px lightgray;
}
.empty {
  width: 100%;
  height: 100%;
  position: absolute;
  top:0;
  left:0;
  padding: 12px;
  box-shadow: 0 0 8px lightgray;
  display: flex;
  justify-content: center;
  align-items: center;
}
.edit-my-script {
  width: 100%;
  height: 100%;  
  position:absolute;
  top:0;
  left:0;
  padding: 12px;
  border: none;
  outline: none;
  box-shadow: 0 0 4px #00BCD4;
  z-index: 2;
}
.btn {
  position:absolute;
  padding: 3px 6px;
  background-color: white;
  border: 1px solid black;
  bottom: 0;
  color: white;
  font-weight: bold;
  cursor: pointer;
}
.edit{
  right: 0;
  border-color: #3F51B5;
  background-color: #3F51B5;
  right: 0;  
}
.save {
  border-color: #4CAF50;
  background-color: #4CAF50;
  left: 0;
}
.cancle {
  border-color: #F44336;
  background-color: #F44336;
  right: 0;
}
.fade-enter-active, .fade-leave-active {
  transition: all 0.7s;
}
.fade-enter /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
  transform: translateX(100%);
}
.fade-leave-to {
  opacity: 0;
  transform: translateX(-100%);
}
</style>