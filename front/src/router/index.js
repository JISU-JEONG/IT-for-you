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
        path: "detail",
        name: "Detail",
        component: () => import("../views/Question/Detail.vue")
      },
      {
        path: "testmic",
        name: "TestMIC",
        component: () => import("../views/TestMIC.vue")
      }
    ],
    meta: {
      needAuthUser: true
    }
  },
  {
    path: "/login",
    name: "login",
    component: () => import("../views/Login.vue"),
    meta: {
      needAuthUser: false
    }
  },
  {
    path: "/profile",
    name: "profile",
    component: import("../views/Profile.vue"),
    meta: {
      needAuthUser: true
    }
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
    ],
    meta: {
      needAuthUser: true
    }
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

router.beforeEach((to, from, next) => {
  const flag = to.matched.some(m => m.meta.needAuthUser);
  // // 로그인 제외 페이지 이동
  if (flag) {
    if (store.getters.userState === null) {
      return next("/login");
    } else {
      return next();
    }
  }
  // // 로그인 되어있다면
  else {
    if (store.getters.userState === null) {
      return next();
    } else {
      return next("category");
    }
  }
});

export default router;
