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
    component: () => import("../views/Question/WrongAnswerNote.vue")
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
  // 세션이 없을경우 로그인페이지로
  if (token === undefined) {
    // 이동할 페이지가 login일경우 이동가능하게(무한루프 방지)
    if (to.path === "/login") {
      return next();
    }

    // 이동할 페이지가 login이 아닐경우 login페이지로 변경
    else {
      return next("/login");
    }
  }
  store.dispatch("loginCheck", token);
  setTimeout(() => {
    isLogin = store.getters.getUserInfo;

    // 토큰만료시
    if (isLogin === null) {
      if (to.path === "/login") {
        return next();
      }

      // 이동할 페이지가 login이 아닐경우 login페이지로 변경
      return next("/login");
    } else {
      if (to.path === "/login") {
        return next("/");
      }
      return next();
    }
  }, 300);
});

export default router;
