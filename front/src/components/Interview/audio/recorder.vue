<style lang="scss">
.no_highlights {
  -webkit-tap-highlight-color: transparent;
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.ar {
  width: 100%;
  padding-top: 16px;
  margin: 0 auto;
  font-family: "Roboto", sans-serif;
  background-color: #fafafa;
  box-shadow: 0 4px 18px 0 rgba(0, 0, 0, 0.17);
  position: absolute;
  bottom: 0;
  box-sizing: border-box;
  &-content {
    /* width:100%; */
    /* padding: 16px; */
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  &-records {
    width: 100%;
    height: 97px;
    padding-top: 8px;
    overflow-y: auto;
    /* margin-bottom: 20px; */

    &__record {
      width: 100%;
      height: 45px;
      padding: 0 10px;
      margin: 0 auto;
      line-height: 45px;
      display: flex;
      justify-content: space-between;
      border-top: 1px solid #e8e8e8;
      border-bottom: 1px solid #e8e8e8;
      position: relative;

      &--selected {
        /* border: 1px solid #E8E8E8; */
        /* border-radius: 24px; */
        background-color: #ffffff;
        margin-top: -1px;
        padding: 0 34px;
      }
    }
  }

  &-recorder {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;

    &__duration {
      color: #aeaeae;
      font-size: 32px;
      font-weight: 500;
      margin-top: 20px;
      margin-bottom: 16px;
    }

    &__stop {
      position: absolute;
      top: 10px;
      right: -52px;
    }

    &__time-limit {
      position: absolute;
      color: #aeaeae;
      font-size: 12px;
      top: 128px;
    }

    &__records-limit {
      position: absolute;
      color: #aeaeae;
      font-size: 13px;
      top: 78px;
    }
  }

  &-spinner {
    display: flex;
    height: 30px;
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    margin: auto;
    width: 144px;
    z-index: 10;

    &__dot {
      display: block;
      margin: 0 8px;
      border-radius: 50%;
      width: 30px;
      height: 30px;
      background: #05cbcd;
      animation-name: blink;
      animation-duration: 1.4s;
      animation-iteration-count: infinite;
      animation-fill-mode: both;

      &:nth-child(2) {
        animation-delay: 0.2s;
      }

      &:nth-child(3) {
        animation-delay: 0.4s;
      }

      @keyframes blink {
        0% {
          opacity: 0.2;
        }
        20% {
          opacity: 1;
        }
        100% {
          opacity: 0.2;
        }
      }
    }
  }

  &__text {
    color: rgba(84, 84, 84, 0.5);
    font-size: 16px;
  }

  &__blur {
    filter: blur(2px);
    opacity: 0.7;
  }

  &__overlay {
    position: absolute;
    width: 100%;
    height: 100%;
    z-index: 10;
  }

  &__upload-status {
    text-align: center;
    font-size: 10px;
    padding: 2px;
    letter-spacing: 1px;
    position: absolute;
    bottom: 0;

    &--success {
      color: green;
    }

    &--fail {
      color: red;
    }
  }

  &__rm {
    cursor: pointer;
    color: #f44336;
  }

  &__downloader,
  &__uploader {
    display: flex;
    justify-content: space-around;
    align-items: center;
    position: absolute;
    width: 50%;
    height: 45px;
    bottom: -46px;
    margin: auto;
    cursor: pointer;
    background-color: #ffffff;
    border-bottom: 1px solid #e8e8e8;
  }

  &__downloader {
    left: 0;
    color: #4caf50;
  }

  &__uploader {
    right: 0;
    color: #2196f3;
    border-left: 1px solid #e8e8e8;
  }
}

@import "@/scss/icons";
</style>

<template>
  <div class="ar">
    <div class="ar__overlay" v-if="isUploading"></div>
    <div class="ar-spinner" v-if="isUploading">
      <div class="ar-spinner__dot"></div>
      <div class="ar-spinner__dot"></div>
      <div class="ar-spinner__dot"></div>
    </div>

    <div class="ar-content" :class="{ ar__blur: isUploading }">
      <div class="ar-recorder">
        <icon-button
          class="ar-icon ar-icon__lg no_highlights"
          :name="iconButtonType"
          :class="{
            'ar-icon--rec': isRecording,
            'ar-icon--pulse': isRecording && volume > 0.02
          }"
          @click.native="toggleRecorder"
        />
        <icon-button
          class="ar-icon ar-icon__sm ar-recorder__stop no_highlights"
          name="stop"
          @click.native="stopRecorder"
        />
      </div>

      <!-- <div class="ar-recorder__records-limit" v-if="attempts">Attempts: {{attemptsLeft}}/{{attempts}}</div> -->
      <div class="ar-recorder__duration">{{ recordedTime }}</div>
      <div class="ar-recorder__time-limit" v-if="time">
        Record duration is limited: {{ time }}m
      </div>

      <div class="ar-records">
        <div
          class="ar-records__record ar-records__record--selected no_highlights"
          :key="record.id"
          v-for="(record, idx) in recordList"
          @click="choiceRecord(record)"
        >
          <div class="ar__text">인터뷰 ({{ record.duration }})</div>
          <div class="ar__rm no_highlights" @click="removeRecord(idx)">
            파일 삭제
          </div>

          <downloader
            v-if="showDownloadButton"
            class="ar__downloader"
            :record="record"
            :filename="filename"
          />

          <uploader
            v-if="showUploadButton"
            class="ar__uploader"
            :record="record"
            :filename="filename"
            :headers="headers"
            :upload-url="uploadUrl"
          />
        </div>
      </div>

      <audio-player :record="selected" />
    </div>
  </div>
</template>

<script>
import AudioPlayer from "./player";
import Downloader from "./downloader";
import IconButton from "./icon-button";
import Recorder from "@/lib/recorder";
import Uploader from "./uploader";
import UploaderPropsMixin from "@/mixins/uploader-props";
import { convertTimeMMSS } from "@/lib/utils";

export default {
  mixins: [UploaderPropsMixin],
  props: {
    attempts: { type: Number },
    time: { type: Number },

    bitRate: { type: Number, default: 128 },
    sampleRate: { type: Number, default: 44100 },

    showDownloadButton: { type: Boolean, default: true },
    showUploadButton: { type: Boolean, default: true },

    micFailed: { type: Function },
    beforeRecording: { type: Function },
    pauseRecording: { type: Function },
    afterRecording: { type: Function },
    failedUpload: { type: Function },
    beforeUpload: { type: Function },
    successfulUpload: { type: Function },
    selectRecord: { type: Function }
  },
  data() {
    return {
      isUploading: false,
      recorder: this._initRecorder(),
      recordList: [],
      selected: {},
      uploadStatus: null
    };
  },
  components: {
    AudioPlayer,
    Downloader,
    IconButton,
    Uploader
  },
  mounted() {
    this.$eventBus.$on("start-upload", () => {
      this.isUploading = true;
      this.beforeUpload && this.beforeUpload("before upload");
    });

    this.$eventBus.$on("end-upload", msg => {
      this.isUploading = false;

      if (msg.status === "success") {
        this.successfulUpload && this.successfulUpload(msg.response);
      } else {
        this.failedUpload && this.failedUpload(msg.response);
      }
    });
  },
  beforeDestroy() {
    this.stopRecorder();
  },
  methods: {
    toggleRecorder() {
      if (this.recordList[0]) {
        if (confirm("현재 녹음된 파일은 지워집니다")) {
          this.removeRecord(0);
          this.$store.commit("setInterviewResult", "");
        } else {
          return;
        }
      }
      if (this.attempts && this.recorder.records.length >= this.attempts) {
        return;
      }

      if (!this.isRecording || (this.isRecording && this.isPause)) {
        this.recorder.start();
      } else {
        this.recorder.pause();
      }
    },
    stopRecorder() {
      if (!this.isRecording) {
        return;
      }

      this.recorder.stop();
      this.recordList = this.recorder.recordList();
      this.choiceRecord(this.recordList[0]);
    },
    removeRecord(idx) {
      this.recordList.splice(idx, 1);
      this.$set(this.selected, "url", null);
      this.$store.commit("setAudioData", new FormData());
      this.$store.commit("setInterviewResult", "");
      this.$eventBus.$emit("remove-record");
    },
    choiceRecord(record) {
      if (this.selected === record) {
        return;
      }
      this.selected = record;
      this.selectRecord && this.selectRecord(record);
    },
    _initRecorder() {
      return new Recorder({
        beforeRecording: this.beforeRecording,
        afterRecording: this.afterRecording,
        pauseRecording: this.pauseRecording,
        micFailed: this.micFailed,
        bitRate: this.bitRate,
        sampleRate: this.sampleRate,
        format: this.format
      });
    }
  },
  computed: {
    attemptsLeft() {
      return this.attempts - this.recordList.length;
    },
    iconButtonType() {
      return this.isRecording && this.isPause
        ? "mic"
        : this.isRecording
        ? "pause"
        : "mic";
    },
    isPause() {
      return this.recorder.isPause;
    },
    isRecording() {
      return this.recorder.isRecording;
    },
    recordedTime() {
      if (this.time && this.recorder.duration >= this.time * 60) {
        this.stopRecorder();
      }
      return convertTimeMMSS(this.recorder.duration);
    },
    volume() {
      return parseFloat(this.recorder.volume);
    }
  }
};
</script>
