<template>
  <div class="interview-detail-container">
    <div class="interview-nav">
      <span class="back-btn"  @click="closeInterview"><span class="arrow-left"></span></span>
    </div>
    <div class="interview-content">
      <transition name="fade">
        <div class="content question" v-if="toggleInterview" key="question" >
          Question : {{p_info.p_question}} id : {{p_info.p_id}} company : {{p_info.p_code}} check : {{p_info.myinter_check}} 
          <button class="toggle-btn" @click="toggleInterview = !toggleInterview">{{toggleInterview ? 'show commentary' : 'show question'}}</button>
        </div>
        <div class="content commentary" v-else key="commentary">
          Commentary : {{p_info.p_commentary}}
          <button class="toggle-btn" @click="toggleInterview = !toggleInterview">{{toggleInterview ? 'show commentary' : 'show question'}}</button>
        </div>
      </transition>
    </div>
    <div class="script-content">
      <div class="my-script">
        <span v-if="!script">You can make your script</span>
        {{script}}
      </div>
      <div class="edit-my-script">

      </div>
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
  import { API_URL } from "@/api/config";
  export default {
    data() {
      return {
        toggleInterview: true,
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
        console.log('click')
        this.$emit('close-interview')
      },
      callback (msg) {
        console.debug('Event: ', msg)
      },
    },
    computed: {
      script() {
        return this.$store.getters.interviewResult
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
  height: 40px;
  line-height: 40px;
  box-shadow: 0 0 2px lightgray;
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
  overflow: scroll;
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
  width: 100%;
  height: 30%;
  padding: 12px 10px 0 10px;
}
.my-script {
  width: 100%;
  height: 100%;
  box-shadow: 0 0 8px lightgray;
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