<template>
  <div class="main-container">
    <div class="info">
      <h2>저장된 인터뷰</h2>
      <p>이곳에서는 여러분이 저장한 인터뷰문제를 다시 볼 수 있습니다.</p>
      <p>연습했던 음성과 해당 음성 파일의 스크립트를 다시 볼 수 있습니다.</p>
    </div>
    <h3 class="no-data" v-if="!interviewList.length">
      아직 저장된 문제가 없습니다.
    </h3>
    <span v-for="interview in interviewList" :key="interview.id" @click="showDetail(interview.id)" >
      <div class="accordion no_highlights" @click="togglePanel">{{interview.p_question}}</div>
      <div class="panel">
        <div class="interview my">
          <h3>내 인터뷰</h3>
          {{interview.p_answer}}
        </div>
        <div class="interview best">
          <h3>모범 답안</h3>
          {{interview.myanswer}}
        </div>
        <audio-player :src="interview.audio_data"/>
      </div>
    </span>

    
  </div>
</template>
<script>
  import AudioPlayer from '@/components/player'
  import axios from '@/api/api.service.js'
  export default {
    data() {
      return {
        interviewList: [],
        currentAccordion: '',
      }
    },
    components: {
      AudioPlayer
    },
    methods: {
      getMyInterview() {
        const token = this.$session.get("jwt");
        const headers =  {
          Authorization: `JWT ${token}`
        }        
        axios.get(`/api/interprobs/myinters/${this.user_id}/`, { headers: headers })
          .then(res => {
            console.log(res.data)
            this.interviewList = res.data
          })
          .catch(err => {
            console.error(err)
          })
      },
  
      showDetail(p_id) {
        const token = this.$session.get("jwt");
        const headers =  {
          Authorization: `JWT ${token}`
        }        
        axios.get(`/api/interprobs/myinters/${this.user_id}/${p_id}/`, { headers: headers })
          .then(res => {
            this.select = res.data.audio_data
            
          })
          .catch(err => {
            console.error(err)
          })
      },
      togglePanel(target) {
        if (this.currentAccordion === event.target) {
          this.showPanel(this.currentAccordion)
          this.currentAccordion = ''
          return
        }
        if (this.currentAccordion) {
          this.showPanel(this.currentAccordion)
        }
        this.showPanel(event.target)
        this.currentAccordion = event.target
      },
      showPanel(target) {
        target.classList.toggle('active')
        const panel = target.nextElementSibling
        if (panel.style.maxHeight) {
          panel.style.maxHeight = null
        } else {
          panel.style.maxHeight = panel.scrollHeight + 'px'
        }
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
  * {
    box-sizing: border-box;
  }
.no-data {
  text-align: center;
  margin-top: 24px;
}
.info {
  height: 200px;
  padding: 20px;
  color: white;
  background-color: #888;
}
.info h2 {
  text-align: center;
}
.no_highlights {
  -webkit-tap-highlight-color: transparent;
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.main-container {
  width: 100%;
  max-width: 500px;
  margin: 0 auto;
}
.accordion {
  width: 100%;
  min-height: 52px;
  padding: 4px 8px;
  display: flex;
  align-items: center;
  word-break: break-all;
  border: none;
  outline: none;
  cursor: pointer;
  color: white;
  background-color: #263238;
  box-shadow: 0 0 2px lightgray;
  transition: 0.3s;
}
.active {
  color: black;
  font-size: 16px;
  font-weight: bold;
  background-color: white;
}
.panel {
  width: 100%;
  background-color: white;
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s ease-out;
}
.interview {
  width:100%;
  height: 300px;
  padding: 10px 20px;
  overflow: scroll;
  border-top: 1px solid lightgray;
}
.interview h3 {
  margin-bottom: 8px;
}
.my {
}
</style>