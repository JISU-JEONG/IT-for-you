<style lang="scss">
@import "@/scss/icons";
</style>

<template>
  <div class="uploader-wrapper" @click="upload">
    <icon-button name="save" class="ar-icon ar-icon__xs ar-icon--no-border" />
    <span> 녹음파일->대본 </span>
  </div>
</template>

<script>
import IconButton from "./icon-button";
import UploaderPropsMixin from "@/mixins/uploader-props";
// import axios from 'axios'
import axios from "@/api/api.service.js";
export default {
  mixins: [UploaderPropsMixin],
  props: {
    record: { type: Object }
  },
  components: {
    IconButton
  },
  methods: {
    upload() {
      if (!this.record.url) {
        return;
      }
      this.$eventBus.$emit("start-upload");
      this.$session.start();
      const token = this.$session.get("jwt");
      const data = new FormData();
      data.append("audio", this.record.blob, `${this.filename}.mp3`);
      this.$store.commit("setAudioData", data);
      const headers = Object.assign(this.headers, {});
      headers[
        "Content-Type"
      ] = `multipart/form-data; boundary=${data._boundary}`;
      headers["Authorization"] = `JWT ${token}`;
      axios
        .post("/api/interprobs/record/", data, { headers: headers })
        .then(resp => {
          this.$eventBus.$emit("end-upload", {
            status: "success",
            response: resp
          });
          this.$store.commit("setInterviewResult", resp.data.content);
        })
        .catch(error => {
          this.$eventBus.$emit("end-upload", {
            status: "fail",
            response: error
          });
        });
    }
  }
};
</script>
