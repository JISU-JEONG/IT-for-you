import Vue from "vue";
import VueRouter from "vue-router";
import store from "../store/index";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    redirect: "/category",
    component: () => import("../views/TestHome.vue"),
    children: [
      {
        path: "category",
        name: "Category",
        component: () => import("../views/Question/Category.vue")
      },
      {
        path: "testmic",
        name: "TestMIC",
        component: () => import("../views/TestMIC.vue")
      },
      {
        path: "interview",
        name: "Interview",
        component: () => import("../views/Interview.vue")
      },
      {
        path: "detail",
        name: "detail",
        component: () => import("../components/Question/Detail.vue")
      },
      {
        path: "mynote",
        name: "mynote",
        component: () => import("../views/MyNote.vue")
      }
    ]
  },
  {
    path: "/login",
    name: "login",
    component: () => import("../views/Login.vue")
  },
  {
    path: "/wrongAnswerNote",
    name: "wrongAnswerNote",
    component: () => import("../components/Question/WrongAnswerNote.vue")
  },
  {
    path: "/admin",
    name: "Admin",
    redirect: "/admin/user",
    component: () => import("../views/Admin.vue"),
    children: [
      {
        path: "user",
        name: "User",
        component: () => import("../views/User.vue")
      },
      {
        path: "make",
        name: "MakeQuestion",
        component: () => import("../views/MakeQuestion.vue")
      },
      {
        path: "edit",
        name: "EditQuestion",
        component: () => import("../views/EditQuestion.vue")
      }
    ]
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
  scrollBehavior(to, from, savedPosition) {
    return { x: 0, y: 0 };
  }
});

router.beforeEach((to, from, next) => {
  if (sessionStorage.getItem("vue-session-key") === null) {
    if (to.path === "/login") {
      return next();
    } else {
      return next("/login");
    }
  }
  const token = JSON.parse(sessionStorage.getItem("vue-session-key"))["jwt"];
  let isLogin = false;

  if (token !== undefined) {
    isLogin = store.dispatch("loginCheck", token);
  }

  // 토큰이 없을경우
  if (isLogin === false) {
    // 이동할 페이지가 login일경우 이동가능하게(무한루프 방지)
    if (to.path === "/login") {
      return next();
    }

    // 이동할 페이지가 login이 아닐경우 login페이지로 변경
    else {
      return next("/login");
    }
  }

  // 토큰이 있을경우
  else {
    // 이전페이지가 로그인이였을 경우 다음페이지로
    if (from.path === "/login") {
      return next();
    }

    // 토큰으로 정보를 찾지 못했다면 세션값 지우고 login으로 이동
    store.dispatch("loginCheck", token);
    console.log(store.getters.getUserInfo);
    if (store.getters.getUserInfo === null) {
      sessionStorage.clear();
      return next("/login");
    }

    // 찾았을경우 다음페이지로 이동
    return next();
  }
});

export default router;
