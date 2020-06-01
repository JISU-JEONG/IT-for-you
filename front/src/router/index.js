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
      }
    ]
  },
  {
    path: "/login",
    name: "login",
    component: () => import("../views/Login.vue")
  },
  {
    path: "/detail",
    name: "detail",
    component: () => import("../components/Question/Detail.vue")
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

  if (isLogin === false) {
    if (to.path === "/login") {
      return next();
    } else {
      return next("/login");
    }
  } else {
    store.dispatch("loginCheck", token);
    // console.log(store.getters.getUserInfo);
    return next();
  }
});

export default router;
