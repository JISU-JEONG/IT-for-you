import Vue from "vue";
import VueRouter from "vue-router";
import Profile from "../views/Profile.vue";

Vue.use(VueRouter);

const routes = [
  // {
  //   path: "/",
  //   name: "Home",
  //   component: () => import("../views/Home.vue"),
  // },
  {
    path: "/",
    name: "Home",
    redirect: '/category',
    component: () => import("../views/TestHome.vue"),
    children: [
      {
        path: "category",
        name: "Category",
        component: () => import("../views/Question/Category.vue"),
      },
      {
        path: "detail",
        name: "Detail",
        component: () => import("../views/Question/Detail.vue"),
      },
      {
        path: "testmic",
        name: "TestMIC",
        component: () => import("../views/TestMIC.vue"),
      },
    ]
  },

  // {
  //   path: "/category",
  //   name: "Category",
  //   component: () => import("../views/Question/Category.vue"),
  // },
  // {

  //   path: "/detail",
  //   name: "Detail",
  //   component: () => import("../views/Question/Detail.vue"),
  // },
  {
    path: "/login",
    name: "login",
    component: () => import("../views/Login.vue"),
  },
  {
    path: '/profile',
    name: 'profile',
    component: Profile
  },
  {
    path: '/admin',
    name: 'Admin',
    redirect: '/admin/user',
    component: () => import("../views/Admin.vue"),
    children: [
      {
        path: "user",
        name: "User",
        component: () => import("../views/User.vue"),
      },
      {
        path: "make",
        name: "MakeQuestion",
        component: () => import("../views/MakeQuestion.vue"),
      },
      {
        path: "edit",
        name: "EditQuestion",
        component: () => import("../views/EditQuestion.vue"),
      },
    ],
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
