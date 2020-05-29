<template>
  <div>
    <h2>ID : {{ this.data.username }}</h2>
    <h2>email : {{ this.data.email }}</h2>
    <h2>name : {{ this.data.username }}</h2>

    <a @click.prevent="userDelete" href="#">회원 탈퇴</a>
  </div>
</template>

<script>
import router from "../router";
import axios from "@/api/api.service.js";

export default {
  name: "Profile",
  data() {
    return {
      data: {},
      user: {}
    };
  },
  methods: {
    isLogin() {
      this.$session.start();
      // session에 jwt가 없다면, 즉 토큰이 없다면, 비로그인이라면,
      if (!this.$session.has("jwt")) {
        router.push("/login");
      } else {
        // 로그인 되어있다면, vuex token 업데이트
        this.$store.dispatch("login", this.$session.get("jwt"));
      }
    },
    getUser() {
      // axios 요청시마다 헤더를 추가해서 보내야 함!
      this.$session.start();
      const token = this.$session.get("jwt");
      const options = {
        headers: {
          Authorization: `JWT ${token}` // JWT 다음에 공백있음.
        }
      };
      axios
        .post("/api/accounts/user/", {}, options)
        .then(({ data }) => {
          console.log(data);
          this.data = data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    userDelete() {
      this.$session.start();
      const token = this.$session.get("jwt");
      const data = {
        token: token
      };
      axios
        .post("http://127.0.0.1:8000/api/accounts/user_delete/", data)
        .then(response => {
          console.log(response); // 만약, 오류가 발생하게 되면 ESLint 설정을 package.json에 추가
          this.data = response.data;
          console.log(this.data);
          this.$session.destroy();
          this.$store.dispatch("logout");
          router.push("/login");
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  mounted() {
    this.isLogin();
    this.getUser();
  }
};
</script>
